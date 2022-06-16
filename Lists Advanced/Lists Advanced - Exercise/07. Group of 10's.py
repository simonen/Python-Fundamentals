numbers = list(map(int, input().split(", ")))

num_max = max(numbers)
max_group = 0
### Define the group boundary
if num_max % 10 > 0:
    max_group = (num_max // 10 + 1) * 10
else:
    max_group = num_max
A = []
for group in range(10, max_group + 10, 10):
    for i, number in enumerate(numbers):
        if group - 10 <= number <= group:
            A.append(number)
    for num in A:
        numbers.remove(num)
    print(f"Group of {group}'s: {A}")
    A = []
