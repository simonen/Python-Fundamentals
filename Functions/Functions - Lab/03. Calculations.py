def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculation(operator, first_num, second_num):
    if operator == "add":
        return add(first_num, second_num)
    elif operator == "subtract":
        return subtract(first_num, second_num)
    elif operator == "multiply":
        return multiply(first_num, second_num)
    elif operator == "divide":
        return divide(first_num, second_num)


operators = input()
first_number = int(input())
second_number = int(input())
result = calculation(operators, first_number, second_number)
print(result)