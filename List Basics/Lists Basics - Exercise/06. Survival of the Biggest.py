number_string = input()
count = int(input())

A = number_string.split(" ")

for i in range(len(A)):
    A[i] = int(A[i])

for _ in range(count):
    A.remove(min(A))

B = ", ".join(map(str, A))

print(B)
