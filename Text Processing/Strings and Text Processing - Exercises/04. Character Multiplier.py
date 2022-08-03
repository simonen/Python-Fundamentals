text = input().split()

string1, string2 = text
short = string1
long = string2

if len(string2) < len(string1):
    long = string1
    short = string2

total = sum([ord(x) for x in long[len(short)::]])

for i in range(len(short)):
    total += ord(short[i]) * ord(long[i])

print(total)
