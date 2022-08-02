numbers = input().split()

evens = [int(x) for x in numbers if int(x) % 2 == 0]
average = sum(evens) / len(evens)

for i in range(len(evens)):
    if evens[i] > average:
        evens[i] = str(evens[i] + 1)
    elif int(evens[i]) <= average:
        evens[i] = str(evens[i] - 1)

print(" ".join(evens))
