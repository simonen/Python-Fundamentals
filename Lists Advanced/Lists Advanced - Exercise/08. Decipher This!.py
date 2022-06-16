code = input().split(" ")

for word in code:
    number = ''
    alpha = []
    for letter in word:
        if letter.isdigit():
            number += letter
        else:
            alpha += letter
    alpha[0], alpha[-1] = alpha[-1], alpha[0]
    new_string = ''.join(alpha)
    decoded_word = chr(int(number)) + new_string
    print(decoded_word, end=" ")