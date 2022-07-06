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
