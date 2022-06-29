class Zoo:

    __animals = 0

    def __init__(self, zooname):
        self.zooname = zooname
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == "mammal":
            result += f"Mammals in {self.zooname}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.zooname}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.zooname}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zname = input()
animals = int(input())

myzoo = Zoo(zname)
command = ''

for animal in range(animals):
    ani_type = list(input().split())
    myzoo.add_animal(ani_type[0], ani_type[1])


command = input()
print(myzoo.get_info(command))