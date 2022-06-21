numbers = list(map(int, input().split(" ")))

average = sum(numbers) // len(numbers)
sorted_list = sorted(numbers, reverse=True)
last_five = [str(x) for x in sorted_list[:5] if x > average]

if len(last_five) > 0:
    last_five = " ".join(last_five)
    print(last_five)
else:
    print("No")
