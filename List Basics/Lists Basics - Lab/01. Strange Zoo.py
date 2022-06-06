tail = input()
body = input()
head = input()

#animal = [head, body, tail]
#print(animal)

animal = [tail, body, head]
animal[0], animal[2] = animal[2], animal[0]

print(animal)