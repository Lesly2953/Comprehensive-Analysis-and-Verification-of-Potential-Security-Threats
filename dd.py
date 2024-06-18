import psutil
import pymem
import os

def dump_process_memory(pid, dump_file):
    try:
        pm = pymem.Pymem()
        pm.open_process_from_id(pid)
        process_name = psutil.Process(pid).name()
        process_module = pymem.process.module_from_name(pm.process_handle, process_name)

        base_address = process_module.lpBaseOfDll
        size = process_module.SizeOfImage

        memory_dump = pm.read_bytes(base_address, size)
        dump_file.write(memory_dump)

        print(f"Memory dump of {process_name} (PID: {pid}) saved to the dump file")
    except Exception as e:
        print(f"An error occurred with PID {pid}: {e}")

def list_running_processes(dump_file_path):
    # Get a list of all running processes
    processes = psutil.process_iter(['pid', 'name', 'memory_info'])

    # Open the dump file once for writing
    with open(dump_file_path, 'wb') as dump_file:
        # Print the header
        print(f"{'PID':<10}{'Name':<25}{'Memory Usage (RSS)'}")

        for process in processes:
            try:
                # Get the process info
                pid = process.info['pid']
                name = process.info['name']
                memory_info = process.info['memory_info']
                memory_usage = memory_info.rss  # Resident Set Size

                # Print the process info
                print(f"{pid:<10}{name:<25}{memory_usage / (1024 * 1024):.2f} MB")

                # Dump process memory
                dump_process_memory(pid, dump_file)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

if __name__ == "__main__":
    list_running_processes('system_memory_dump.bin')
