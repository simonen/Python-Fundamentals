class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []
        self.free_capacity = self.__capacity

    def add_item(self, item: str):
        if self.free_capacity > 0:
            self.items.append(item)
            self.free_capacity -= 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.free_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

