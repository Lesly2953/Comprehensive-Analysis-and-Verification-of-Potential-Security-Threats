import wmi
import psutil 
import MainMemoryDumpFile as main_dmp
import SuspectedProcess as susproc

f = wmi.WMI()

#print(wmi.WMI().Win32_Process.methods.keys());

#print(wmi.WMI().Win32_Process.properties.keys());

#print("PID                 Process Name")

# for process in f.WIN32_Process():
#   owner_info = process.GetOwner();
#   owner_name = f"{owner_info[0]}\\{owner_info[2]}" if owner_info[2] else "N/A"
#   print("ID: {0}\nName: {1}\nOwner Name: {2}\nDescription: {3}\n".format(process.ProcessId , process.Name , owner_name , process.Description));

sus_process = []

dump_file = "main_memory_dump.dmp"



def info_running_process():
  for proc in psutil.process_iter(['pid','name','exe']):
    try:
      process_info = proc.info
      main_dmp.create_memory_dump(process_info['pid'],dump_file)
      if(susproc.susProcess(process_info)):
        sus_process.append([process_info['pid'],process_info['name']])
      print(f'''ID : {process_info['pid']}\nName: {process_info['name']}\nFolder Path: {process_info['exe']}\n''');
    except (psutil.NoSuchProcess , psutil.AccessDenied,psutil.ZombieProcess):
      print("Error");
  return sus_process;