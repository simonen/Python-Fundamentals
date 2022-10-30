from termcolor import colored


# Splits a string into n equal parts
def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 8):
        chunk = string_f[i:i + 8]
        grouped.append(chunk)

    return grouped


def subnet_mask(cidr_f):
    mask_dec = ['0', '0', '0', '0']
    bytes_full = cidr_f // 8
    borrowed_bits = cidr_f % 8
    for i in range(0, bytes_full):
        mask_dec[i] = '255'
        if i + 1 < len(mask_dec):
            mask_dec[i + 1] = f"{256 - 2 ** (8 - borrowed_bits)}"

    mask_bin = list(map(lambda x: f"{int(x):08b}", mask_dec))
    return mask_dec, mask_bin


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
    return ".".join(addr_sep), ".".join(addr_dec)


def print_addr(ip_f):
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
            cidr_f = int(input("Enter mask bits (1-31): "))
            if int(cidr_f) in range(1, 32):
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
    subnet_dec = subnet_mask(cidr)[0]
    print("=> ", ".".join(subnet_dec), ": subnet mask")
    subnet_bin = subnet_mask(cidr)[1]
    ip_bin = list(map(lambda x: f"{int(x):08b}", ip_dec))
    # Isolate the network portion
    masked_addr = "".join(ip_bin)[:cidr]
    print("=> ", masked_addr + "| " + "".join(ip_bin)[cidr::])
    print("=> ", "".join(subnet_bin)[:cidr] + "| " + "".join(subnet_bin)[cidr::])
    print("=> ", ".".join(ip_bin))
    print("=> ", ".".join(subnet_bin))
    # print("=> ", ip_bin, ": ip address binary")
    # print("=> ", subnet_bin, ": subnet mask binary")

    print(colored("Network address", 'yellow'))
    print_addr(subnet(masked_addr, 'net_addr'))

    print(colored("Broadcast address", 'yellow'))
    print_addr(subnet(masked_addr, 'broad_addr'))

    print(colored("First usable IP address", 'yellow'))
    print_addr(subnet(masked_addr, 'first_ip'))

    print(colored("Last usable IP address", 'yellow'))
    print_addr(subnet(masked_addr, 'last_ip'))

    print(colored("Total number of hosts", 'yellow'))
    total_addr = 2 ** host_bits
    print("=> ", total_addr)
    print(colored("Usable IP hosts addresses", 'yellow'))
    usable_ips = 2 ** host_bits - 2
    print("=> ", usable_ips)
