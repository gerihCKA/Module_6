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
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            # print(Color.RED + f'Такого этажа {new_floor} не существует, максимальный этаж {self.number_of_floors}' + Color.END)
              print(f"{RED}Такого этажа{END} {YELLOW}{new_floor}{END} {RED}не существует, максимальный этаж{END} {YELLOW}{self.number_of_floors}{END}")
        else:
            for floor in range(1, new_floor + 1):
                print(f"{CYAN}{UNDERLINE}Поднимаемся на{END}",
                      f"{RED}{floor}-й{END}",
                      f"{PURPLE}этаж{END}")

    def get_floor_input(self):
        while True:
            try:
                new_floor = int(input(f"{GREEN}Введите этаж для перехода в {RED}{self.name}{END} {GREEN}(или{END} {YELLOW}0{END} {GREEN}для выхода): {END}"))
                if new_floor == 0:
                    print(f"{YELLOW}Покидаем здание...{END}")
                    return
                self.go_to(new_floor)
            except ValueError:
                print(f"{RED}Пожалуйста, введите целое число.{END}")

building_name = input(f"{GREEN}Введите название здания: {END}")
number_of_floors = int(input(f"{GREEN}Введите количество этажей: {END}"))

house = House(building_name, number_of_floors)
house.get_floor_input()