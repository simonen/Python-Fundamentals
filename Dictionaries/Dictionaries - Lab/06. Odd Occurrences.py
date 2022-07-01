words = input().lower().split()

B = {lett: words.count(lett) for lett in words if words.count(lett) % 2 != 0}

# for key in B.keys():
#     print(key, end=" ")
D = []
C = [D.append(letter) for letter in words if words.count(letter) % 2 != 0 and letter not in D]

print(" ".join(D))