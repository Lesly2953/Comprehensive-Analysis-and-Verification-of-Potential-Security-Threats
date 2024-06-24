import ctypes
import sys

# Define necessary constants
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
MEM_COMMIT = 0x1000
PAGE_NOACCESS = 0x01

# Define MEMORY_BASIC_INFORMATION structure
class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_void_p),
        ("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", ctypes.c_ulong),
        ("RegionSize", ctypes.c_size_t),
        ("State", ctypes.c_ulong),
        ("Protect", ctypes.c_ulong),
        ("Type", ctypes.c_ulong)
    ]

def create_memory_dump(pid, dump_file):
    try:
        kernel32 = ctypes.windll.kernel32
        process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)

        if not process:
            raise ctypes.WinError(ctypes.get_last_error())

        with open(dump_file, 'wb') as dump:
            address = 0
            mbi = MEMORY_BASIC_INFORMATION()

            while kernel32.VirtualQueryEx(process, ctypes.c_void_p(address), ctypes.byref(mbi), ctypes.sizeof(mbi)):
                base_address = mbi.BaseAddress
                region_size = mbi.RegionSize
                state = mbi.State
                protect = mbi.Protect

                if state == MEM_COMMIT and not (protect & PAGE_NOACCESS):
                    buffer = ctypes.create_string_buffer(region_size)
                    bytesRead = ctypes.c_size_t(0)

                    if kernel32.ReadProcessMemory(process, ctypes.c_void_p(base_address), buffer, region_size, ctypes.byref(bytesRead)):
                        dump.write(buffer.raw[:bytesRead.value])
                        #print(f"Dumped {bytesRead.value} bytes from address {hex(base_address)}")
                    else:
                        print(f"Failed to read memory at address {hex(base_address)}: {ctypes.WinError(ctypes.get_last_error())}")
                
                address += region_size
                if address >= 0x7FFFFFFFFFFF:  # 48-bit address space for user-mode processes
                    break

        kernel32.CloseHandle(process)
        print(f"Memory dump created at {dump_file}")

    except Exception as e:
        print(f"Failed to create memory dump: {e}", file=sys.stderr)
















