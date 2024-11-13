import psutil
import SuspectedProcess as susproc

def info_running_process():
    suspected_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            process_info = proc.info
            if susproc.susProcess(process_info):
                suspected_processes.append([process_info['pid'], process_info['name']])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print(f"Error accessing process information for PID: {proc.pid}")
    return suspected_processes