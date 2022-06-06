n = int(input())

all_numbers = []
new_list = []

for _ in range(n):
    number = int(input())
    all_numbers.append(number)

command = input()

for num in all_numbers:
    filter_command = (
        (command == "even" and num % 2 == 0) or
        (command == "odd" and num % 2 != 0) or
        (command == "positive" and num >= 0) or
        (command == "negative" and num < 0)
    )
    if filter_command:
        new_list.append(num)

print(new_list)