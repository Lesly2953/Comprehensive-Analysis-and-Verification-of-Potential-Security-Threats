import pandas as pd

# Read the CSV file created by the previous script
df = pd.read_csv('process_details.csv')

# Filter the processes that are sending network packets to any source
df_filtered = df[df['Network Packets'] > 0]

# Print the details of processes sending network packets
print("Processes sending network packets:")
print(df_filtered)

# Optionally, save the filtered results to a new CSV file
df_filtered.to_csv('process_sending_network_packets.csv', index=False)

print("Filtered process details saved to process_sending_network_packets.csv")
