from termcolor import colored


# Splits a string into n equal parts
def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 8):
        chunk = string_f[i:i + 8]
        grouped.append(chunk)

    return grouped


def subnet(masked_addr_f, addr_type):
    addr_bin = ''
    if addr_type == "net_addr":
        addr_bin = f"{masked_addr_f:0<32}"
    elif addr_type == "broad_addr":
        addr_bin = f"{masked_addr_f:1<32}"
    elif addr_type == "first_ip":
        addr_bin = f"{masked_addr_f:0<32}"[:-1] + "1"
    elif addr_type == "last_ip":
        addr_bin = f"{masked_addr_f:1<32}"[:-1] + "0"

    addr_sep = str_splitter(str(addr_bin))
    addr_dec = [f"{int(x, 2)}" for x in addr_sep]

    ip_f = ".".join(addr_sep), ".".join(addr_dec)
    for i in ip_f:
        print("=> ", i)


def valid_ip():
    while True:
        try:
            ip_dec_f = input("Enter IPv4 address: ")
            ip_dec_f = ip_dec_f.split(".")
            if (len(ip_dec_f) == 4) and all(x in range(0, 256) for x in list(map(int, ip_dec_f))):
                return ip_dec_f
            print("Invalid IPv4 address")
        except ValueError as ve:
            print(ve)


def valid_mask():
    while True:
        try:
            cidr_f = int(input("Enter mask bits (8-31): "))
            if int(cidr_f) in range(8, 32):
                return int(cidr_f)
            else:
                print("Invalid mask")
        except ValueError as ve:
            print(ve)


while True:
    ip_dec = valid_ip()
    cidr = valid_mask()
    host_bits = 32 - cidr
    print("=> ", ".".join(ip_dec), ": ip address")
    netmask_bin = f"{('1' * cidr):0<32}"
    netmask_oct = str_splitter(netmask_bin)
    netmask_dec = [f"{int(x, 2)}" for x in netmask_oct]
    print("=> ", ".".join(netmask_dec), ": subnet mask")
    ip_bin = list(map(lambda x: f"{int(x):08b}", ip_dec))
    # Isolate the network portion
    masked_addr = "".join(ip_bin)[:cidr]
    print("=> ", ".".join(ip_bin), ": ip binary")
    print("=> ", ".".join(netmask_oct),  ': netmask binary')
    print("=> ", masked_addr + "|  " + "".join(ip_bin)[cidr::], ":", host_bits, "host bits")
    print("=> ", "".join(netmask_bin)[:cidr] + "|  " + "".join(netmask_bin)[cidr::], ":", cidr, "network bits")

    print(colored("Network address", 'yellow'))
    subnet(masked_addr, 'net_addr')

    print(colored("Broadcast address", 'yellow'))
    subnet(masked_addr, 'broad_addr')

    print(colored("First usable IP address", 'yellow'))
    subnet(masked_addr, 'first_ip')

    print(colored("Last usable IP address", 'yellow'))
    subnet(masked_addr, 'last_ip')

    print(colored("Total number of hosts", 'yellow'))
    total_addr = 2 ** host_bits
    print("=> ", total_addr)
    print(colored("Usable IP hosts addresses", 'yellow'))
    usable_ips = 2 ** host_bits - 2
    print("=> ", usable_ips)
    print(colored(f"Total number of subnets for /{cidr} networks", 'yellow'))
    print("=> ", 2 ** (cidr % 8))
