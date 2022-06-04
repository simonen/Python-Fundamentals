number = int(input())
flag = False

for i in range(2, number):
    if (number % i) == 0:
        flag = True
        break
if flag:
    print("False")
else:
    print("True")