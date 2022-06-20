from math import ceil

numbers = list(map(int, input().split(", ")))
max_group = ceil(max(numbers) / 10) * 10

for group in range(10, max_group + 10, 10):
    A = []
    for number in numbers:
        if group - 10 < number <= group:
            A.append(number)

    print(f"Group of {group}'s: {A}")


