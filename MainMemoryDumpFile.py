import ctypes
import sys

# Define necessary constants
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
MEMORY_BASIC_INFORMATION = ctypes.sizeof(ctypes.c_ulonglong) * 5 + ctypes.sizeof(ctypes.c_uint) * 2

def create_memory_dump(pid, dump_file):
    try:
        kernel32 = ctypes.windll.kernel32
        process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)

        if not process:
            raise ctypes.WinError(ctypes.get_last_error())

        with open(dump_file, 'wb') as dump:
            address = 0
            mbi = ctypes.create_string_buffer(MEMORY_BASIC_INFORMATION)

            while kernel32.VirtualQueryEx(process, ctypes.c_void_p(address), mbi, ctypes.sizeof(mbi)):
                mbi_contents = struct.unpack("QIIQQQQ", mbi.raw)  # Unpack structure
                base_address = mbi_contents[0]
                region_size = mbi_contents[3]
                state = mbi_contents[4]

                if state == 0x1000:  # MEM_COMMIT
                    buffer = ctypes.create_string_buffer(region_size)
                    bytesRead = ctypes.c_size_t(0)

                    if kernel32.ReadProcessMemory(process, ctypes.c_void_p(base_address), buffer, region_size, ctypes.byref(bytesRead)):
                        dump.write(buffer.raw[:bytesRead.value])

                address += region_size

        kernel32.CloseHandle(process)
        print(f"Memory dump created at {dump_file}")

    except Exception as e:
        print(f"Failed to create memory dump: {e}", file=sys.stderr)









