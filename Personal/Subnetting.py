# Splits a string into n equal parts
def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 8):
        chunk = string_f[i:i + 8]
        grouped.append(chunk)

    return grouped


def subnet_mask(cidr_f):
    mask_dec = [0, 0, 0, 0]
    bytes_full = cidr_f // 8
    borrowed_bits = cidr_f % 8
    for i in range(0, bytes_full):
        mask_dec[i] = '255'
        if i + 1 < len(mask_dec):
            mask_dec[i + 1] = f"{256 - 2 ** (8 - borrowed_bits)}"

    mask_bin = list(map(lambda x: f"{int(x):08b}", mask_dec))
    return mask_dec, mask_bin


def network_addr(masked_addr_f):
    # Isolate the network portion
    net_address_bin = f"{masked_addr_f:0<32}"
    net_addr_oct = str_splitter(net_address_bin)
    net_addr_dec = [f"{int(x, 2)}" for x in net_addr_oct]
    return net_address_bin, net_addr_oct, net_addr_dec


def broadcast_addr(masked_addr_f):
    broadcast_bin = f"{masked_addr:1<32}"
    broadcast_bin_oct = str_splitter(broadcast_bin)
    broadcast_dec = [f"{int(x, 2)}" for x in broadcast_bin_oct]
    return broadcast_bin, broadcast_bin_oct, broadcast_dec


def first_ip(masked_addr_f):
    net_address_bin = f"{masked_addr:0<32}"
    first_ip_bin = net_address_bin[:-1] + "1"
    first_ip_oct = str_splitter(str(first_ip_bin))
    first_ip_dec = [f"{int(x, 2)}" for x in first_ip_oct]
    return first_ip_bin, first_ip_oct, first_ip_dec


def last_ip(masked_addr_f):
    broadcast_bin = f"{masked_addr:1<32}"
    last_ip_bin = broadcast_bin[:-1] + "0"
    last_ip_oct = str_splitter(str(last_ip_bin))
    last_ip_dec = [f"{int(x, 2)}" for x in last_ip_oct]
    return last_ip_bin, last_ip_oct, last_ip_dec


def print_addr(ip_f):
    for i in ip_f:
        print("=> ", i)


while True:
    ip_dec = input("Enter IP address: ").split(".")
    cidr = int(input("Mask bits: "))
    host_bits = 32 - cidr

    print("=> ", ".".join(ip_dec), ": ip address")
    subnet_dec = subnet_mask(cidr)[0]
    subnet_bin = subnet_mask(cidr)[1]
    ip_bin = list(map(lambda x: f"{int(x):08b}", ip_dec))
    masked_addr = "".join(ip_bin)[:cidr]
    print("=> ", subnet_dec, ": subnet mask")
    print("=> ", ip_bin, ": ip address binary")
    print("=> ", subnet_bin, ": subnet mask binary")

    print("Network address")
    # print("=> ", network_addr(masked_addr)[0])
    # print("=> ", network_addr(masked_addr)[1], ": network address binary")
    # print("=> ", network_addr(masked_addr)[2])
    print_addr(network_addr(masked_addr))

    print("Broadcast address")
    print("=> ", broadcast_addr(masked_addr)[0])
    print("=> ", broadcast_addr(masked_addr)[1], "broadcast address binary")
    print("=> ", broadcast_addr(masked_addr)[2])

    print("First usable IP address")
    print("=> ", first_ip(masked_addr)[0])
    print("=> ", first_ip(masked_addr)[1])
    print("=> ", first_ip(masked_addr)[2])

    print("Last usable IP address")
    print("=> ", last_ip(masked_addr)[0])
    print("=> ", last_ip(masked_addr)[1])
    print("=> ", last_ip(masked_addr)[2])

    print("Total number of hosts")
    total_addr = 2 ** host_bits
    print("=> ", total_addr)
    print("Usable IP hosts addresses")
    usable_ips = 2 ** host_bits - 2
    print("=> ", usable_ips)
