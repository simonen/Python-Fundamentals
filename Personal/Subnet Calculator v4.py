def ip_calc(ip_f, addr_type, bin_dec_f):
    # ip_f = ip_f.split(".")
    ip_bin_f = [f"{x:08b}" for x in map(int, ip_f)]
    masked_addr = "".join(ip_bin_f)[:cidr]
    addr_bin = ''
    if addr_type == "net_addr":
        addr_bin = f"{''.join(ip_bin_f[:octet]):0<32}"
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


def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 8):
        chunk = string_f[i:i + 8]
        grouped.append(chunk)

    return grouped


def str_split2(string_ff, index_f):
    if string_ff[index_f - 1] == ".":
        string_ff = string_ff[:index_f] + '' + string_ff[index_f::]
    else:
        string_ff = string_ff[:index_f] + ' ' + string_ff[index_f::]
    return string_ff


def cidr_dotted(cidr_f, bin_dec_f):
    netmask_bin_f = f"{('1' * cidr_f):0<32}"
    netmask_dotted = str_splitter(netmask_bin_f)
    netmask_dec_str = ".".join([f"{int(x, 2)}" for x in netmask_dotted])
    if bin_dec_f == "bin":
        return ".".join(netmask_dotted)
    return netmask_dec_str


ip_dec = "192.168.44.56".split(".")
cidr = 26
octet = cidr // 8

netmask_dec = cidr_dotted(cidr, 'dec')
netmask_bin = cidr_dotted(cidr, 'bin')
index = netmask_bin.find("0")
ip_bin = ".".join([f"{x:08b}" for x in map(int, ip_dec)])
print(f"{'### Subnet Calculator v0.1 by don_simone ###': <30}")
print('ip address', "-" * 80)
print(f"{'.'.join(ip_dec)}")
print(str_split2(ip_bin, index))
print(f"{'subnet mask' : <15} {netmask_dec}")
print(f"{'cidr notation': <15} {'.'.join(ip_dec)} /{cidr}")
print(str_split2(netmask_bin, index))
print('network', "-" * 80)
net_addr = ip_calc(ip_dec, 'net_addr', 'dec')
net_addr_bin = ip_calc(ip_dec, 'net_addr', 'bin')
print(net_addr[1])
print(net_addr_bin[1])
broad_addr = ip_calc(ip_dec, 'broad_addr', 'dec')
broad_addr_bin = ip_calc(ip_dec, 'broad_addr', 'bin')
print('broadcast', "-" * 78)
print(broad_addr[1])
print(broad_addr_bin[1])
print('first usable host', "-" * 70)
first_host = ip_calc(ip_dec, 'first_ip', 'dec')
first_host_bin = ip_calc(ip_dec, 'first_ip', 'bin')
print(first_host[1])
print(first_host_bin[1])
last_host = ip_calc(ip_dec, 'last_ip', 'dec')
last_host_bin = ip_calc(ip_dec, 'last_ip', 'bin')
print('last usable host', "-" * 71)
print(last_host[1])
print(last_host_bin[1])
subnet_count = 2 ** (cidr % 8)
print("-" * 88)
host_bits = 32 - cidr
total_addr = 2 ** host_bits
usable_ips = total_addr - 2
print(f"{total_addr} total addresses | {usable_ips} usable host addresses ")
print("-" * 88)
print(f"All of the {subnet_count} possible /{cidr} networks for {net_addr[1]}")
print("-" * 88)
print(f"{'Network Address' : <17} | {'Range of Usable Host Addresses' : ^33} | {'Broadcast Address'}")
network = 0
bin_table = [128, 64, 32, 16, 8, 4, 2, 1]
for _ in range(subnet_count):
    net_addr[0][octet] = str(network)
    print("-" * 88)
    marked = ''
    start = int(ip_calc(net_addr[0], 'first_ip', 'dec')[0][-1])
    end = int(ip_calc(net_addr[0], 'last_ip', 'dec')[0][-1])
    if start < int(ip_dec[-1]) < end:
        marked = "*"
    print(f"{'.'.join(net_addr[0]) : <17} | {ip_calc(net_addr[0], 'first_ip', 'dec')[1] : ^15}-{ip_calc(net_addr[0], 'last_ip', 'dec')[1] : ^17} | {ip_calc(net_addr[0], 'broad_addr', 'dec')[1]}  {marked}")
    network += bin_table[cidr % 8 - 1]
