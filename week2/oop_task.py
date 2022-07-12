# Task 1
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def show_author(self):
#         return f'Автор этой песни {self.author}'
#     def show_title(self):
#         return f'Название этой песни {self.title}'
#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'
# song = Song('Happy', 'Aibek', 2001)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

#Task 2
# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return pow(self.radius, 2) * Circle.pi
        
# circle = Circle(2)
# circle.color = 'red'
# print(circle.color)
# print(circle.get_area())
#Task 3
# class BankAccount:
#     balance = 0
#     def deposit(self, amount):
#         self.amount = amount
#         BankAccount.balance += amount
#         print(f'Ваш баланс: {BankAccount.balance} сом') 
#     def withdraw(self, amount):
#         self.amount = amount
#         BankAccount.balance -= amount
#         print(f'Ваш баланс: {BankAccount.balance} сом')
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

#Task 4
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self, km):
#         kmch = self.cost + self.cost_km * km
#         return f'Такси {self.name}, стоимость поездки: {kmch} сом'
# taxi1 = Taxi('Namba', 45, 7)
# taxi2 = Taxi('Yandex', 69, 18)
# taxi3 = Taxi('Jorgo', 43, 15)
# print(taxi1.get_total_cost(10))
# print(taxi2.get_total_cost(6))
# print(taxi3.get_total_cost(14))
#Task 5
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: +{self.phone}')

# contact = Phone('Aibek', 'Basketbolov', +996709465252)
# contact.get_info()
#Task 6
# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
#     def count_percent(self):
#         res = self.salary / 100 * self.percent
#         result = self.experience * res
#         return result
# obj = Salary(10000, 10)
# print(obj.count_percent())
#Task 7
# from datetime import date

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
    
#     def get_year(self):
#         current_year = date.today().year
#         return f'выиграл {current_year - self.year} лет назад' 

# winner1 = Nobel('Литература', 1971, 'Пабло Неруда') 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())
  
# winner2 = Nobel('Литература', 1994, 'Кэндзабуро Оэ') 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())
#Task 8
# class Password:
#     def __init__(self, password):
#         self.password = password

#     def validate(self):
#         if 8 > len(self.password) or len(self.password) > 15:
#             raise Exception('Password should be longer than 8, and less than 15')
        
#         check_num = list(filter(lambda x: x.isdigit(), self.password))
#         if  len(check_num) == 0:
#             raise Exception('Password should contain numbers too')

#         check_alpha = list(filter(lambda x: x.isalpha(), self.password))
#         if len(check_alpha) == 0:
#             raise Exception('Password should contain letters as well')

#         check_symbol = list(filter(lambda x: x in '@#&$%!~*', self.password))
#         if len(check_symbol) == 0:
#             raise Exception('Your password should have some symbols')
        
#         return 'Ваш пароль сохранен.'

#     def __str__(self):
#         pass_length = len(self.password)
#         return pass_length * '*'

# password = Password('we@#3fdfe')

# print(password.validate())
# class Password:
#     def __init__(self, password):
#         self.password = password
#     def validate(self):
#         if 8 > len(self.password) or len(self.password) > 15:
#             raise Exception('Password should be longer than 8, and less than 15')
#         nums = list(filter(lambda x: x.isdigit(), self.password))
#         if len(nums) == 0:
#             raise Exception ('Password should contain numbers too')
#         words = list(filter(lambda x : x.isalpha(), self.password))
#         if len(words) == 0:
#             raise Exception('Password should contain letters as well')
#         sym = list(filter(lambda x: x in '@#&$%!~*', self.password))
#         if len(sym) == 0:
#             raise Exception('Your password should have some symbols ')
#         return 'Ваш пароль сохранен'
#     def __str__(self):
#         pass_ = len(self.password)
#         return pass_ * '*'
# password = Password('')     
# print(password.validate())        

# Task 9
# import math
# class Math:
#     def __init__(self, value):
#         self.value = value
#     def get_factorial(self):
#         fk = math.factorial(self.value)
#         return fk
#     def get_sum(self):
#         sum_ = map(int, str(self.value))
#         res = sum(sum_)
#         return res
#     def get_mul_table(self):
#         end = ""
#         num = list(range(1,11))
#         for nums in num:
#             sq = self.value * nums
#             end += f'{self.value}x{nums}={sq}\n'
#         return end
# mat = Math(11)
# print(mat.get_factorial())
# print(mat.get_sum())
# print(mat.get_mul_table())
        
#Task 10
# class ToDo:
#     instances = {}

#     def __init__(self, todo):
#         self.todo = todo
    
#     def give_priority(self, priority):
#         self.instances.update({priority: self.todo})

#     def list_of_tasks(self):
#         todo_list = list(self.instances.items())
#         todo_list.sort(key=lambda todo: todo[0])
#         return todo_list

# todo1 = ToDo('Сделать домашку')
# todo2 = ToDo('Сходить в кино')
# todo3 = ToDo('Погулять с девушкой')

# todo1.give_priority(2)
# todo2.give_priority(1)
# todo2.give_priority(3)
# print(ToDo.instances)
# print(todo1.list_of_tasks())



# import random
# class Sniper:
#   def __init__(self, name):
#     self.name = name
#     self.health = 100
#   def shoots(self, sniper):
#     sniper.health -= 20
    
# sniper1 = Sniper(name='Bob')
# sniper2 = Sniper(name='Tom')

# choices = (sniper1, sniper2)
# while True:
#     shooter = random.choice(choices)
#     if shooter == sniper1:
#         shot = sniper2
#     else:
#         shot = sniper1
#       
#     print(f'shooter {shooter.name} is shooting {shot.name}, has {shot.health}')
    
#     if sniper1.health == 0:
#         print(f'{sniper1.name} is dead. {sniper2.name} win')
#         break
#     elif sniper2.health == 0:
#         print(f'shooter {shooter.name} is shooting {shot.name}, has {shot.health}')
#         break
#     else:
#         continue
# from collections import Counter
# class Hogwarts:
#     Griffindor = 'Griffindor'
#     Ravenclaw = 'Ravenclaw'
#     Hufflepuff = 'Hufflepuff'
#     Slytherin = 'Slytherin'
#     def __init__(self, courage, intelligence, justice, ambition):
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition
        
#     def sorting_hat(self):
#         res = max(self.courage, self.intelligence, self.justice, self.ambition)
#         if self.courage == self.intelligence and self.courage == self.justice and self.courage == self.ambition:
#             return 'Only one character'
#         if res == self.courage:
#             return f'{self.courage} Идет в Грифендор'
#         elif res == self.intelligence:
#             return f'{self.intelligence} Идет в Равенклав'
#         elif res == self.justice:
#             return f'{self.justice} Идет в Хуфлепув'
#         else:
#             return f'{self.ambition} Идет в Слизерин'
        
        
                

# harry = Hogwarts(100,100,10,99)
# print(harry.sorting_hat())


