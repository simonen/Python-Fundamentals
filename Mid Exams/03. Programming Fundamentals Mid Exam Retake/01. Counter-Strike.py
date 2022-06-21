start_energy = int(input())

command = input()
wins = 0

while command != "End of battle":
    energy = int(command)
    if energy <= start_energy:
        start_energy -= energy
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {start_energy} energy")
        break
    if wins % 3 == 0:
        start_energy += wins
    command = input()
else:
    print(f"Won battles: {wins}. Energy left: {start_energy}")