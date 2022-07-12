tickets = input().replace(" ", "").split(",")

valid = ['@', '#', '$', '^']

for ticket in tickets:
    side_a = ''
    side_b = ''
    max_a = ''
    max_b = ''
    previous = ''
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    for t in ticket[0:10]:
        if t in valid and t == previous:
            side_a += t
            if len(side_a) >= len(max_a):
                max_a = side_a
        else:
            side_a = t
        previous = t

    previous = ''
    for t in ticket[10::]:
        if t in valid and t == previous:
            side_b += t
            if len(side_b) >= len(max_b):
                max_b = side_b
        else:
            side_b = t
        previous = t

    least = min(len(max_a), len(max_b))

    if 6 <= least < 10 and max_a[0] == max_b[0]:
        print(f'ticket "{ticket}" - {least}{max_a[0]}')
    elif least == 10:
        print(f'ticket "{ticket}" - 10{max_a[0]} Jackpot!')
    else:
        print(f'ticket "{ticket}" - no match')
