number_string = input()
beggar = int(input())

number_list = number_string.split(", ")
beggars = []

for index, string in enumerate(number_list):
    number_list[index] = int(string)

for i in range(beggar):
    beggars.append(sum(number_list[i::beggar]))

print(beggars)
