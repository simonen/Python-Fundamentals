class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        by_letter = [x for i, x in enumerate(self.products) if self.products[i][0] == first_letter]
        return by_letter

    def __repr__(self):
        joined = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{joined}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Zzza")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")

catalogue.add_product("Hair")
catalogue.add_product("Carpet")
catalogue.add_product("Zafa")
print(catalogue.get_by_letter("Z"))
print(catalogue) ## repr



