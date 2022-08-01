countries = input().split(", ")
cities = input().split(", ")

dict = {countries[i]: cities[i] for i in range(0, len(countries))}

for k, v in dict.items():
    print(f"{k} -> {v}")

# countries = input().split(", ")
# capitals = input().split(", ")
#
# book = dict(zip(countries, capitals))
#
# for country, capital in book.items():
#     print(f"{country} -> {capital}")