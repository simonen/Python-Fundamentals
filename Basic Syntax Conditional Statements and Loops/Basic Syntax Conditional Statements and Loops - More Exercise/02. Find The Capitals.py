import string

word = input()
upper = string.ascii_uppercase

upper_index = []
for index, letter in enumerate(word):
    if letter in upper:
        upper_index.append(index)
print(upper_index)