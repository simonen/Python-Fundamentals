numbers = input()
A = numbers.split()
D = A
len_D = len(D)
A_even = []
A_odd = []
for i in D:
    if int(i) % 2 == 0:
        A_even.append(int(i))
    else:
        A_odd.append(int(i))
max_even = 0
max_odd = 0
min_even = 0
min_odd = 0
if len(A_odd) > 0:
    max_odd = max(A_odd)
    min_odd = min(A_odd)
if len(A_even) > 0:
    max_even = max(A_even)
    min_even = min(A_even)
max_even_count = A_even.count(max_even)
min_even_count = A_even.count(min_even)
max_odd_count = A_odd.count(max_odd)
min_odd_count = A_odd.count(min_odd)
########################### EVEN / ODD MAX / MIN COUNT
exchange = False

# CHECK IF A_even or A_odd ARE EMPTY /// NO MIN MAX
for _ in range(1, 50):
    command = input()
    if command == "end":
        break
    G = command.split()
    #print(len(D))
    first = G[0]
    number = (G[1])
    if len(G) > 2:
        num_type = G[2]
    if exchange:
        A_even = []
        A_odd = []
        for i in D:
            if int(i) % 2 == 0:
                A_even.append(int(i))
            else:
                A_odd.append(int(i))
    exchange = False
    ################### EXCHANGE INDEX
    if first == "exchange":
        if 0 <= int(number) < len_D:
            exchange = True
            left = D[0:int(number) + 1]
            right = D[int(number) + 1:]
            D = right + left
        elif int(number) > len(D):
            print("Invalid index")
        #print(D)
        continue
    if (number == "even" and len(A_even) == 0) or (number == "odd" and len(A_odd) == 0):
        print(f"No matches")
        continue
    # CHECK IF MAX / MIN VALUES ARE MORE THAN 1
    if (max_even_count > 1 or min_even_count > 1 or max_odd_count > 1 or min_odd_count > 1):
        ########### RETURN THE RIGHTMOST MIN/MAX INDEX
        for i, p in reversed(list(enumerate(D))):
            right_number = (
                    (command == "max odd" and p == str(max_odd)) or
                    (command == "min odd" and p == str(min_odd)) or
                    (command == "max even" and p == str(max_even)) or
                    (command == "min even" and p == str(min_even))
            )
            if right_number:
                print(i)
                break
    else:
        if command == "max odd":
            print(D.index(str(max_odd)))
        elif command == "min odd":
            print(D.index(str(min_odd)))
        elif command == "max even":
            print(D.index(str(max_even)))
        elif command == "min even":
            print(D.index(str(min_even)))
            ############################ COUNTING FIRST / LAST EVEN \ ODD
    if (first == "first" or first == "last"):
        pass
    else:
        continue
    if int(number) > len(D) and int(number) > len(D):
        print("Invalid count")
        continue
    if first == "first":
        if num_type == "even":
            print(A_even[0:int(number)])
        elif num_type == "odd":
            print(A_odd[0:int(number)])
    elif first == "last":
        if num_type == "even":
            print(A_even[-1 * int(number):])
        elif num_type == "odd":
            print(A_odd[-1 * int(number):])
E = []
for i in D:
    E.append(int(i))
print(E)