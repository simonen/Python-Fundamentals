health = int(input())
command = input()

initial_health = health
V = []
remaining_health = 0

while command != "end":
    virus = command
    v_power = sum(list(map(ord, virus))) // 3
    defeat_time = v_power * len(virus) #seconds
    if V.count(virus) == 1:
        defeat_time //= 3
    V.append(virus)
    health -= defeat_time
    print(f'Virus {virus}: {v_power} => {defeat_time} seconds')

    if health > 0:
        print(f"{virus} defeated in {defeat_time // 60}m {defeat_time % 60}s.")
        print(f'Remaining health: {int(health)}')
        health = int(health * 1.2)
    else:
        print("Immune System Defeated.")
        break

    if health > initial_health:
        health = initial_health
    remaining_health = health

    command = input()
else:
    print(f"Final Health: {remaining_health:.0f}")
