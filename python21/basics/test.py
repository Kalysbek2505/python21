"===================Переменные======================"

# переменные    - это ссылки на ячейке памяти ,где хранятся какие-то данные 

a = int(input())

"=========================Ввод и вывод данных=========================="

# print - функция вывода данных в терминал

# input - функция ввода данных с терминала 

b = int(input())

sum = a + b

print ('равно:', sum)

# integers(int) - целые числа (3 34 445 2 -4 )

a = 6

# float - вещественные (с плавающей точкой) (2.434 4.45435 12234.34)

b =10.2

# desimal - точное вещественное число

# чтобы использовать decimal нужно его импортировать 

from decimal import Decimal
c = Decimal(0.1)

# complex - комлексные числа 

complex (1,5)

"=======================операция над числами=========================="

# 5 + 5 сложение 

# 10 - 3 вычитание 

# 2 * 3 умножение
 
# 15 / 3 деление (flaot 5.0)

# 15 // 2 целочисленое деление (int 7)

# 5 % 2 остаток от деления (int 1)

# 5  2 возведение в степень 

# 25  0.5 квадратный корень числа


# модуль числа - из отрицательного числа сделает положительное 

abs (-5) # 5

# pow:
# 1. возводит число в определенную степень
 
# 2. возвращяет остаток от деления результата действия на третье число 

pow(2, 3) # 8 = 2  3

pow(2, 3, 4) # 8 % 4 = 0

# (2  3) %  4 - 0

#  divmod - функция которая принимает два числа и возвращяет два числа , где первое - это целая часть а второе - остаток от деления 

divmod (15/ 2) # 7, 1

divmod (9 / 3) #3, 0

# round - функция которая округляет число

round (5.6) # 6 

round (4.4) # 4

round (5.49) # 5 (берет первое число после точки)
# можно указать сколько цифр после запятой оставить

round (10.0475, 3) # 10.048

round (10.0474, 3) # 10.047

# sqrt - функция для нахождения корня из числа
# для работы надо ее импортировать из библиотеки math

from math import sqrt 

sqrt (36) # 6 

sqrt (25) # 5

