happiness = list(map(int, input().split(" ")))
factor = int(input())


def multiply(x):
    return x * factor


factor1 = list(map(multiply, happiness))
average = sum(factor1) / len(happiness)
print(factor1)

faxtor = map(lambda a: a if a >= average in factor1 else "no", range(len(factor1)))
filtered = filter(lambda b: b != "no", faxtor)
print(list(filtered))
# factored = [x * factor for x in happiness]
#

# total = len(happiness)
# happy = 0
#
# for i in factored:
#     if i >= average:
#         happy += 1
#
# if happy >= total // 2:
#     print(f"Score: {happy}/{total}. Employees are happy!")
# else:
#     print(f"Score: {happy}/{total}. Employees are not happy!")
