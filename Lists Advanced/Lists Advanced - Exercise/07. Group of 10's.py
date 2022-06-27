from math import ceil

numbers = list(map(int, input().split(", ")))
max_group = ceil(max(numbers) / 10) * 10

for group in range(10, max_group + 10, 10):
    filtered = [num for num in numbers if num <= group]
    numbers = [num for num in numbers if num > group]
    print(f"Group of {group}'s: {filtered}")


