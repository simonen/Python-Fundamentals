def car_index(cars_f, car_f):
    for i, p in enumerate(cars_f):
        if p[0] == car_f:
            return i


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
    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car_index(cars, car)][2] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car_index(cars, car)][1] += distance
            cars[car_index(cars, car)][2] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car_index(cars, car)][1] > 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car_index(cars, car))

    elif action == "Refuel":
        refuel = int(command[2])
        max_fuel = 75
        if cars[car_index(cars, car)][2] + refuel > max_fuel:
            refuel = refuel - (cars[car_index(cars, car)][2] + refuel - max_fuel)
            cars[car_index(cars, car)][2] = 75
        else:
            cars[car_index(cars, car)][2] += refuel
        print(f"{car} refueled with {refuel} liters")

    elif action == "Revert":
        take_kilometers = int(command[2])
        min_mileage = 10000
        if cars[car_index(cars, car)][1] - take_kilometers > min_mileage:
            cars[car_index(cars, car)][1] -= take_kilometers
            print(f"{car} mileage decreased by {take_kilometers} kilometers")
        else:
            cars[car_index(cars, car)][1] = min_mileage

    command = input()

for c in cars:
    print(f"{c[0]} -> Mileage: {c[1]} kms, Fuel in the tank: {c[2]} lt.")
