#Task1
# def foo():
#     var = 'переменная foo' 
#     def bar():
#         global var
#         var = 'переменная bar'
        
 
#     bar()
#     print('переменная в foo: ', var)
# foo()
# print('переменная в foo: ', var)
#Task 2
# x = 'Я глобальная переменная!'
# print(x)
# def my_func():
#     global x
#     x = 'Я могу изменяться'
#     print(x)
# my_func()
# print(globals())
#Task 3
# num = 3 
# def mul():
#     global num
#     num = num **2
# mul() 
# mul()
# mul()
# print(num)    
#Task 4
# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount
# def pay_bills(amount,log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
# def get_balance():
#     print(f'У вас на счету {balance} сом ')
# get_salary(1000)
# get_balance()
# pay_bills(300,'интернет')
# get_balance()
#Task 5
# result = 0
# def pow_first(x,y):
#     global result
#     result = x**y
# def pow_second(z):
#     global result
#     result = result % z
# pow_first(2,3)
# pow_second(3)
# print(result)
#Task 6
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def ages():
#     global a
#     for k,v in a.items():
#         if v < 17:
#             print(f'{k}, извините, Вы не проходите по age-control')
#         else:
#             print(f'{k}, Вы можете войти в клуб')
# ages()
#Task 7
# a = ['pipi', 'papa', 'mama']
# b = []
# def titles():
#     global a
#     for i in a:
#         b.append(i.title())
# titles()
# print(b)
#Task 8
# def count_symbols(string):
#     ae = 0
#     bd = 0
#     sym = 0
#     for i in string.lower():
#         if i in 'йуеыаоэяиюё':
#             ae += 1
#         elif i in 'цкнгшщзмчвфжрлдтсп':
#             bd += 1
#         else:
#             sym += 1
#     return(f'Количество гласных: {ae} , согласных: {bd} , остальных символов: {sym}')
# print(count_symbols('Мурат супер!'))
#Task 9
# a = list()
# def sym():
#     global a
#     for i in range(11):
#         a.append(i)
#     print(a)    
# sym()
#Task 10
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def sym():
#     for i in a:
#         if i < 7:
#             print(i)
# sym()
from pathlib import Path
from pprint import pprint

def searching_all_files(directory):
    dirpath = Path(directory)
    file_list = []
    for x in dirpath.iterdir():
        if x.is_file():
            file_list.append(x)
        elif x.is_dir():
            file_list.extend(searching_all_files(x))
    return file_list

pprint(searching_all_files('.'))

# import os

# for root, dirs, files in os.walk("."):
#     for filename in files:
#         print(filename)

from pathlib import Path
root_directory = Path(".")
for path_object in root_directory.glob('**/*'):
    if path_object.is_file():
        print(f"hi, I'm a file: {path_object}")
    elif path_object.is_dir():
        print(f"hi, I'm a dir: {path_object}")

