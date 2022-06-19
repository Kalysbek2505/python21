#Task2
# try:
#     b = 10
#     c = 11
# except:
#     print("Нет такой переменной")
# else:
#     print(a)
#Task 3
# try:
#     num1 = int(input())
#     num2 = int(input())
#     num3 = num1/num2
# except:
#     print('На ноль делить нельзя')
# else:
#     print(num3)
#Task 4
# try:
#     num1 = int(input())
#     num2 = int(input())
#     num3 = num1+num2
# except:
#     print('Введите число!')
# else:
#     print(num3)
#Task 5
# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'} 
#     print(dict_['key3'])   
# except:
#     print('Нет такого ключа!')
#task 6
# try:
#     list_ = [1, 4, 9, 16, 25, 36] 
#     print(list_[11])
# except:
#     print('Нет такого элемента!')
#Task 7
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('ValueError Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

#Task 8 
# try:
#     num1 = int(input())
#     num2 = int(input())
#     num3 = num1/num2
#     print(num3)
# except:
#     print('Произошла ошибка!')
#Task 9 
# cash = int(input())
# if cash < 0: 
#     raise ValueError('Сумма не может быть отрицательной!')   
# else:
#     print(cash)
# Task 10
# try:
#     inp1 = input()
#     inp2 = input()
#     if type(int(inp1))  == int and type(int(inp2)) == int:
#         print(int(inp1)+int(inp2))  
# except:
#      if type(str(inp1))  == str and type(str(inp2)) == str:
#         print(str(inp1)+str(inp2))
#Task11

inp1 = input()
list_ = [list1 for list1 in str.split(inp1) if list1.isdigit()]
print(list_)
if inp1 == list_:
    raise("Данный элемент не является числом")
