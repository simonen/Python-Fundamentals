def data_type(dtype):
    num = ''
    if dtype == "int":
        num = int(input()) * 2
    elif dtype == "real":
        num = float(input()) * 1.5
    elif dtype == "string":
        num = "$" + input() + "$"
    return num


result = data_type(input())
print(result)
