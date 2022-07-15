#Task 1
# class Auto:
#     def ride(self):
#         print('Riding on a ground')
# class Boat:
#     def swim(self):
#         print('Floating on water')
# class Amphibian(Auto, Boat):
#     pass
# obj = Amphibian()
# obj.ride()
# obj.swim()    
#Task 2

# class RadioMixin:
#     def play_music(self, title):
#         self.title = title
#         return(f'Песня называется {self.title}')
# class Auto(RadioMixin):
#     pass
# class Boat(RadioMixin):
#     pass
# class Amphibian(Auto, Boat):
#     pass
# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# print(auto.play_music('auto'))
# print(boat.play_music('bout'))
# print(obj.play_music('Amphibian'))

#Task 3
# from datetime import datetime
# class Clock:
#     def current_time(self):
#         now = datetime.now()
#         res = now.strftime('%H:%M:%S')
#         print(res)
# class Alarm:
#     def on(self):
#         print('Alarm clock on')
#     def off(self):
#         print('Alarm clock off')
# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()
# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()
#Task 4
from abc import ABC, abstractmethod
class Coder(ABC):
    count_code_time = 0
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def coding(self):
        pass
class Backend(Coder):
    def __init__(self, experience, languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend
    def get_info(self):
        return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
    
    def coding(self, chislo):
        self.count_code_time += chislo
 

class Frontend(Coder):
    def __init__(self, experience, languages_frontend):
        self.experience = experience
        self.languages_frontend = languages_frontend
    def get_info(self):
        return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
    
    def coding(self, chislo):
        self.count_code_time += chislo
class Fullstack(Backend, Frontend):
    pass
a = Backend('Junior', 'Python')
b = Frontend('Middle', 'Javascript')
c = Fullstack('Middle', 'Python and JS')
a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info())         
# Task 5
# class Square:
#     def __init__(self, side):
#         self.side = side
#     def get_area(self):
#         res = self.side ** 2
#         return res

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
#     def get_area(self):
#         res = 0.5 * self.base * self.height
#         return res
# class Pyramid(Triangle, Square):
#     def get_volume(self):
#         res = int(1/3 * self.base ** 2 * self.height)
#         return res
# cal = Square(4)
# cal2 = Triangle(5,5)
# cal3 = Pyramid(5,5)
# print(cal.get_area())
# print(cal2.get_area())
# print(cal3.get_area())

#Task 6
class CreateMixin:
    def create(self, key, todo):
        if key in self.todos.keys():
            return 'Задача под таким ключём уже существует'
        self.todos[key] = todo
        return self.todos

class DeleteMixin:
    def delete(self, key):
        res = None
        if key in self.todos.keys():
            res = self.todos.pop(key)
        return res

class UpdateMixin:
    def update(self, key, new_value):
        self.todos.update({key:new_value})
        return self.todos

class ReadMixin:
    def read(self):
        res = [x for x in self.todos.items()]
        return sorted(res)

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    def __init__(self):
        self.todos = {}

    def set_deadline(self, data):
        from datetime import date
        data = data.split('/')
        dead_line = date(int(data[2]), int(data[1]),int(data[0]))
        date_now = date.today()
        res = dead_line - date_now
        return res.days

task = ToDo()

print(task.create(1, 'Do housework'))
print(task.create(1, 'Do housework'))
print(task.create(2,'Go for a walk'))
print(task.update(1, 'Do homework'))
print(task.delete(2))
print(task.read())
print(task.set_deadline('6/7/2022'))