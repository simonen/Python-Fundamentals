numbers = list(input().split())
command = input()

turns = 0
while command != "end":
    turns += 1
    command_in = command.split()
    index1 = int(command_in[0])
    index2 = int(command_in[1])

    if (0 <= index1 <= len(numbers) - 1) and (0 <= index2 <= len(numbers) - 1) and index1 != index2:
        if numbers[index1] == numbers[index2]:
            print(f"Congrats! You have found matching elements - {numbers[index1]}!")
            numbers.pop(index1)
            if index2 > 0:
                numbers.pop(index2 - 1)
            else:
                numbers.pop(index2)
        else:
            print("Try again!")
    else:
        print(f"Invalid input! Adding additional elements to the board")
        numbers.insert((len(numbers) // 2), "-" + str(turns) + "a")
        numbers.insert((len(numbers) // 2), "-" + str(turns) + "a")

    if len(numbers) == 0:
        print(f"You have won in {turns} turns!")
        break

    command = input()
else:
    print("Sorry you lose :(")
    print(" ".join(numbers))
