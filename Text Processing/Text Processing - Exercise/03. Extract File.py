path = input().split("\\")

filename = path[-1].split(".")
name, ext = filename

print(f"File name: {name}")
print(f"File extension: {ext}")