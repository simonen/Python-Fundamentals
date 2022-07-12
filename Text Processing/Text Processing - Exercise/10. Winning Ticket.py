tickets = input().split(", ")
valids = ['@', '#', '$', '^']

previous = ""
side_a = '@'
side_b = '@'
special = ''
count = 0

for ticket in tickets:
    if len(ticket) != 20:
        print("Invalid ticket")
        continue
    for t in ticket[0:len(ticket) // 2 + 1]:
        if t in valids and t == previous:
            special = t
            side_a += t

        previous = t
    for t in ticket[len(ticket) // 2::]:
        if t in valids and t == previous:
            side_b += t
        previous = t
    match = len(side_a)
    if len(side_a) > len(side_b):
        match = len(side_b)

    if 6 <= match < 10:
        print(f"ticket {ticket} - {match}{special}")
    elif match == 10:
        print(f"ticket {ticket} - 10{special} Jackpot!")
    else:
        print(f"ticket {ticket} - no match")