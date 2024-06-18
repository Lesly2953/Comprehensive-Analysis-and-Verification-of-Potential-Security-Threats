import psutil
import pymem
import os

def dump_process_memory(process_name, dump_file_path):
    try:
        pm = pymem.Pymem(process_name)
        process = pymem.process.module_from_name(pm.process_handle, process_name)
        
        base_address = process.lpBaseOfDll
        size = process.SizeOfImage

        with open(dump_file_path, 'wb') as dump_file:
            memory_dump = pm.read_bytes(base_address, size)
            dump_file.write(memory_dump)

        print(f"Memory dump of {process_name} saved to {dump_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_running_processes():
    # Get a list of all running processes
    processes = psutil.process_iter(['pid', 'name', 'memory_info'])

    # Print the header
    print(f"{'PID':<10}{'Name':<25}{'Memory Usage (RSS)'}")

    for process in processes:
        try:
            # Get the process info
            pid = process.info['pid']
            name = process.info['name']
            memory_info = process.info['memory_info']
            dump_process_memory(name,'process_memory_dump.bin')
            memory_usage = memory_info.rss  # Resident Set Size

            # Print the process info
            print(f"{pid:<10}{name:<25}{memory_usage / (1024 * 1024):.2f} MB")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    list_running_processes()
