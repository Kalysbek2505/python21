from decimal import Decimal
while True:
    number = int(input('Введите первое значение: '))
    number2 = int(input("Введите второе значение: "))
    values = input('Введите операцию из следующих: + - * / % //: ')
    if values == '+':
        number1 = number + number2
        print(number1)
    elif values == '-':
        number1 = number - number2
        print(number1)
    elif values == '*':
        number1 = number * number2
        print(number1)
    elif values == '/':
        number1 = number / number2
        print(number1)
    elif values == '%':
        number1 = number % number2
        print(number1)
    elif values == '//':
        number1 = number // number2
        print(number1)
    elif values == '**':
        number1 = number ** number2
        print(number1)    
    elif number == 'stop':
        break    
    else:
        print('Данной операции нет в системе')
    