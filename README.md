
# Windows Process and Network Monitor

## Overview
This Python-based tool monitors running processes on a Windows system, tracks their network connections, and identifies potentially suspicious activities. The tool checks destination IP addresses against security databases such as AbuseIPDB and VirusTotal, helping to detect threats. It generates a detailed CSV report that provides key insights for security analysis and threat detection.

## Features
- **Process Monitoring:** Continuously monitors running processes on a Windows system.
- **Network Tracking:** Tracks network connections made by each process, capturing source and destination IP addresses.
- **Threat Identification:** Cross-references destination IP addresses with AbuseIPDB and VirusTotal databases to identify potential threats.
- **Process Classification:** Classifies processes as either suspicious or legitimate based on their company information and network behavior.
- **Report Generation:** Generates a comprehensive CSV report summarizing the findings, aiding in further security analysis and investigation.

## Technologies Used
- **Python:** Core language used for development.
- **Windows API:** Used to interact with and gather information from the Windows operating system.
- **psutil:** Python library used for retrieving information on system processes and network connections.
- **AbuseIPDB API:** For checking IP addresses against a known list of abusive IPs.
- **VirusTotal API:** For checking IP addresses against virus databases for potential malicious activity.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repository/windows-process-network-monitor.git
   cd windows-process-network-monitor
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys:**
   - Obtain your API keys from [AbuseIPDB](https://www.abuseipdb.com/) and [VirusTotal](https://www.virustotal.com/).
   - Store them in an `.env` file in the root of your project:
     ```bash
     ABUSEIPDB_API_KEY=your_abuseipdb_api_key
     VIRUSTOTAL_API_KEY=your_virustotal_api_key
     ```

## Usage

1. **Run the script:**
   ```bash
   python monitor.py
   ```

2. **Monitor and Output:**
   - The script will start monitoring running processes and tracking their network connections.
   - It will classify each process and its connections as suspicious or legitimate based on database lookups.
   - A CSV report will be generated with detailed information about each process and connection.

## CSV Report
The generated CSV report contains the following columns:
- **Process Name:** The name of the running process.
- **PID:** Process ID of the running process.
- **Company Information:** The company associated with the process (if available).
- **Source IP Address:** The IP address from which the process is making a connection.
- **Destination IP Address:** The IP address to which the process is connecting.
- **AbuseIPDB Status:** Whether the destination IP is flagged in AbuseIPDB.
- **VirusTotal Status:** Whether the destination IP is flagged in VirusTotal.
- **Classification:** Whether the process is classified as suspicious or legitimate.

## Example Output

Here’s a sample of what the CSV report might look like:
| Process Name | PID  | Company        | Source IP | Destination IP | AbuseIPDB Status | VirusTotal Status | Classification |
|--------------|------|----------------|-----------|----------------|------------------|-------------------|----------------|
| chrome.exe   | 3456 | Google LLC     | 192.168.1.2 | 8.8.8.8        | Clean            | Clean             | Legitimate     |
| malware.exe  | 7890 | Unknown        | 192.168.1.2 | 1.2.3.4        | Malicious        | Malicious         | Suspicious     |

