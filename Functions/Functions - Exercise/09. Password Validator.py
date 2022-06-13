string = list(input())

str_to_ascii = list(map(ord, string))
digits = list(range(48, 58))
valid_letters = list(range(65, 91)) + list(range(97, 123)) + digits
pass_char = True
pass_len = False
digit_count = 0

for letter in str_to_ascii:
    if int(letter) not in valid_letters:
        pass_char = False
        break

if 6 <= len(str_to_ascii) <= 10:
    pass_len = True

for char in str_to_ascii:
    if int(char) in digits:
        digit_count += 1

if not pass_len:
    print("Password must be between 6 and 10 characters")
if not pass_char:
    print("Password must consist only of letters and digits")
if digit_count < 2:
    print(f"Password must have at least 2 digits")
if digit_count >= 2 and pass_len and pass_char:
    print("Password is valid")
