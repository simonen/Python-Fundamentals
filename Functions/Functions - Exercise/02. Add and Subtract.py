def sum_numbers(a, b):
    sum_num = a + b
    return sum_num


def subtract(a, b):
    diff = a - b
    return diff


def add_and_subtract():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    sum_numb = sum_numbers(num1, num2)
    diff_numb = subtract(sum_numb, num3)
    return diff_numb


print(add_and_subtract())
