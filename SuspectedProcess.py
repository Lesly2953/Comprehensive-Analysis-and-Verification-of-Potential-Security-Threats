import win32api
import os
import logging

# Set up logging
logging.basicConfig(filename='suspected_process.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_company_info(file_path):
    if not os.path.exists(file_path):
        logging.warning(f"File does not exist: {file_path}")
        return None

    try:
        info = win32api.GetFileVersionInfo(file_path, '\\')
        lang, codepage = win32api.GetFileVersionInfo(file_path, '\\VarFileInfo\\Translation')[0]
        str_info_path = f'\\StringFileInfo\\{lang:04x}{codepage:04x}\\CompanyName'
        company_name = win32api.GetFileVersionInfo(file_path, str_info_path)
        return company_name
    except Exception as e:
        logging.error(f"Error getting company info for {file_path}: {str(e)}")
        return None

def is_trusted_company(company_name):
    trusted_companies = ["Microsoft Corporation", "Google LLC", "Apple Inc."]  # Example list
    return company_name in trusted_companies

def susProcess(process_info):
    exe_path = process_info.get('exe')
    if not exe_path:
        logging.warning(f"No executable path for process: {process_info.get('name', 'Unknown')}")
        return True  # Consider it suspicious if we can't check

    company_name = get_company_info(exe_path)
    if company_name is None:
        logging.info(f"No company info for process: {process_info.get('name', 'Unknown')} ({exe_path})")
        return True  # Consider it suspicious if we can't get company info

    if is_trusted_company(company_name):
        logging.info(f"Trusted process: {process_info.get('name', 'Unknown')} ({company_name})")
        return False
    else:
        logging.info(f"Suspicious process: {process_info.get('name', 'Unknown')} ({company_name})")
        return True 