numbers = list(map(int, input().split()))
command = input()


def first_last(even_odd_f, first_or_last):
    if first_or_last == "first":
        return even_odd_f[:index]
    elif first_or_last == "last":
        return even_odd_f[-index:]


def min_max_f(even_odd_f, min_maxa):
    if min_maxa == "min":
        return min(even_odd_f)
    elif min_maxa == "max":
        return max(even_odd_f)


def exchange_f(nums, split):
    if 0 <= split <= len(nums) - 1:
        left_side = nums[0:split + 1]
        right_side = nums[split + 1::]
        nums = right_side + left_side
        return nums
    else:
        return "Invalid index"


def even_odd(nums, even_or_odd):
    evens = [x for x in nums if x % 2 == 0]
    odds = [y for y in nums if y % 2 != 0]
    if even_or_odd == "even":
        return evens
    elif even_or_odd == "odd":
        return odds


while command != "end":
    command = command.split()
    action = command[0]
    if command[1].isdigit():
        index = int(command[1])

    if action == "min" or action == "max":
        odd_even = command[1]
        if len(even_odd(numbers, odd_even)) == 0:
            print("No matches")
            command = input()
            continue
        else:
            min_max = min_max_f(even_odd(numbers, odd_even), action)
            num_type = len(numbers) - numbers[::-1].index(min_max) - 1
        print(num_type)

    elif action == "exchange":
        if 0 <= index <= len(numbers) - 1:
            numbers = exchange_f(numbers, index)
        else:
            print("Invalid index")

    elif action == "first" or action == "last":
        odd_even = command[2]
        if not 0 < index <= len(numbers):
            print("Invalid count")
        else:
            print(first_last(even_odd(numbers, odd_even), action))

    command = input()

print(numbers)
