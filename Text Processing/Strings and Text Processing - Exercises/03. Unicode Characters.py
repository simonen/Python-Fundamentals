res = ''.join(r'\u{:04x}'.format(ord(char)) for char in list(input()))

print(res)