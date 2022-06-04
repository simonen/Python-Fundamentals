n = int(input())

sum = 0
for i in range(1, n + 1):
    char = input()
    sum += ord(char)

print(f"The sum equals: {sum}")