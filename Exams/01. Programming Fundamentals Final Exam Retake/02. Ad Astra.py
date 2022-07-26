import re

text = input()

match = re.findall(r"(#|\|)([a-zA-Z ]+)(\1)([0-9]{2}\/[0-9]{2}\/[0-9]{2})(\1)([0-9]{1,5})(\1)", text)
total_calories = 0
item_list = []

for m in match:
    food = m[1]
    date = m[3]
    calories = int(m[5])
    if 0 < calories <= 10000:
        total_calories += calories

    item_list.append(f"Item: {food}, Best before: {date}, Nutrition: {calories}")

print(f"You have food to last you for: {total_calories // 2000} days!")

for item in item_list:
    print("".join(item))
