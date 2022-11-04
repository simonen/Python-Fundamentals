def str_splitter(string_f):
    grouped = []
    for i in range(0, len(string_f), 8):
        chunk = string_f[i:i + 8]
        grouped.append(chunk)

    return grouped


def ip_calc(ip_f, addr_type):
    ip_f = ip_f.split(".")
    ip_bin = [f"{x:08b}" for x in map(int, ip_f)]
    masked_addr = "".join(ip_bin)[:cidr]
    addr_bin = ''
    if addr_type == "net_addr":
        addr_bin = f"{''.join(ip_bin[:octet]):0<32}"
    elif addr_type == "broad_addr":
        addr_bin = f"{masked_addr:1<32}"
    elif addr_type == "first_ip":
        addr_bin = f"{masked_addr:0<32}"[:-1] + "1"
    elif addr_type == "last_ip":
        addr_bin = f"{masked_addr:1<32}"[:-1] + "0"

    addr_sep = str_splitter(addr_bin)
    addr_dec = [f"{int(x, 2)}" for x in addr_sep]

    return ".".join(addr_dec)


ip = "192.168.44.56"
cidr = 24
host_bits = 32 - cidr
octet = cidr // 8
borrowed_bits = cidr % 8
subnets_count = 2 ** borrowed_bits
total_addr = 2 ** host_bits
usable_ips = total_addr - 2
print(f"{ip : <15} | {'ip address' : <10}")
netmask_bin = f"{('1' * cidr):0<32}"
netmask_oct = str_splitter(netmask_bin)
print(".".join([f"{int(x, 2)}" for x in netmask_oct]), 'subnet mask')
print(".".join(netmask_oct), "subnet mask")
print(f"{ip_calc(ip, 'net_addr') : <15} | {'network address' : <10}")
print(f"{ip_calc(ip, 'broad_addr') : <15} | {'broadcast address' : <10}")
print(f"{ip_calc(ip, 'first_ip') : <15} | {'first usable host' : <10}")
print(f"{ip_calc(ip, 'last_ip') : <15} | {'last usable host' : <10}")
print()
print("Total number of hosts")
print("=> ", total_addr)
print("Usable IP hosts addresses")
print("=> ", usable_ips)
print()
bin_table = [128, 64, 32, 16, 8, 4, 2, 1]
network = 0
base_network = ip_calc(ip, 'net_addr').split(".")
print(f"All of the {subnets_count} possible /{cidr} networks for {'.'.join(base_network)}")
print(f"{'[Network Address]'} | {'[First Usable Address]'} | {'[Last Usable Address]'} | {'[Broadcast Address]'}")

for _ in range(0, subnets_count):
    base_network[octet] = str(network) # !!!!!
    base_network = ".".join(base_network)
    print(f"{base_network : <17} | {ip_calc(base_network, 'first_ip') : <22} | {ip_calc(base_network, 'last_ip') : <21} | {ip_calc(base_network, 'broad_addr') : <14}")
    network += bin_table[borrowed_bits - 1]
    base_network = base_network.split(".")
