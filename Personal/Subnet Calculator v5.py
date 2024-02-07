import pandas as pd


def str_split(string: str) -> list:
    return [string[j: j + 8] for j in range(0, 32, 8)]


def ip_class(ip_bin_f: list) -> str:
    class_map = {
        '0': 'A',
        '10': "B",
        '110': 'C',
        '1110': 'D',
        "11110": "E"
        }

    for prefix, addr_class in class_map.items():
        if "".join(ip_bin_f).startswith(prefix):
            return addr_class
    return ''


def addr_scope(ip_bin_f: list) -> str:
    private_addr = ["00001010", "1010101100010000", "1010110000011111", "1100000010101000"]
    for prefix in private_addr:
        if "".join(ip_bin_f).startswith(prefix):
            return "private"
    return "public"


def first_usable(addr: list) -> str:
    return "".join(addr)[:-1] + "1"


def last_usable(addr: list) -> str:
    return "".join(addr)[:-1] + "0"


def net(addr: list, mazk) -> str:
    return f'{("".join(addr)[:mazk]):0<32}'


def broad(addr: list, mazk) -> str:
    return f'{("".join(addr)[:mazk]):1<32}'


def decimal(addr: list):
    return list(map(lambda x: int(x, 2), addr))


def valid_ip():
    while True:
        try:
            ip_addr = input("Enter IPv4 Address: ").split(".")
            if all(x in range(0, 256) for x in map(int, ip_addr)) and (len(ip_addr) == 4):
                return ip_addr
            print("invalid ip address!")
        except ValueError:
            print("ip address should be in dotted decimal format")


def valid_mask():
    while True:
        try:
            ip_mask = int(input("Enter a mask [1 - 30]: "))
            if ip_mask in range(1, 31):
                return ip_mask
        except ValueError:
            print('invalid mask')


def addr_type(ip_addr: list) -> str:
    dic = {
        net(ip_addr, mask): 'network', broad(ip_addr, mask): 'broadcast'
    }
    return dic.get(''.join(ip_addr), 'host')


chars = 90

ip = valid_ip()
mask = valid_mask()
octet = mask // 8
norm_mask = octet * 8
all_networks = 2 ** (mask % 8)
step = 256 // all_networks
total_hosts = 2 ** (32 - mask)
usable_hosts = total_hosts - 2

ip_dec = '.'.join(ip)
bin_ip = [f"{x:08b}" for x in list(map(int, ip))]
subnet_mask_bin = str_split(f"{mask * '1':0<32}")
subnet_mask_dec = decimal(subnet_mask_bin)
wildcard_bin = str_split(f"{mask * '0':1<32}")
wildcard_dec = decimal(wildcard_bin)

scope = addr_scope(bin_ip)
class_ip = ip_class(bin_ip)
hex_id = "0x" + "".join([f"{x:02x}" for x in map(int, ip)])
arpa = f'{".".join([x for x in ip[::-1]])}.in-addr.arpa.'
ipv4_mapped = f"::ffff:{hex_id[:4]}.{hex_id[4:8]}"

print("=" * chars)
print(f'all {all_networks} possible /{mask} networks for {".".join(ip[:octet]) + (4 - octet) * ".*"}')
print("=" * chars)

data = []
current_addr = [[ip, bin_ip], [subnet_mask_dec, subnet_mask_bin]]

for i in range(0, 256, step):
    mark = ''
    net_addr_bin = str_split(net(bin_ip, norm_mask))
    net_addr_bin[octet] = f"{i:08b}"
    first_bin = str_split(first_usable(net_addr_bin))
    broad_bin = str_split(broad(net_addr_bin, mask))
    last_bin = str_split(last_usable(broad_bin))

    if decimal(net_addr_bin)[octet] <= int(ip[octet]) <= decimal(broad_bin)[octet]:
        mark = "*"
        current_addr.extend([[decimal(net_addr_bin), net_addr_bin], [decimal(broad_bin), broad_bin],
                             [decimal(first_bin), first_bin], [decimal(last_bin), last_bin],
                             [wildcard_dec, wildcard_bin]])

    data.append([decimal(net_addr_bin), decimal(first_bin), "-", decimal(last_bin), decimal(broad_bin), mark])

df = pd.DataFrame(data, columns=['network address', 'first usable host', '',
                                 'last usable host', 'broadcast address', ''])

for j in ['network address', 'first usable host', 'last usable host', 'broadcast address']:
    df[j] = df[j].apply(lambda lst: ".".join(str(x) for x in lst))

pd.options.display.max_colwidth = None  # To display the full content of each cell

print(df.to_string(index=False, header=True))
print("=" * chars)
print(f'{".".join(ip)} /{mask} is a {addr_type(bin_ip)} address')
print("=" * chars)

df = pd.DataFrame(current_addr, index=['ip address', 'subnet mask', 'network address', 'broadcast address',
                                       'first usable', 'last usable', 'wildcard mask'],
                  columns=['decimal', 'binary'])

df['decimal'] = df['decimal'].apply(lambda lst: ".".join(str(x) for x in lst))
df['binary'] = df['binary'].apply(lambda lst: ".".join(lst))

print(df)
print("=" * chars)

df = pd.DataFrame([f"{total_hosts:,}", f"{usable_hosts:,}", scope, class_ip, hex_id, arpa, ipv4_mapped],
                  index=['total hosts          ', 'usable hosts', 'scope',
                         'ip class', 'hex id', 'in-addr.arpa', 'IPv4 mapped'],
                  columns=[""])
print(df)
