import re

string = input()

match = re.findall(r"(#|\|)([A-Za-z ]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]{1,5})\1", string)
total_cals = sum([int(x[3]) for x in match])
days = total_cals // 2000
items = [x[1::] for x in match]
print(f"You have food to last you for: {days} days!")

for item in items:
    calories = item[2]
    food = item[0]
    date = item[1]
    print(f"Item: {food}, Best before: {date}, Nutrition: {calories}")
