
# TODO: Подробно описать три произвольных класса

import doctest

# TODO: описать класс

class student:
    def __init__ (self, surname: str = None, add_debt: int = 0, is_in_uni: bool = False):
        """
        Создание объета класса "student"
        :param surname: фамилия студента (str)
        :param add_debt: Количество долгов у студента (int)
        :param is_in_uni: Учится ли студент в ВУЗе (bool)

        Примеры:
        >>> student1 = student("Ivanov", 1, True)   # Инициализация объекта класса
        """
        self.add_data(surname, add_debt, is_in_uni)

    def add_data (self, surname: str = None, add_debt: int = 0, is_in_uni: bool = None):
        """
        добавление данных о студенте

        :param surname: фамилия студента (str)
        :param add_debt: Количество долгов у студента (int)
        :param is_in_uni: Учится ли студент в ВУЗе (bool)
        """
        self.surname = surname
        if add_debt >= 0:  # Студент не может иметь отрицательное количество долгов
            self.add_debt = add_debt
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.is_in_uni = is_in_uni

# TODO: описать ещё класс

class cat:

    def __init__(self, name: str = None, age: int = None, breed: str = None):
        """
        Создание объекта класса "cat":
        :param name: имя кота (str)
        :param age: Возраст кота (int)
        :param breed: порода кота (str)

        Примеры:
        >>> cat1 = cat("pisi", 3, "borzoi")   # Инициализация объекта класса
        """
        self.add_data(name, age, breed)

    def add_data(self, name: str = None, age: int = None, breed: str = None):
        """
        добавление данных о коте

        :param name: имя кота (str)
        :param age: Возраст кота (int)
        :param breed: порода кота (str)
        """
        self.name = name
        if age >= 0:   # Возраст не может быть отрицательным
            self.age = age
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.breed = breed

    def print_data(self):
        print(self.name, self.age, self.breed)

# TODO: и ещё один
class coffee:
    def __init__(self, name: str = None, plce_of_origin: str = None, roasted: bool = False):
        """
        Создание объекта класса "coffee"
        :param name: Название кофе (str)
        :param plce_of_origin: Место происхождения кофе (str)
        :param roasted: Обжарено ли кофе (bool)

        Примеры:
        >>> coffe1 = coffee("Арабика", "Бразилия", True)
        """
        self.add_data(name, plce_of_origin, roasted)

    def add_data(self, name: str = None, plce_of_origin: str = None, roasted: bool = False):
        """
        Функция добавления данных о кофе 
        :param name: Название кофе (str)
        :param plce_of_origin: Место происхождения кофе (str)
        :param roasted: Обжарено ли кофе (bool)
        """
        self.name = name
        self.plce_of_origin = plce_of_origin
        self.roasted = roasted
    def print_data(self):
        """
        Функция вывода данных о кофе
        """
        print(self.name, self.plce_of_origin, self.roasted)

cat1 = cat("pisi", 3, "borzoi")
coffee1 = coffee("Арабика", "Бразилия", True)
student1 = student("Ivanov", 1, True)
print (student1.__dict__)