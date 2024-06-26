import struct

def read_memory_dump(dump_file):
    try:
        with open(dump_file, 'rb') as f:
            print("Reading dump file...")

            # Read and print the entire content in hexadecimal format
            content = f.read()
            hex_output = content.hex()
            for i in range(0, len(hex_output), 32):
                print(hex_output[i:i+32])
            
            print("\nInterpreting as 32-bit integers:")
            f.seek(0)
            while True:
                bytes_read = f.read(4)
                if not bytes_read:
                    break
                value = struct.unpack('I', bytes_read)[0]
                print(f"Read integer: {value}")

    except Exception as e:
        print(f"Failed to read memory dump: {e}")

# Replace with the path to your dump file
dump_file_path = 'main_memory_dump.dmp'
read_memory_dump(dump_file_path)

