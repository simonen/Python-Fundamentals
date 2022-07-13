text = input().split()

morse = {'A': '.-', '  B': '-...',
         'C': '-.-.', 'D': '-..',  'E': '.',
         'F': '..-.', 'G': '--.',  'H': '....',
         'I': '..',   'J': '.---', 'K': '-.-',
         'L': '.-..', 'M': '--',   'N': '-.',
         'O': '---',  'P': '.--.', 'Q': '--.-',
         'R': '.-.',  'S': '...',  'T': '-',
         'U': '..-',  'V': '...-', 'W': '.--',
         'X': '-..-', 'Y': '-.--', 'Z': '--..'}

key_list = list(morse.keys())
val_list = list(morse.values())
message = ''

for i in text:
    if i != "|":
        position = val_list.index(i)
        message += key_list[position]
    else:
        message += " "

print(message)