import win32api

def get_company_info(file_path):
  try:
    info = win32api.GetFileVersionInfo(file_path,'\\');
    lang , codepage = win32api.GetFileVersionInfo(file_path, '\\VarFileInfo\\Translation')[0]
    #string_file_info = info['StringFileInfo'];
    #print(string_file_info);
    str_info_path = f'\\StringFileInfo\\{lang:04x}{codepage:04x}\\CompanyName'
    company_name = win32api.GetFileVersionInfo(file_path , str_info_path);
    return True
  except Exception as e:
    return False


def susProcess(process_info):
  if(get_company_info(process_info['exe'])):
    return False
  return True