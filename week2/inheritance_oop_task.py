#Task 1
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass
# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass
# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()
#Task 2
# class A:
#     def method1(self):
#         print('Основной функционал')
# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')
# obj = B()
# obj.method1()           

#Task 3 
# class MyString(str):
#     def init(self,value):
#         self.value = value
    
#     def str(self):
#         return self.value

#     def append(self,string):
#         self.value += string
#         return self.value

#     def pop(self):
#         re = self.value[-1]
#         self.value = self.value[:-1]
#         return re
    

# example = MyString('String') 
# example.append('hello')
# print(example.pop()) 
# print(example)

#Task 4
# class MyDict(dict):
#     def get(self, key, default = 'Are you kidding?'):
#         return dict.get(self, key, default)
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))

#Task 5
# class Person:
#     def __init__(self, name, age,):
#         self.name = name
#         self.age = age
#     def display(self):
#         return (f'name:{self.name}, age:{self.age}')
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         self.faculty = faculty
#         super().__init__(name, age)
#     def display_student(self):
#         debil = super().display()
#         return f'{debil}, faculty:{self.faculty}'
# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())@#$%^&*()_+-=;,./?[]{}
#Task 6
# class ContactList(list):
#     def __init__(self,list_):
#         self.list_ = list_
#     def search_by_name(self,name):
#         a = []
#         for i in self.list_:
#             if name in i:
#                 a.append(i)
#         return a
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))

#Task 7
# from datetime import datetime
# class SmartPhones:
#     def __init__(self,name,color,memory,battery = 0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0
#     def __str__(self):
#         return f'{self.name} {self.memory}'
#     def charge(self,per):
#         self.battery = per + self.battery

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name,color,memory)
#         self.ios = ios
#     def send_imessage(self,sending):
#         return f'sending {sending} from {self.name} {self.memory}'

# class Samsung(SmartPhones):
#     def __init__(self,name,color,memory,android):
#         super().__init__(name,color,memory)
#         self.android = android
#     def show_time(self):
#         x = datetime.now().time()
#         return x
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())

#Task 8
# class CustomError(Exception):
#     def __init__(self, letters):
#         self.letters = letters

# def check_letters(debil):
#     if debil.isupper():
#         return f'ВСЕ ОТЛИЧНО! {debil}'
#     else:
#         raise capitals_error
    

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
# print(check_letters('HELLO'))

class ToDo:
    instances = {}
    def __init__(self, delo):
        self.delo = delo
    def give_priority(self, priority):
        ToDo.instances.update({priority: self.delo})
    def list_of_tasks(self):
        res = list(self.instances.items())
        res.sort(key = lambda delo: delo[0])
        return res  
todo1 = ToDo('Сходить в кино')
todo2 = ToDo('Сделать домашку')
todo3 = ToDo('Выгулять собаку')
todo1.give_priority(3)
todo2.give_priority(1)
todo3.give_priority(2)
print(ToDo.instances)
print(todo1.list_of_tasks())

