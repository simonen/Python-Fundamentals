def ip_calc(ip_f, addr_type, bin_dec_f):
    # ip_f = ip_f.split(".")
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


ip_dec = "192.168.63.191".split(".")
cidr = 27
octet = cidr // 8

netmask_dec = cidr_dotted(cidr, 'dec')
netmask_bin = cidr_dotted(cidr, 'bin')
index = netmask_bin.find("0")
ip_bin = ".".join([f"{x:08b}" for x in map(int, ip_dec)])
net_addr = ip_calc(ip_dec, 'net_addr', 'dec')
net_addr_bin = ip_calc(ip_dec, 'net_addr', 'bin')
broad_addr = ip_calc(ip_dec, 'broad_addr', 'dec')
broad_addr_bin = ip_calc(ip_dec, 'broad_addr', 'bin')
first_host = ip_calc(ip_dec, 'first_ip', 'dec')
first_host_bin = ip_calc(ip_dec, 'first_ip', 'bin')
dashes = 85
print(f"{'### IPv4 Subnet Calculator v0.1 by don_simone ###': <30}")
print("-" * dashes)
print(f"{'.'.join(ip_dec)} /{cidr}")
print("-" * dashes)
address = 'host address'
if '.'.join(ip_dec) == net_addr[1]:
    address = 'network address'
elif '.'.join(ip_dec) == broad_addr[1]:
    address = 'broadcast address'
print(f"{address : <21} {'.'.join(ip_dec) : <21} {str_split2(ip_bin, index)}")
print(f"{'subnet mask' : <21} {netmask_dec : <21} {str_split2(netmask_bin, index)}")
# print(f"{'cidr notation' : <21} /{cidr} ")
print(f"{'network address' : <21} {net_addr[1] : <21} {net_addr_bin[1]}")
print(f"{'broadcast address' : <21} {broad_addr[1] : <21} {broad_addr_bin[1]}")
print(f"{'first host' : <21} {first_host[1] : <21} {first_host_bin[1]}")
last_host = ip_calc(ip_dec, 'last_ip', 'dec')
last_host_bin = ip_calc(ip_dec, 'last_ip', 'bin')
print(f"{'last host' : <21} {last_host[1] : <21} {last_host_bin[1]}")
subnet_count = 2 ** (cidr % 8)
print("-" * dashes)
host_bits = 32 - cidr
total_addr = 2 ** host_bits
usable_ips = total_addr - 2
print(f"{'total addresses' : <21} {total_addr}  \n"
      f"{'host addresses' : <21} {usable_ips}")
print("-" * dashes)
print(f"All of the {subnet_count} possible /{cidr} networks for {'.'.join(ip_dec[:octet]) + '.*' * (4 - octet)}")
print()
print(f"{'network address' : <18} | {'range of usable host addresses' : ^35} | {'broadcast address': <18}")
network = 0
bin_table = [128, 64, 32, 16, 8, 4, 2, 1]
for _ in range(subnet_count):
    net_addr[0][octet] = str(network)
    print("-" * dashes)
    marked = ''
    start = int(ip_calc(net_addr[0], 'first_ip', 'dec')[0][octet])
    end = int(ip_calc(net_addr[0], 'last_ip', 'dec')[0][octet])
    if start < int(ip_dec[octet]) < end:
        marked = "*"
    print(f"{'.'.join(net_addr[0]) : <18} | {ip_calc(net_addr[0], 'first_ip', 'dec')[1]:^16} - {ip_calc(net_addr[0], 'last_ip', 'dec')[1] : ^16} | {ip_calc(net_addr[0], 'broad_addr', 'dec')[1]} {marked}")
    network += bin_table[cidr % 8 - 1]
