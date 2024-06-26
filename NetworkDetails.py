import psutil
import socket
import ctypes
import struct
from ctypes import wintypes
import win32process
import win32api
import win32con
import pandas as pd

# Function to get the company name from the process executable
# def get_company_name(executable_path):
#     try:
#         size = win32api.GetFileVersionInfoSize(executable_path)
#         if not size:
#             return "N/A"

#         res = win32api.GetFileVersionInfo(executable_path, "\\")
#         if not res:
#             return "N/A"

#         str_info = win32api.VerQueryValue(res, r'\\StringFileInfo\\040904E4\\CompanyName')
#         if not str_info:
#             return "N/A"
        
#         return str_info
#     except:
#         return "N/A"

# Function to get network details of a process
def get_network_details(pid):
    source_ips = []
    destination_ips = []
    network_packets = 0

    try:
        process = psutil.Process(pid)
        connections = process.connections(kind='inet')

        for conn in connections:
            source_ip = conn.laddr.ip
            if conn.raddr:
                destination_ip = conn.raddr.ip
            else:
                destination_ip = "N/A"

            source_ips.append(source_ip)
            destination_ips.append(destination_ip)
            network_packets += 1  # Placeholder for actual packet count
    except:
        pass

    return [source_ips, destination_ips, network_packets]

# List to hold process details
# process_list = []

# # Get the list of all processes
# processes = psutil.process_iter()

# # Iterate through all processes
# for process in processes:
#     try:
#         # Get process details
#         pid = process.pid
#         name = process.name()
#         memory_info = process.memory_info()
#         memory_usage = memory_info.rss

#         # Get the executable path
#         executable_path = process.exe()

#         # Get company name
#         company_name = get_company_name(executable_path)

#         # Get network details
#         source_ips, destination_ips, network_packets = get_network_details(pid)

#         if network_packets == 0:
#             source_ips = ["N/A"]
#             destination_ips = ["N/A"]

#         # Add process details to the list
#         for src_ip, dest_ip in zip(source_ips, destination_ips):
#             process_list.append({
#                 'PID': pid,
#                 'Name': name,
#                 'Memory Usage': memory_usage,
#                 'Company': company_name,
#                 'Source IP': src_ip,
#                 'Destination IP': dest_ip,
#                 'Network Packets': network_packets
#             })

#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass

# # Create a DataFrame from the process list
# df = pd.DataFrame(process_list)

# # Save the DataFrame to a CSV file
# df.to_csv('process_details.csv', index=False)

# print("Process details saved to process_details.csv")
