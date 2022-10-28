number = int(input())

times = number // 8
remainder = number % 8

mask = [0, 0, 0, 0]

for i in range(0, times):
    mask[i] = 8
    mask[i + 1] = remainder

print(mask)

print(times, remainder)