def ip_calc(ip_f, addr_type, bin_dec_f):
    ip_bin_f = [f"{x:08b}" for x in map(int, ip_f)]
    masked_addr = "".join(ip_bin_f)[:cidr]
    addr_bin = ''
    if addr_type == "net_addr":
        addr_bin = f"{masked_addr:0<32}"
    elif addr_type == "broad_addr":
        addr_bin = f"{masked_addr:1<32}"
    elif addr_type == "first_ip":
        addr_bin = f"{masked_addr:0<32}"[:-1] + "1"
    elif addr_type == "last_ip":
        addr_bin = f"{masked_addr:1<32}"[:-1] + "0"

    addr_sep = str_splitter(addr_bin)
    addr_dec = [f"{int(x, 2)}" for x in addr_sep]
    if bin_dec_f == "bin":
        return addr_sep, ".".join(addr_sep)

    return addr_dec, ".".join(addr_dec)


def ip_class(ip_bin_f):
    addr_class = ''
    if ip_bin_f[0] == "0":
        addr_class = "A"
    elif ip_bin_f[:2] == "10":
        addr_class = "B"
    elif ip_bin_f[:3] == "110":
        addr_class = "C"
    elif ip_bin_f[:4] == "1110":
        addr_class = "D"

    return addr_class


def ip_scope(ip_bin_f, ip_f):
    scope = 'public'
    if ip_f[0] == '10' or (ip_f[0] == "172" and ip_bin_f[9:13] == "0001")\
            or (ip_f[0] == "192" and ip_f[1] == '168'):
        scope = 'private'

    return scope


def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 8):
        chunk = string_f[i:i + 8]
        grouped.append(chunk)

    return grouped


def str_split2(string_ff, index_f):
    if string_ff[index_f - 1] != ".":
        string_ff = string_ff[:index_f] + ' ' + string_ff[index_f::]
    return string_ff


def cidr_dotted(cidr_f, bin_dec_f):
    netmask_bin_f = f"{('1' * cidr_f):0<32}"
    netmask_dotted = str_splitter(netmask_bin_f)
    netmask_dec_str = ".".join([f"{int(x, 2)}" for x in netmask_dotted])
    if bin_dec_f == "bin":
        return ".".join(netmask_dotted)
    return netmask_dec_str


def valid_ip():
    while True:
        try:
            ip_dec_f = input(" Enter IPv4 address: ")
            ip_dec_f = ip_dec_f.split(".")
            if (len(ip_dec_f) == 4) and all(x in range(0, 256) for x in list(map(int, ip_dec_f))):
                return ip_dec_f
            print(" Invalid IPv4 address!")
            print()
        except ValueError as ve:
            print(ve)


def valid_mask():
    while True:
        try:
            cidr_f = int(input(" Enter mask bits (8-30): "))
            if int(cidr_f) in range(8, 32):
                return int(cidr_f)
            else:
                print("Invalid mask")
        except ValueError as ve:
            print(ve)


while True:
    print()
    print(f"{'### IPv4 Subnet Calculator v0.1 by don_simone ###'}")
    print()
    ip = valid_ip()
    cidr = valid_mask()

    octet = cidr // 8
    netmask_dec = cidr_dotted(cidr, 'dec')
    netmask_bin = cidr_dotted(cidr, 'bin')
    index = netmask_bin.find("0")
    ip_dec = '.'.join(ip)
    ip_bin = '.'.join([f"{x:08b}" for x in map(int, ip)])
    net_addr = ip_calc(ip, 'net_addr', 'dec')
    net_addr_bin = ip_calc(ip, 'net_addr', 'bin')
    broad_addr = ip_calc(ip, 'broad_addr', 'dec')
    broad_addr_bin = ip_calc(ip, 'broad_addr', 'bin')
    first_host = ip_calc(ip, 'first_ip', 'dec')
    first_host_bin = ip_calc(ip, 'first_ip', 'bin')
    last_host = ip_calc(ip, 'last_ip', 'dec')
    last_host_bin = ip_calc(ip, 'last_ip', 'bin')
    wildcard_dec = [str(255 - int(x)) for x in netmask_dec.split(".")]
    wildcard_bin = ".".join([f"{x:08b}" for x in map(int, wildcard_dec)])
    hex_id = ".".join([f"{x:02x}" for x in map(int, ip)])
    arpa = ".".join([x for x in ip[::-1]])
    subnet_count = 2 ** (cidr % 8)
    host_bits = 32 - cidr
    total_addr = 2 ** host_bits
    usable_ips = total_addr - 2
    dashes = 85
    char = '='

    print(char * dashes)
    print(f" {ip_dec} /{cidr}")
    print(char * dashes)

    address = 'host address'
    if ip_dec == net_addr[1]:
        address = 'network address'
    elif ip_dec == broad_addr[1]:
        address = 'broadcast address'

    print(f" {address : <21} {ip_dec : <21} {str_split2(ip_bin, index)}")
    print(f" {'subnet mask' : <21} {netmask_dec : <21} {str_split2(netmask_bin, index)}")
    print(f" {'network address' : <21} {net_addr[1] : <21} {net_addr_bin[1]}")
    print(f" {'broadcast address' : <21} {broad_addr[1] : <21} {broad_addr_bin[1]}")
    print(f" {'first host' : <21} {first_host[1] : <21} {first_host_bin[1]}")
    print(f" {'last host' : <21} {last_host[1] : <21} {last_host_bin[1]}")
    print(f" {'wildcard mask' : <21} {'.'.join(wildcard_dec) :<21} {wildcard_bin}")
    print("-" * dashes)
    print(f" {'class' : <21} {ip_class(ip_bin)}")
    print(f" {'scope' : <21} {ip_scope(ip_bin, ip)}")
    print(f" {'hex id' : <21} 0x{hex_id}")
    print(f" {'in-addr.arpa' : <21} {arpa}.in-addr.arpa")
    print("-" * dashes)

    print(f" {'total addresses' : <21} {total_addr}  \n"
          f" {'host addresses' : <21} {usable_ips}")

    print(char * dashes)
    print(f" All of the {subnet_count} possible /{cidr} networks for {'.'.join(ip[:octet]) + '.*' * (4 - octet)}")
    print(char * dashes)
    print(f" {'network address' : <18} | {'range of usable host addresses' : ^39} | {'broadcast address': <18}")

    network = 0
    bin_table = [128, 64, 32, 16, 8, 4, 2, 1]
    for _ in range(subnet_count):
        net_addr[0][octet] = str(network)
        print("-" * dashes)
        marked = ''
        start = int(ip_calc(net_addr[0], 'first_ip', 'dec')[0][octet])
        end = int(ip_calc(net_addr[0], 'last_ip', 'dec')[0][octet])
        if start < int(ip[octet]) < end:
            marked = "*"
        print(f" {'.'.join(net_addr[0]) : <18} | {ip_calc(net_addr[0], 'first_ip', 'dec')[1]: >18} - {ip_calc(net_addr[0], 'last_ip', 'dec')[1] : <18} | {ip_calc(net_addr[0], 'broad_addr', 'dec')[1]} {marked}")
        network += bin_table[cidr % 8 - 1]
    print()
