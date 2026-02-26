from datetime import date

class RestaurantOrder:
    def __init__(self) -> None:
        self.__time = date.today()
        self.__count: int = 0
        self.__prices: list[float|int] = []

    def __str__(self) -> str:
        return f'Дата: {self.__time}\nЧисло персон: {self.__count}\nИтого: {self.get_summ()}'

    # индивидуальный заказ на человека
    def new(self, price: int|float = None) -> None:
        if price != None:
            self.__count += 1
            self.__prices += [price]
    def get_summ(self) -> float|int:
        return sum(self.__prices)
# !RestaurantOrder

# int main() :)
if __name__ == "__main__":

    order = RestaurantOrder()
    order.new(1212)
    order.new(1345)
    order.new(13)


    print(order)