number_list = list(map(int, input().split(", ")))

E = []
# for i, v in enumerate(number_list):
#     if v % 2 == 0:
#         E.append(i)
#
#
# print(E)

found_indices = map(
    lambda x: x if number_list[x] % 2 == 0 else "False",
    range(len(number_list))
)

even_i = list(filter(lambda a: a != "False", found_indices))

print(even_i)
