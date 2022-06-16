vowels = ["a", "e", "o", "i", "u", "A", "E", "U", "O", "I"]

string = input()

new_string = "".join(x for x in string if x not in vowels)

print(new_string)