countries = input().split(", ")
cities = input().split(", ")

dict = {countries[i]: cities[i] for i in range(0, len(countries))}

for k, v in dict.items():
    print(f"{k} -> {v}")

# for i in range(0, len(countries)):
#     key = countries[i]
#     value = capitals[i]
#     dict[key] = value

#print(dict)

