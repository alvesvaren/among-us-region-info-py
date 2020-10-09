#!/usr/bin/python

from sys import argv

# Currently the only possible value
SERVER_SUFFIX = "-Master-1"


def gen_stream(region_name: str, ip_address: str = "127.0.0.1", port: int = 22023) -> bytearray:
    """
    Generates the bytearray with the specified values.
    Port should currently always be 22023 for it to work
    """

    # Make sure all variables are within the correct length range
    if (len(region_name + SERVER_SUFFIX) > 0xff):
        raise ValueError("Region name too long")
    if (len(ip_address) > 0xff):
        raise ValueError("IP-address too long")
    if (port > 0x7fff):
        raise ValueError("Port too high")

    # Append region name
    data = bytearray(len(region_name).to_bytes(5, "big"))
    data += region_name.encode("ascii")

    # Append ip address
    data.append(len(ip_address))
    data += ip_address.encode("ascii")
    data.extend(0x1.to_bytes(4, "little"))

    # Append server name
    server_name = region_name + SERVER_SUFFIX
    data.append(len(server_name))
    data += server_name.encode("ascii")

    # Append ip address in byte form
    ip_address_bytes = bytearray()
    for value in ip_address.split("."):
        ip_address_bytes.append(int(value))
    data += ip_address_bytes
    data.extend(port.to_bytes(2, "little"))
    data.extend(0x0.to_bytes(4, "big"))

    return data


def write_file(region_name: str, ip_address: str = "127.0.0.1", file_name: str = "regionInfo.dat", port: int = 22023, *, log_bytes=False):
    """
    Creates and writes the among us regionInfo.dat file. 
    Port should currently always be 22023 for it to work


    Example:
    ```py
    try:
        write_file("Example server", "127.0.0.1", port=12345))
        print("Success!")
    except Exception as error:
        print(error)
    ```
    """

    # Generate the file and save to the specified file name
    data = gen_stream(region_name, ip_address, port)
    with open(file_name, "wb") as file:
        file.write(data)

    # Log the bytes to stdout if specified
    if (log_bytes):
        print("Writing", content_from_stream(data), "to", file_name)


def content_from_stream(stream: bytearray) -> str:
    """
    Create a string with the bytes in 'stream'
    """
    hex_array = []
    for byte in stream:
        hex_array.append(hex(byte))
    return "{" + ", ".join(hex_array) + "}"


if __name__ == "__main__":
    if (len(argv) < 2):
        print('Usage: python main.py <name> [ip-address] [file-name] [port]')
        print('Example: python main.py "Server name" 127.0.0.1')
        exit(1)
    print(f"Creating file using arguments '{', '.join(argv[1:])}'")
    try:
        write_file(*argv[1:], log_bytes=True)
    except Exception as error:
        print("Error:", error)
        exit(2)
