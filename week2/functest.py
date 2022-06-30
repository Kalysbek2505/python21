
# while True:
#     def translate(string):
#         eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#         ru = "йцукенгшщзхъфывапролджэячсмитьбю"
#         if string[0] == eng:
#             dictionary = str.maketrans(eng, ru)
#         else:
#             dictionary = str.maketrans(ru,eng)
#         return string.translate(dictionary)
#     print(translate(input('Введите слово')))



# Task 1
# def mul(x, z):
#     return x + z 
#     print(mul)
#Task 2
# def get_string_length(x):
#     return len(x)
# print(get_string_length('hello'))
#Task 3
# def get_type(a, b):
#     print(type(a)) 
#     print(type(b))
# print(get_type(5, 's'))
#Task 4
# def divide(a, b):
#     return a / b
# print(divide(5, 10)) 
#Task 5
# dict_ = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# def dictionary(dict_):
#     for i in dict_:
#         print(i)
# dictionary(dict_)
#Task 6
# num = 6
# def check(num):
#     if num % 2 == 0:
#         return 'It is even number'
#     else:
#         return 'It is odd number'
        
# print(check(num))
#Task 7
# def is_palindrome(x):
#     if (x.lower() == x[::-1].lower()):
#         return (True)
#     else:
#         return (False)
# print(is_palindrome('Mom'))
#Task 8
# def max_num(a, b):
#     return max(a,b)
# print(max_num(4,2))
#Task 9
# def multiply_list(x):
#     a = 1
#     for i in x:
#         a *= i
#     return a
# print(multiply_list([1,2,3,4,5,6]))
#Task 10
# def sum_digits(x):
#     b = 0
#     for i in str(x):
#         b += int(i)
#     return b
# print(sum_digits(105))
# classwork  
  
# import random
# def generate_password(a, b):
#     ran = random.sample(range(1, 11), k=7)
#     ran = [str(i) for i in ran]
#     res = a + b + ''.join(ran)
#     return res

# def get_info(name = input(),pas = input()):
#     res = generate_password(a = name, b = pas)
#     return res

# print(get_info())
from audioop import add


def plus(a, b):
    return a + b
def delen(a,b):
    return a / b
def proiz(a,b):
    return a * b
def minus(a,b):
    return a - b
print('1 плюс')
print('2 деление')
print('3 Умножение')
print('4 Миинус')

value = input('Выбери от 1 до 4')
val1 = int(input())
val2 = int(input())
if value == '1':
    print(val1, '+', val2, '=', plus(val1, val2))
if value == '2':
    print(delen(val1, val2))
if value == '3':
    print(proiz(val1, val2))
if value == '4':
    print(minus(val1, val2))
def get_info():
    val1 = int(input())
    val2 = int(input())
    operation = input()
    if operation == '+':
        print(val1 + val2)
    elif operation == '-':
        print(val1 - val2)
    elif operation == '*':
        print(val1 * val2)
    elif  operation == '//':
        print(val1 // val2)
get_info()