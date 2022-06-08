fires_cells = input().split("#")
water = int(input())

high = range(81, 126)
mid = range(51, 81)
low = range(1, 51)

print("Cells:")
total_fire = 0

for cell in fires_cells:
    split_cell = cell.split(" = ")
    fire = int(split_cell[1])
    fire_command = (
            ("High" in cell and fire in high and water >= fire) or
            ("Medium" in cell and fire in mid and water >= fire) or
            ("Low" in cell and fire in low and water >= fire)
    )
    if fire_command:
        print(f" - {split_cell[1]}")
        total_fire += fire
        water -= fire

effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print("Total Fire: " + str(total_fire))

