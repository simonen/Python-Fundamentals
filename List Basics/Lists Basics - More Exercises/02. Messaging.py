numbers = input()
string = input()

a = list(string)
A = numbers.split(" ")
B = []
C = []
string_len = len(string)

for number in range(len(A)): # Convert the numbers to indices not exceeding the len(string)
    suma = 0
    for digit in A[number]:
        suma += int(digit)
    if suma > string_len:
        suma %= string_len
    B.append(suma)

for i in B:
    new_string = a
    letter = new_string.pop(i)
    C.append(letter)

C = "".join(C)
print(C)