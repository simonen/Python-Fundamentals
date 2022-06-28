class Party:

    people_count = 0

    def __init__(self):
        self.people = []

        Party.people_count += 1


command = input()
party_list = Party()

while command != "End":
    going = command
    party_list.people.append(going)

    command = input()

going = ", ".join(party_list.people)
print(f"Going: {going}")
print(f"Total: {len(party_list.people)}")