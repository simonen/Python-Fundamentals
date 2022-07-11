word = input()

code = ''

for i in word:
    code += chr(ord(i) + 3)

print(code)