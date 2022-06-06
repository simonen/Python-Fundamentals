factor = int(input())
count = int(input())

num = 0
numbers = []

for i in range(count):
    num += factor
    numbers.append(num)

print(numbers)
