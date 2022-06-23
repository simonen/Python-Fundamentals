numbers = list(input().split())
command = input()

turns = 0
while command != "end":
    turns += 1
    command_in = command.split()
    index1 = int(command_in[0])
    index2 = int(command_in[1])
    indices = [index1, index2]

    if (0 <= index1 <= len(numbers) - 1) and (0 <= index2 <= len(numbers) - 1) and index1 != index2:
        if numbers[index1] == numbers[index2]:
            print(f"Congrats! You have found matching elements - {numbers[index1]}!")
            numbers = [numbers[x] for x in range(len(numbers)) if x not in indices]
        else:
            print("Try again!")
    else:
        print(f"Invalid input! Adding additional elements to the board")
        numbers.insert((len(numbers) // 2), f"-{str(turns)}a")
        numbers.insert((len(numbers) // 2), f"-{str(turns)}a")

    if len(numbers) == 0:
        print(f"You have won in {turns} turns!")
        break

    command = input()
else:
    print("Sorry you lose :(")
    print(" ".join(numbers))
