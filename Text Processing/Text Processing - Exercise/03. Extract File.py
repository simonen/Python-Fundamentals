path = input().split("\\")

name, ext = path[-1].split(".")

print(f"File name: {name}")
print(f"File extension: {ext}")