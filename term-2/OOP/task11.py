class Item:
    def __init__(self, name: str, price: int):
        self.name: str = name
        self.price: int|float = price


class ShoppingCart:
    def __init__(self):
        self.items: list[Item] = []
    
    def add_item(self, name: str, price: int, item: list[Item]|None = None) -> None:
        if item == None:
            self.items += [Item(name, price)]
        else:
            self.items += [item]
    
    def total(self) -> int|float:
        res = 0
        for i in self.items:
            res += i.price
        return res
    
    def item_count(self) -> int:
        return len(self.items)

cart = ShoppingCart()
cart.add_item("Хлеб", 50)
cart.add_item("Молоко", 80)
print(cart.total()) # 130
print(cart.item_count()) # 2