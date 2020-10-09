from sys import argv

# Currently the only possible value
SERVER_SUFFIX = "-Master-1"


def gen_file(region_name: str, ip_address: str = "127.0.0.1", port: int = 22023) -> bytearray:
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


def write_file(region_name: str, ip_address: str = "127.0.0.1", file_name: str = "regionInfo.dat", port: int = 22023):
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
    Port should currently always be 22023 for it to work
    """

    # Generate the file and save to the specified file_name
    data = gen_file(region_name, ip_address, port)
    with open(file_name, "wb") as file:
        file.write(data)


if __name__ == "__main__":
    print(f"Creating file using {argv[1:]}")
    write_file(*argv[1:])
