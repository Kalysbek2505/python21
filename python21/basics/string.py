"=================Строки====================="
# строки - тип данных, который предназначен для хранения текста 
# или для последовательности символов, заключенного в одинарные или в двойные
# Синтаксис:
from fileinput import _HasReadlineAndFileno
from turtle import st


string1 = "строка с одинарными ковычками"
string2 = "строка с двойными ковычками"
#error = 'не правильная строка"
string3 = "Dont't" # потому что внутри двойных ковычек все одинарные это просто символы
string4 = '"makers bootcamp"' 
print (string3, string4)
string5 = '''
Многострочный текст в одинарных ковычках
Тут можно ставить 'любые' "ковычки"
'''
string6 = """
Многострочный текст в одинарных ковычках
Тут можно ставить 'любые' "ковычки"
"""



"=============Экранизация==============="
# экранизация спец символов
"\n" # это у нас перенос на новую строку
"\t" # это у нас табуляция
"\\"# отоброжения (потому что он является инструкцией, котороя влияет на наш код)
"\'" # отображения '
"\r" # возвращение каретки в начале строки
"\v" # перенос на новую строку со смещением в право на длину предыдущей строки

"hello\nworld"
# hello
# world

'hello\tworld'
# hello   world

'что бы экранизировать нужен символ\\'
# что бы экранизировать нужени символ\\


'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello\vworld'
# _hello
        # world



"==============Форматирование строк=================="
title = 'Плов'
price = 1500

format1 = f"Название: {title}, Цена; {price}"
# Название Плов Цена 1500

format2 = 'Название: %s, Цена: %s'
print(format2 % ('Гуляш', '250'))
print(format2 % ('Cfvcs', '70'))

format3 = 'Наззвание: {}, Цена: {}'
print(format3.format('Шакарап', '35'))


"========Методы строк=========="
# Методы типов данных - функции к которым мы обращемся через точку
dir(str) # посмотреть все методы класса


'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase() # 'hELLO'
'hello world'.title() # 'Hello World'
'hello world'.capitalize() #'Hello world'
"hello".center(11) # '  hello
'hello'.count("l") # 2
"hello".count('ll') # 1
'hello'.count('w') # 0
'hello world'.startswith('hell') # True
'hello world'.endswith('ld') # True
'Hello world'.startswith('h') # False


'hello world'.find(' ') # 5
'hello world'.find('o') # 4
'hello world'.find('wo')# 6
'hello world'.find('hello') # 0
'hello world'.split() # ['hello', 'world']
'hello world'.split('o')#['hell', 'w', 'rld']
'$'.join(['hello', 'world']) # 'hello$world'
' '.join(['hello', 'world']) # 'hello world'
''.join(['hello', 'world']) # 'helloworld'
 
 # конкатенация - склеивание строк
 "hello" + 'world' #'helloworld'
 'hello' + ' ' + 'world' #'helloworld'



"=============Индексы==================="
# индекс это порядковый номер в строк
'hello world'
# 0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] #'h'
string[10]#'d'
string[5] #" "


#срезы  это подстрока строки
string[0:5] # 'hello'
string[0:6] # 'hello'
string[2:4] # 'll'
string[0:11:2] #'hlowrd'
string[::-1]# 'dlrow olleh'
string == string[::-1]




"============Доп инфа===================" 
 a = 5
 b = 5
 print(id(a))
 print(id(b))

  




