def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 8):
        chunk = string_f[i:i + 8]
        grouped.append(chunk)

    return grouped


def ip_calc(ip_f, addr_type):
    ip_f = ip_f.split(".")
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

    return ".".join(addr_dec)


def str_split2(string_ff, index_f):
    if string_ff[index_f - 1] == ".":
        string_ff = string_ff[:index_f] + '' + string_ff[index_f::]
    else:
        string_ff = string_ff[:index_f] + ' ' + string_ff[index_f::]
    return string_ff


def cidr_dotted(cidr_f, bin_dec_f):
    netmask_bin_f = f"{('1' * cidr_f):0<32}"
    netmask_dotted = str_splitter(netmask_bin_f)
    netmask_bin_str = ".".join(str_splitter(netmask_bin_f))
    netmask_dec_str = ".".join([f"{int(x, 2)}" for x in netmask_dotted])
    if bin_dec_f == "bin":
        return netmask_bin_str
    elif bin_dec_f == "dec":
        return netmask_dec_str


ip_dec = "192.168.44.56"
cidr = 25
host_bits = 32 - cidr
octet = cidr // 8
borrowed_bits = cidr % 8
subnets_count = 2 ** borrowed_bits
total_addr = 2 ** host_bits
usable_ips = total_addr - 2
netmask_dec = cidr_dotted(cidr, 'dec')
netmask_bin = cidr_dotted(cidr, "bin")
index = netmask_bin.find("0")
print("-" * 33)
print(f"{'ip address' : <17} | {ip_dec}")
print(f"{'subnet mask' : <17} | {netmask_dec}")
print(f"{'cidr notation' : <17} | {ip_dec} /{cidr}")
ip_list = ip_dec.split(".")
ip_bin_list = [f"{x:08b}" for x in map(int, ip_list)]
ip_bin = '.'.join(ip_bin_list)
print(str_split2(ip_bin, index))
print(str_split2(netmask_bin, index))
print("-" * 33)
print(f"{'network address' : <17} | {ip_calc(ip_dec, 'net_addr') : <10}")
print(f"{'broadcast address' : <17} | {ip_calc(ip_dec, 'broad_addr') : <10}")
print(f"{'first usable host' : <17} | {ip_calc(ip_dec, 'first_ip') : <10}")
print(f"{'last usable host' : <17} | {ip_calc(ip_dec, 'last_ip') : <10}")
print("-" * 33)
print(f"Total number of addresses: {total_addr : >5}")
print(f"Usable hosts addresses: {usable_ips : >8}")
print("-" * 33)
bin_table = [128, 64, 32, 16, 8, 4, 2, 1]
network = 0
base_network = ip_calc(ip_dec, 'net_addr').split(".")
print(f"All of the {subnets_count} possible /{cidr} networks for {'.'.join(base_network)}")
print(f"{'Network Address' : <17} | {'First Usable Address' : ^15} | {'Last Usable Address'} | {'Broadcast Address'}")

for _ in range(0, subnets_count):
    base_network[octet] = str(network) # !!!!!
    base_network = ".".join(base_network)
    print(f"{base_network : <17} | {ip_calc(base_network, 'first_ip') : <22} |"
          f" {ip_calc(base_network, 'last_ip') : <21} | {ip_calc(base_network, 'broad_addr') : <14}")
    network += bin_table[borrowed_bits - 1]
    base_network = base_network.split(".")

