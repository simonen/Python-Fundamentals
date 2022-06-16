current_version = "".join(input().split("."))

next_ver_num = int(current_version) + 1
next_ver_str = [str(x) for x in str(next_ver_num)]
next_ver = ".".join(next_ver_str)

print(next_ver)

