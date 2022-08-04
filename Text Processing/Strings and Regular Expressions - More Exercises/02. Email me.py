email = input()

index = email.index("@")
result = sum(map(ord, email[0:index + 1])) - sum(map(ord, email[index::]))

if result >= 0:
    print("Call her!")
else:
    print("She is not the one.")
