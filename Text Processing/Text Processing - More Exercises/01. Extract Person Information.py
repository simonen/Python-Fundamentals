n = int(input())

for _ in range(1, n + 1):
    name = ''
    age = ''
    string = input().split()

    for word in string:
        if "@" in word and "|" in word:
            id1 = word.rindex("@")
            id2 = word.index("|")
            name = word[id1 + 1:id2]

        if "#" in word and "*" in word:
            id1 = word.rindex("#")
            id2 = word.index("*")
            age = word[id1 + 1:id2]

    print(f"{name} is {age} years old.")

