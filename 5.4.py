# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
#
# ex = Example('data', second=25, third=3.14)


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):  # ,*args, **kwargs
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
### блок перегрузок
    def __eq__(self, other):
        if isinstance(other, House):
            return(self.number_of_floors == other.number_of_floors)
        else:
            print('неверный тип данных')
    def __lt__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors < other.number_of_floors)
        else:
            print('неверный тип данных')
    def __le__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors <= other.number_of_floors)
        else:
            print('неверный тип данных')
    def __gt__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors > other.number_of_floors)
        else:
            print('неверный тип данных')
    def __ge__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors >= other.number_of_floors)
        else:
            print('неверный тип данных')
    def __ne__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors != other.number_of_floors)
        else:
            print('неверный тип данных')
### блок перегрузок закончен
### блоки задания мод 5.3:
    def __add__(self, value):
        #self = Название: ЖК Эльбрус, кол-во этажей: 10.
        if isinstance(value, int):
            self.number_of_floors += value
            return (self)
        else:
            print('неверный тип данных')
    def __radd__(self, value):
        return (self.__add__(value))
    def __iadd__(self, value):
        return (self.__add__(value))

    def __del__(self):
        print(self.name, ' снесён, но он останется в истории')

    ### блоки задания мод 5.3 закончились

    def __len__(self):
        return (self.number_of_floors)

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.')

    def go_to(self, new_floor : int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


#
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__

