string = list(map(int, input().split(" ")))

removed_sum = 0
removed_number = 0
while len(string) > 0:
    number = int(input())
    if number < 0:
        removed_number = string[0]
        string[0] = string[-1]
    elif number > len(string) - 1:
        removed_number = string[-1]
        string[-1] = string[0]
    else:
        removed_number = string.pop(number)
    removed_sum += removed_number
    for i, d in enumerate(string):
        if d <= removed_number:
            string[i] += removed_number
        else:
            string[i] -= removed_number

print(removed_sum)

