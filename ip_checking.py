import requests

def check_ip_abuseipdb(ip, api_key):
    url = f"https://api.abuseipdb.com/api/v2/check"
    querystring = {"ipAddress": ip, "maxAgeInDays": "90"}
    headers = {"Accept": "application/json", "Key": api_key}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def check_ip_virustotal(ip, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"accept": "application/json", "x-apikey": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def is_ip_legitimate(ip, abuseipdb_key, virustotal_key):
    abuse_result = check_ip_abuseipdb(ip, abuseipdb_key)
    vt_result = check_ip_virustotal(ip, virustotal_key)

    is_legitimate = (abuse_result.get('data', {}).get('abuseConfidenceScore', 100) < 50 and
                     vt_result.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious', 1) == 0)
    
    return is_legitimate