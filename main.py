from sys import argv

SERVER_SUFFIX = "-Master-1"

def gen_file(region_name: str, ip_address: str = "127.0.0.1", port: int = 22023):
    if (len(region_name) + len(SERVER_SUFFIX) > 0xff):
        raise ValueError("Region name too long")
    if (len(ip_address) > 0xff):
        raise ValueError("IP-address too long")
    if (port > 0xffff * 5):
        raise ValueError("Port too high")

    # Append region name
    data = bytearray([0x00] * 4 + [len(region_name)])
    data += region_name.encode("ascii")
    
    # Append ip address
    data.extend([len(ip_address)])
    data += ip_address.encode("ascii")
    data.extend([0x01] + [0x00] * 3)
    
    # Append server name
    server_name = region_name + SERVER_SUFFIX
    data.extend([len(server_name)])
    data += server_name.encode("ascii")
    
    # Append ip address in byte form
    ip_address_bytes = bytearray()
    for value in ip_address.split("."):
        ip_address_bytes.extend([int(value)])
    data += ip_address_bytes
    data.extend([port & 0xff, (port & 0xff00) >> 8])
    data.extend([0x00] * 4)

    print(data)
    return data

"""
Creates and writes the among us regionInfo.dat file
Example:
```py
try:
    writeFile("Example server", "169.0.0.1", port=12345))
    print("Success!")
except Exception as error:
    print(error)
```
"""
def write_file(region_name: str, ip_address: str = "127.0.0.1", file_name: str = "regionInfo.dat", port: int = 22023):
    data = gen_file(region_name, ip_address, port)
    with open(file_name, "wb") as file:
        file.write(data)

if __name__ == "__main__":
    print(f"Creating file using {argv[1:]}")
    write_file(*argv[1:])