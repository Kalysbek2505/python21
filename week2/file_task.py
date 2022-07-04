#Task 1
# lines = open('task1.txt', 'r')
# for line in lines.readlines(9):
#     lines.close()
#     print(line)

#Task2 
# p = open('task2.txt')
# for line in p:
#     print(line)
# p.close()

#Task3
# with open('task3.txt', 'w+') as file:
#     for num in range(10):
#         str_ = str(num) + '*'
#         file.write(str_)
#     file.seek(0)
    
#     print(file.read())
#Task4
# with open('task4.txt', 'r') as file:
#     b = file.readlines()
#     print(len(b))
#Task5 
# with open('task5.txt') as file:
#     num = [int(i) for i in file]
#     with open('task6.txt', 'w') as file1:
#         file1.write(f'{min(num)}-{max(num)}')
        
"""
1) Создайте файл numbers.txt и напишите скрипт, который запишет в этот файл числа от 1 до 20. Затем создайте файл squares.txt. Напишите скрипт, который будет считывать числа из файла numbers.txt и записывать квадраты этих чисел в файл squares.txt
"""
# with open('numbers.txt', 'w+') as file:
#   num = []
#   for i in range(1,21):
#     num.append(i)
#   file.write(str(num))
#   file.seek(0)
#   print(file.read())
# with open('squares.txt','w+') as file1:
#   b = [int(i) ** 2 for i in num]
#   print(b)


"""
2) Создайте файл usernames.txt. Напишите скрипт, который будет запрашивать у пользователя имена, а эти имена будут помещаться в файл usernames.txt. При этом напротив каждого имени будет записано количество букв в юзернейме. Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
"""
# with open('username.txt', 'w+') as file:
#   while True:
#     username = input()
#     b = len(username)
#     file.write(username)
#     file.write(str(b))