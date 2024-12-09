class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
### блок перегрузок
    def __eq__(self, other):
        return(self.number_of_floors == other.number_of_floors)
    def __lt__(self, other):
        return (self.number_of_floors < other.number_of_floors)
    def __le__(self, other):
        return (self.number_of_floors <= other.number_of_floors)
    def __gt__(self, other):
        return (self.number_of_floors > other.number_of_floors)
    def __ge__(self, other):
        return (self.number_of_floors >= other.number_of_floors)
    def __ne__(self, other):
        return (self.number_of_floors != other.number_of_floors)
### блок перегрузок закончен
### блоки задания мод 5.3:
    def __add__(self, value):
        #self = Название: ЖК Эльбрус, кол-во этажей: 10.
        self.number_of_floors += value
        return (self)
    def __radd__(self, value):
        return (self.__add__(value))
    def __iadd__(self, value):
        return (self.__add__(value))

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



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

