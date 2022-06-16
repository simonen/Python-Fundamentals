names = input().split(", ")

sorted_list = sorted(list(names), key=lambda x: (-len(x), x))

print(sorted_list)
