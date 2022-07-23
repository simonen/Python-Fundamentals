def car_index(cars_f, car_f):
    for ind, p in enumerate(cars_f):
        if p[0] == car_f:
            return ind


cars_count = int(input())

cars = []
for _ in range(cars_count):
    cars_string = input().split("|")
    car, mileage, tank = cars_string
    cars.append([car, int(mileage), int(tank)])

command = input()

while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    car = command[1]
    i = car_index(cars, car)
    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if cars[i][2] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[i][1] += distance
            cars[i][2] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[i][1] > 100000:
            print(f"Time to sell the {car}!")
            cars.pop(i)

    elif action == "Refuel":
        refuel = int(command[2])
        max_fuel = 75
        if cars[i][2] + refuel > max_fuel:
            refuel = refuel - (cars[i][2] + refuel - max_fuel)
            cars[i][2] = 75
        else:
            cars[i][2] += refuel
        print(f"{car} refueled with {refuel} liters")

    elif action == "Revert":
        rev_kilometers = int(command[2])
        min_mileage = 10000
        if cars[i][1] - rev_kilometers > min_mileage:
            cars[i][1] -= rev_kilometers
            print(f"{car} mileage decreased by {rev_kilometers} kilometers")
        else:
            cars[i][1] = min_mileage

    command = input()

for c in cars:
    print(f"{c[0]} -> Mileage: {c[1]} kms, Fuel in the tank: {c[2]} lt.")
