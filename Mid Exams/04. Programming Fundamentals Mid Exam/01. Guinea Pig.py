food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
pig_weight_kg = float(input())

pig_weight_g = pig_weight_kg * 1000
hay_g = hay_kg * 1000
food_g = food_kg * 1000
cover_g = cover_kg * 1000

for day in range(1, 31):
    food_g -= 300
    if day % 2 == 0:
        hay_g -= food_g * 0.05
    if day % 3 == 0:
        cover_g -= (pig_weight_g / 3)
    if food_g <= 0 or hay_g <= 0 or cover_g <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_g / 1000:.2f}, Hay: {hay_g / 1000:.2f}, Cover: {cover_g / 1000:.2f}.")
