#Task 1
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}
# list_ = []
# list_.append(a)
# list_.append(b)
# list_.append(c)
# for i in list_:
#     print(len(i))
#Task 2
# class Dog:
#     def voice(self):
#         print('Гав')
# class Cat:
#     def voice(self):
#         print('Мяу')
# barsik = Cat()
# rex = Dog()
# def to_pet(dalban):
#     dalban.voice()
# to_pet(barsik)
# to_pet(rex)

#Task 3
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'
# class Employee(Person):
#         def __init__(self, name, last_name, work, status):
#             super().__init__(name, last_name)
#             self.work = work
#             self.status = status
#         def get_info(self):
#             return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'
# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'
# person = Person('Иван', 'Петров')
# employee = Employee('Иван', 'Петров', 'Рога и Копыта', 'директор')
# student = Student('Иван', 'Петров', 'КГТУ', 3)
# def get_human_info(dalban):
#     print(dalban.get_info())
# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person)
#Task 4
# from abc import ABC, abstractmethod
# import math
# class Shape(ABC):
#     pi = 3.14
#     @abstractmethod
#     def get_area(self):
#         pass
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         res = 0.5 * self.base * self.height
#         return res
# class Square(Shape):
#     def __init__(self, lenght):
#         self.lenght = lenght
#     def get_area(self):
#         res = self.lenght ** 2
#         return res
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         res = math.pi * self.radius ** 2
#         return res
# triangle = Triangle(5, 5)
# square = Square(5)
# circle = Circle(10)
# print(triangle.get_area()) 
# print(square.get_area())
# print(circle.get_area()) 
#Task 5
# class OS:
#     def __init__(self, version):
#         self.version = version
# class Windows(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + C'
# class MacOS(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'
# class Linux(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + SHIFT + C'

# win = Windows(1)
# mac = MacOS(2)
# lin = Linux(4)
# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))


#Task 6
# class Language:
#     def __init__(self, level, type):
#         self.level = level
#         self.type = type
# class Python(Language):
#     def write_function(self, func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f'def {self.func_name}({self.arg}):'
#     def create_variable(self, var_name, value):
#         self.var_name = var_name
#         self.value = value
#         return f'{self.var_name} = {self.value.__repr__()}'
# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         res = '{     }'
#         return f'function {self.func_name}({self.arg}) {res};'
#     def create_variable(self, var_name, value):
#         self.var_name = var_name
#         self.value = value
#         return f'let {self.var_name} = {self.value.__repr__()};'
# py = Python('fdas', 3)
# js = JavaScript('dsadsa', 1)
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John')) 
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))
#Task 7
# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol
# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         self.amount = amount
#         res = self.amount * self.rate
#         return f'$ {self.amount} равен {res} сомам'
# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         self.amount = amount
#         res = self.amount * Euro.rate
#         return f'€ {self.amount} равен {res} сомам'
# e = Euro('des', 3)
# d = Dollar('dea', 3)
# print(d.exchange(100))
# print(e.exchange(80))
# Task 8

# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit
# class Mercury(Planet):
#     def __init__(self, orbit):
#         super().__init__(orbit)

#     def get_age(self, earth_age):
#         self.earth_age = earth_age
#         res = self.earth_age * 365 // self.orbit
#         return f'на Меркурии ваш возраст составляет {res} лет'
# class Jupiter(Planet):
#     def __init__(self, orbit):
#         super().__init__(orbit)
#     def get_age(self, earth_age):
#         self.earth_age = earth_age
#         res = (self.earth_age * 365 // self.orbit) * (24 * 365)
#         return f'на Юпитере ваш возраст составляет {res} часов'
# class Venus(Planet):
#     def __init__(self, orbit):
#         super().__init__(orbit)
#     def get_age(self, earth_age):
#         self.earth_age = earth_age
#         res = self.earth_age * 365 / self.orbit * 365
#         return f'на Венере ваш возраст составляет {round(res)} дней'
# merc = Mercury(88)
# print(merc.get_age(20))
# ven = Venus(225)
# print(ven.get_age(20))
# jup = Jupiter(12)
# print(jup.get_age(20))



