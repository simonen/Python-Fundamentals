n = int(input())
word = input()

my_list = []

for _ in range(n):
    my_list.append(input())

print(my_list)
new_list = []

for index, sentence in enumerate(my_list):
    if word in sentence:
        new_list.append(sentence)

print(new_list)
