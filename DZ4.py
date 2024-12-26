PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

class House:
    houses_history = []

    def __new__(cls, name, number_of_floors):
        instance = super().__new__(cls)
        cls.houses_history.append(name)  # Добавляем название в историю при создании объекта
        return instance

    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
              print(f"{RED}Такого этажа{END} {YELLOW}{new_floor}{END} {RED}не существует, максимальный этаж{END} "
                    f"{YELLOW}{self.number_of_floors}{END}")
        else:
            for floor in range(1, new_floor + 1):
                print(f"{CYAN}{UNDERLINE}Поднимаемся на{END}",
                      f"{RED}{floor}-й{END}",
                      f"{PURPLE}этаж{END}")

    def get_floor_input(self):
        while True:
            try:
                new_floor = int(input(f"{GREEN}Введите этаж для перехода в {RED}{self.name}{END} {GREEN}(или{END} "
                                      f"{YELLOW}0{END} {GREEN}для выхода): {END}"))
                if new_floor == 0:
                    print(f"{YELLOW}Покидаем здание...{END}")
                    return
                self.go_to(new_floor)
            except ValueError:
                print(f"{RED}Пожалуйста, введите целое число.{END}")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"{GREEN}Название:{END} {YELLOW}{self.name}{END}, {GREEN}кол-во этажей:{END} "
                f"{YELLOW}{self.number_of_floors}{END}")


    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise TypeError(f"Невозможно сравнить {type(self)} с {type(other)}.")

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
        elif isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        else:
            raise TypeError(f"Невозможно прибавить {type(other)} к {type(self)}.")
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors -= other
        elif isinstance(other, House):
            self.number_of_floors -= other.number_of_floors
        else:
            raise TypeError(f"Невозможно вычесть {type(other)} из {type(self)}.")
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors *= other
        elif isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
        else:
            raise TypeError(f"Невозможно умножить {type(self)} на {type(other)}.")
        return self

    def __truediv__(self, other):
        if isinstance(other, int):
            self.number_of_floors //= other
        elif isinstance(other, House):
            self.number_of_floors //= other.number_of_floors
        else:
            raise TypeError(f"Невозможно поделить {type(self)} на {type(other)}.")
        return self

    def __floordiv__(self, other):
        if isinstance(other, int):
            self.number_of_floors //= other
        elif isinstance(other, House):
            self.number_of_floors //= other.number_of_floors
        else:
            raise TypeError(f"Невозможно поделить {type(self)} на {type(other)}.")
        return self

    def __mod__(self, other):
        if isinstance(other, int):
            self.number_of_floors %= other
        elif isinstance(other, House):
            self.number_of_floors %= other.number_of_floors
        else:
            raise TypeError(f"Невозможно взять остаток от деления {type(self)} на {type(other)}.")
        return self

    def __pow__(self, other):
        if isinstance(other, int):
            self.number_of_floors **= other
        elif isinstance(other, House):
            self.number_of_floors **= other.number_of_floors
        else:
            raise TypeError(f"Невозможно возвести {type(self)} в степень {type(other)}.")
        return self

    def __del__(self):
        print(f"{RED}<{self.name}> снесён, но он останется в истории{END}.")


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
del h2

del h3
print(House.houses_history)

print(House.houses_history)
# print(h1)
# # print(h2)
# print(h1 == h2) # __eq_
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
# h1 += 10 # __iadd__
# print(h1)
# h2 = 10 + h2 # __radd__
# print(h2)
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__