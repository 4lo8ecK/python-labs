class Item:
    def __init__(self, name: str, price: int):
        self.__name: str = name
        self.__price: int|float = price

    def get_name(self) -> str:
        return self.__name
    
    def get_price(self) -> int|float:
        return self.__price

class ShoppingCart:
    def __init__(self):
        self.__items: list[Item] = []
    
    def add_item(self, name: str, price: int, item: list[Item]|None = None) -> None:
        if item == None:
            self.__items += [Item(name, price)]
        else:
            self.__items += [item]
    
    def total(self) -> int|float:
        res = 0
        for i in self.__items:
            res += i.get_price()
        return res
    
    def item_count(self) -> int:
        return len(self.__items)


if __name__ == "__main__":
    
    cart = ShoppingCart()
    cart.add_item("Хлеб", 50)
    cart.add_item("Молоко", 80)
    print(cart.total()) # 130
    print(cart.item_count()) # 2