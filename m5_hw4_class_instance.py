class House:

    house_history = []

    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

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
        return self.number_of_floors

    def __radd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __iadd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self.number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


# Практическое задание № 1 - Атрибуты и методы объекта

# dream_h = House('ЖК Дом мечты', 10)
# elite_h = House('ЖК Элита', 20)

# dream_h.go_to(4)
# elite_h.go_to(44)

# Практическое задание № 2 - Специальные методы классов

# print()
# print(dream_h)
# print(len(dream_h))
# print(elite_h)
# print(len(elite_h))

# Практическое задание № 3 - Перегрузка операторов

# print(dream_h)
# print(elite_h)
#
# print(dream_h == elite_h)
#
# dream_h.number_of_floors = dream_h + 10
# print(dream_h)
# print(dream_h == elite_h)
#
# dream_h.number_of_floors += 10
# print(dream_h)
#
# elite_h.number_of_floors = 10 + elite_h
# print(elite_h)
#
# print(dream_h > elite_h)
# print(dream_h >= elite_h)
# print(dream_h < elite_h)
# print(dream_h <= elite_h)
# print(dream_h != elite_h)

# Практическое задание № 4 - Различие атрибутов класса и экземпляра

dream_h = House('ЖК Дом мечты', 10)
print(House.house_history)
elite_h = House('ЖК Элита', 20)
print(House.house_history)
city_h = House('ЖК Городок', 30)
print(House.house_history)

del elite_h
del city_h

print(House.house_history)
