book = {"Algo": {"Peter": 350, "Prakash": 300, "George": 300}}

students = ["Peter", "Prakash", "George"]

# for s in sorted(students, key=lambda x: x[0]):
#     sorted1 = sorted(book["Algo"], key=lambda y: y[1])
#     #print(f"} -> {book['Algo'][s]}")
#

for v in range(len(book["Algo"])):
    sorted_a = sorted(book["Algo"].items(), key=lambda x: x[0])
    sorted_v = sorted(sorted_a, key=lambda x: x[1], reverse=True)
    print(f"{sorted_v[v][0]} -> {sorted_v[v][1]}")