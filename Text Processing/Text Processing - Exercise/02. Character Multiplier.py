strings = input().split()

str1, str2 = strings
longer = str1
shorter = str2

if len(str1) < len(str2):
    longer = str2
    shorter = str1

total = sum([(ord(x)) for x in longer[len(shorter):]])      #remaining characters, 0 if equal

for i in range(len(shorter)):
    total += ord(str1[i]) * ord(str2[i])

print(total)
