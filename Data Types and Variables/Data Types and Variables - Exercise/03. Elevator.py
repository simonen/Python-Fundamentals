import math
people = int(input())
capacity = int(input())

courses = people // capacity
remaining_people = people - (capacity * courses)
if remaining_people != 0:
    courses += 1

print(courses)