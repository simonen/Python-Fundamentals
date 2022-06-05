divisor = int(input())
boundary = int(input())

max_number = - 100000
for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > max_number:
            max_number = i
print(max_number)