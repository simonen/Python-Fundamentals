import re

n = int(input())

for _ in range(n):
    string = input()
    match = re.findall(r"^(\$|\%)([A-Z][a-z]{2,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|($|\s)", string)
    if len(match) == 0:
        print("Valid message not found!")
    else:
        a = [x for x in match[0]]
        print(f"{a[1]}: {chr(int(a[2]))}{chr(int(a[3]))}{chr(int(a[4]))}")

#####
# Sonia Haralambieva
# import re
# num = int(input())
# pattern = r'^(\%|\$)([A-Z][a-z]{2,})\1:\s\[(\d+\]\|\[\d+\]\|\[\d+)\]\|$'
#
# for _ in range(num):
#     current_command = input()
#     matches = re.match(pattern, current_command)
#
#     if not matches:
#         print("Valid message not found!")
#     else:
#         list_of_numbers = re.findall("\d+", matches.group())
#         ascii_list_of_numbers = [chr(int(num)) for num in list_of_numbers]
#
#         current_decrypted_message = "".join(ascii_list_of_numbers)
#         tag = matches[2]
#
#         print(f"{tag}: {current_decrypted_message}")

