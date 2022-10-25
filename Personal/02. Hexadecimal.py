def hex_dec(hex_num_f):
    book = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    dec = 0
    index = len(hex_num_f) - 1
    for n in hex_num_f:
        if n in book:
            dec += book[n] * 16 ** index
        else:
            dec += int(n) * 16 ** index
        index -= 1
    return dec


def dec_bin(dec_num_f):
    bin_list = []
    num = int(dec_num_f)
    while num > 0:
        bin_list.append(str(num % 2))
        num //= 2
    if len(bin_list) == 0:
        return "0"
    return bin_list[::-1]


print("### MAC Address-To-Binary Converter by don_simone ###")
print("### Type 'end' to exit the program ###")
# ex E8-11-32-4E-07-DB
mac_hex = input("Enter MAC address: ")

while mac_hex != "end":
    mac_binary = []
    hex = mac_hex.split("-")
    for i in hex:
        try:
            bin_num = "".join(dec_bin(hex_dec(i)))
            mac_binary.append(f"{bin_num:0>8}")
        except ValueError as ve:
            print(ve)
    print("-".join(mac_binary))
    mac_hex = input("Enter MAC address: ")

# book = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
# number = int(input())
# hexan = ""
# rem1 = ''
# while number > 0:
#     rem = number % 16
#     number = number // 16
#     if rem in book:
#         rem = book[rem]
#     hexan += str(rem)

