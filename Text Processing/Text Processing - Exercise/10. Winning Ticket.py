def longest(string):
    side_a = ''
    max_a = ''
    previous = ''
    for t in string:
        if t in valid and t == previous:
            side_a += t
            if len(side_a) >= len(max_a):
                max_a = side_a
        else:
            side_a = t
        previous = t
    return max_a


tickets = input().replace(" ", "").split(",")
valid = ['@', '#', '$', '^']

for ticket in tickets:

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    max1 = longest(ticket[:10])
    max2 = longest(ticket[10::])
    least = min(len(max1), len(max2))

    if 6 <= least < 10 and max1[0] == max2[0]:
        print(f'ticket "{ticket}" - {least}{max1[0]}')
    elif least == 10:
        print(f'ticket "{ticket}" - 10{max1[0]} Jackpot!')
    else:
        print(f'ticket "{ticket}" - no match')
