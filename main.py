import RunningProcess as run_proc
import NetworkDetails as net_det
from ip_checking import is_ip_legitimate
import csv
import os

ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY","Key paste here")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "Key paste here")

def main():
    suspected_processes = run_proc.info_running_process()
    network_details = []
    
    for proc in suspected_processes:
        pid, name = proc
        source_ips, dest_ips, packet_count = net_det.get_network_details(pid)
        
        # Check each destination IP
        legitimate_ips = []
        suspicious_ips = []
        for ip in dest_ips:
            if ip != "N/A":
                if is_ip_legitimate(ip, ABUSEIPDB_API_KEY, VIRUSTOTAL_API_KEY):
                    legitimate_ips.append(ip)
                else:
                    suspicious_ips.append(ip)
        
        network_details.append([pid, name, source_ips, legitimate_ips, suspicious_ips, packet_count])
    
    # results to a CSV file
    with open("process_network_details.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["PID", "Process Name", "Source IPs", "Legitimate Destination IPs", "Suspicious Destination IPs", "Network Packets"])
        for detail in network_details:
            writer.writerow(detail)
    
    print(f"Process and network details have been written to process_network_details.csv")

if __name__ == "__main__":
    main()
