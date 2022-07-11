import itertools as it

username = input().split(", ")
invalid = [chr(x) for x in it.chain(range(32, 45), range(46, 48), range(58, 65), range(91, 95), range(96, 97))]

for user in username:
    is_invalid = False
    if len(user) not in range(3, 17):
        continue
    for letter in user:
        if letter in invalid:
            is_invalid = True
            break
    if is_invalid:
        continue
    print(user)