def caesar_encrypt(lower_f, upper_f, cipher_lower_f, cipher_upper_f, string_f):
    encrypted = ''
    for i in string_f:
        if i in lower_f:
            encrypted += cipher_lower_f[lower_f.index(i)]
        elif i in upper_f:
            encrypted += cipher_upper_f[upper_f.index(i)]
        else:
            encrypted += i
    return encrypted


def caesar_decrypt(lower_f, upper_f, cipher_lower_f, cipher_upper_f, string_f):
    decrypted = ''
    for j in string_f:
        if j in cipher_lower_f:
            decrypted += lower_f[cipher_lower_f.index(j)]
        elif j in upper_f:
            decrypted += upper_f[cipher_upper_f.index(j)]
        else:
            decrypted += j

    return decrypted


lower = [chr(x) for x in range(97, 123)]
upper = [chr(x) for x in range(65, 91)]
command = input("<encrypt/decrypt> <shift> ")
while True:
    command = command.split()
    shift = int(command[1])
    cipher_lower = [lower[(lower.index(x) + shift) % len(lower)] for x in lower]
    cipher_upper = [upper[(upper.index(x) + shift) % len(upper)] for x in upper]
    if command[0] == "encrypt":
        string = input("Enter a string to encrypt: ")
        print("Encrypted text:", caesar_encrypt(lower, upper, cipher_lower, cipher_upper, string))
    elif command[0] == "decrypt":
        string = input("Enter a string to decrypt: ")
        print("Deciphered text:", caesar_decrypt(lower, upper, cipher_lower, cipher_upper, string))

    command = input("<encrypt/decrypt> <shift> ")