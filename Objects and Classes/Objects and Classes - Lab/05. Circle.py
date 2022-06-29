class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.diameter * Circle.__pi

    def calculate_area(self):
        return Circle.__pi * (self.diameter / 2) ** 2

    def calculate_area_of_sector(self, angle):
        return Circle.__pi * (self.diameter / 2) ** 2 * angle / 360


# circle = Circle(10)
# print()
# circumference = circle.calculate_circumference()
# area = circle.calculate_area()
# sector_area = circle.calculate_area_of_sector(5)
# print(f"{circumference:.2f}")
# print(f"{area:.2f}")
# print(f"{sector_area:.2f}")