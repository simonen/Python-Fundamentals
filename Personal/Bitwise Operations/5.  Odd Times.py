number = input().split(" ")

print(number)

for i in number:
    if number.count(i) % 2 != 0:
        print(i)
        break