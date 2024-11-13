import psutil

def get_network_details(pid):
    source_ips = set()
    destination_ips = set()
    network_packets = 0

    try:
        process = psutil.Process(pid)
        connections = process.connections(kind='inet')

        for conn in connections:
            source_ips.add(conn.laddr.ip if conn.laddr else "N/A")
            destination_ips.add(conn.raddr.ip if conn.raddr else "N/A")
            network_packets += 1  # Placeholder for actual packet count

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

    return [list(source_ips), list(destination_ips), network_packets]