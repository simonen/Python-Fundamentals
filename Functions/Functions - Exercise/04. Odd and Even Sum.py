number = input()


def sum_even_odd(a):
    sum_even = 0
    sum_odd = 0
    for i in a:
        if int(i) % 2 == 0:
            sum_even += int(i)
        else:
            sum_odd += int(i)
    return sum_odd, sum_even


odds = sum_even_odd(number)[0]
evens = sum_even_odd(number)[1]

print(f"Odd sum = {odds}, Even sum = {evens}")
