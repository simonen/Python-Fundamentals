fires_cells = input()
water = int(input())

high = range(81, 126)
mid = range(51, 81)
low = range(1, 51)

cell_list = fires_cells.split(" = ")
cell_list = " ".join(cell_list)
cell_list = cell_list.split("#")

print("Cells:")
total_fire = 0

for cell in cell_list:
    fire = int(cell.split()[1])
    fire_command = (
            ("High" in cell and fire in high and water >= fire) or
            ("Medium" in cell and fire in mid and water >= fire) or
            ("Low" in cell and fire in low and water >= fire)
    )
    if fire_command:
        print(f" - {cell.split()[1]}")
        total_fire += fire
        water -= fire

effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print("Total Fire: " + str(total_fire))

