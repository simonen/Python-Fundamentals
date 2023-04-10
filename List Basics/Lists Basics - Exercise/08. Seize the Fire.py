cells = input().split("#")
water = int(input())

total_fire = 0
print("Cells:")

for i in cells:
    cell = i.split(" = ")
    fire_type = cell[0]
    fire_value = int(cell[1])
    fire_command = (
            (fire_type == "High" and 81 <= fire_value <= 125) or
            (fire_type == "Medium" and 51 <= fire_value <= 80) or
            (fire_type == "Low" and 1 <= fire_value <= 50) and
            (water >= fire_value)
    )
    if fire_command:
        print(" -", fire_value)
        water -= fire_value
        total_fire += fire_value

effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
