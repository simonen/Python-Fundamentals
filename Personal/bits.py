# Splits a string into n equal parts
group_len = 8


def str_splitter(string_f, group_len_f):
    grouped = []
    for i in range(0, len(string_f), group_len_f):
        chunk = string_f[i:i + group_len_f]
        grouped.append(chunk)

    return grouped


ip_dec = input("Enter IP address: ").split(".")
cidr = int(input("Mask bits: "))

host_bits = 32 - cidr
mask_dec = [0, 0, 0, 0]
times = cidr // 8
remainder = cidr % 8
for i in range(0, times):
    mask_dec[i] = 255
    if i + 1 < len(mask_dec):
        mask_dec[i + 1] = f"{(256 - 2 ** (8 - remainder))}"

print(ip_dec, "  ==>  ip address")
print(mask_dec, "  ==>  subnet mask")
ip_bin = list(map(lambda x: f"{int(x):08b}", ip_dec))
mask_bin = list(map(lambda x: f"{int(x):08b}", mask_dec))
print(ip_bin, "  ==>  ip address")
print(mask_bin, "  ==>  mask")
print("".join(ip_bin), "  ==>  ip address")
print("".join(mask_bin), "  ==>  mask")

# Isolate the network portion
masked_addr = "".join(ip_bin)[:cidr]
print("network address")
net_address_bin = f"{masked_addr:0<32}"
print("=> ", net_address_bin)
net_addr_oct = str_splitter(net_address_bin, group_len)
print("=> ", net_addr_oct)
net_addr_dec = [f"{int(x, 2)}" for x in net_addr_oct]
print("=> ", net_addr_dec)
# Broadcast address
print("Broadcast address")
broadcast_bin = f"{masked_addr:1<32}"
print("=> ", broadcast_bin)
broadcast_bin_oct = str_splitter(broadcast_bin, group_len)
print("=> ", broadcast_bin_oct)
broadcast_dec = [f"{int(x, 2)}" for x in broadcast_bin_oct]
print("=> ", broadcast_dec)
print("First usable IP address")
first_ip_bin = net_address_bin[:-1] + "1"
print("=> ", first_ip_bin)
first_ip_oct = str_splitter(str(first_ip_bin), group_len)
print("=> ", first_ip_oct)
first_ip_dec = [f"{int(x, 2)}" for x in first_ip_oct]
print("=> ", first_ip_dec)
print("Last usable IP address")
last_ip_bin = broadcast_bin[:-1] + "0"
print("=> ", last_ip_bin)
last_ip_oct = str_splitter(str(last_ip_bin), group_len)
print("=> ", last_ip_oct)
last_ip_dec = [f"{int(x, 2)}" for x in last_ip_oct]
print("=> ", last_ip_dec)
print("Total number of hosts")
total_addr = 2 ** host_bits
print("=> ", total_addr)
print("Usable IP hosts addresses")
usable_ips = 2 ** host_bits - 2
print("=> ", usable_ips)
