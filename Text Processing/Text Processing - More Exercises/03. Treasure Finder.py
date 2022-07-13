key = list(map(int, input().split()))

command = input()

while command != 'find':
    index = 0
    decrypted = ''
    string = command
    for char in string:
        decrypted += chr(ord(char) - key[index])
        if index == len(key) - 1:
            index = 0
        else:
            index += 1

    id1 = decrypted.index("&")
    id2 = decrypted.rindex("&")
    treasure = decrypted[id1 + 1:id2]
    coord = decrypted[decrypted.index("<") + 1:decrypted.index(">")]

    print(f"Found {treasure} at {coord}")

    command = input()
