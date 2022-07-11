path = input().split("\\")

filename = path[-1].split(".")
name = filename[0]
ext = filename[1]

print(f"File name: {name}")
print(f"File extension: {ext}")