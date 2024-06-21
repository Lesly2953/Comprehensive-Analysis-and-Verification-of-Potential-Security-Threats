import wmi
import psutil 
import win32api

f = wmi.WMI()

#print(wmi.WMI().Win32_Process.methods.keys());

#print(wmi.WMI().Win32_Process.properties.keys());

#print("PID                 Process Name")

# for process in f.WIN32_Process():
#   owner_info = process.GetOwner();
#   owner_name = f"{owner_info[0]}\\{owner_info[2]}" if owner_info[2] else "N/A"
#   print("ID: {0}\nName: {1}\nOwner Name: {2}\nDescription: {3}\n".format(process.ProcessId , process.Name , owner_name , process.Description));

sus_process = []

def get_company_info(file_path):
  try:
    info = win32api.GetFileVersionInfo(file_path,'\\');
    lang , codepage = win32api.GetFileVersionInfo(file_path, '\\VarFileInfo\\Translation')[0]
    #string_file_info = info['StringFileInfo'];
    #print(string_file_info);
    str_info_path = f'\\StringFileInfo\\{lang:04x}{codepage:04x}\\CompanyName'
    company_name = win32api.GetFileVersionInfo(file_path , str_info_path);
    return company_name
  except Exception as e:
    return 'null'

def info_running_process():
  for proc in psutil.process_iter(['pid','name','exe']):
    try:
      process_info = proc.info
      company_name = get_company_info(process_info['exe']);
      if(company_name == 'null'):
        sus_process.append([process_info['pid'], process_info['name']]);
      print(f'''ID : {process_info['pid']}\nName: {process_info['name']}\nFolder Path: {process_info['exe']}\nCompany Name: {company_name}\n\n''');
    except (psutil.NoSuchProcess , psutil.AccessDenied,psutil.ZombieProcess):
      print("Error");
  return sus_process;
