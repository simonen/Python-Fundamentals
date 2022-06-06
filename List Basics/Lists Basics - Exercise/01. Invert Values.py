num_string = input()
numbers = []

my_list = num_string.split(" ")
for num in my_list:
    int_number = int(num) * -1
    numbers.append(int_number)

print(numbers)
