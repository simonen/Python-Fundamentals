class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        lettered = [x for i, x in enumerate(self.products) if self.products[i][0] == first_letter]
        return lettered

    def __repr__(self):
        print(f"Items in {self.name} catalogue: ")
        return "\n".join(sorted(self.products))


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



