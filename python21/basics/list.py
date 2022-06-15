'===============List===================='
#списки - изменяемый, индексируемый, упорядоченный, итерируемый тип данных предназначенный для хранения данных в определленном спис
list  = [1, 2, 3, 4, 'Hello', [0.1, 2] {'a': 3}]
list = [1] #2
list [4] #[0.1, 2]
list [4][0]#0.1
list[3][0] #h
list [-1]['a'] # 3
'===============Создание списков======================'
list = [1,2,3]
list2 = list('Hello') # ['h', 'e', 'l', 'l', 'o']
'================Методы списков=================='
# append добавляет элемент в конец списка
list = []
list.append(1)
print(list) #[1]
list.append('hello')
print(list)#[1, 'hello']
# clear очищает список
list.clear()
print(list)# []
list[1,2,3,4,5,6,1,2,1,]
list.count(1) # 3
list.count(2)#  2
list.count(4)# 1
list = ['hello', 'hello', 'hello']
list.count('h') # 0
list.count('hello')
len(list) # 3
list[[1,2,3,]4,5,6,[1,2,1,]]
len(list) # 6
# extend добавляет элементы второго списка в первый, изменяя первый
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1) # [1,2,3,4,5,6]
print(list2) # [4,5,6]

# index возвращает индекс первого вхождения принятого элемента
list1 = [1,2,3,4,1,2,3,5,4,1]
list1.index(3) # 2
list1.index(1) # 0

# insert добавляет элемент по индексу list.insert(index, obj)
list_ = [1,2,3]
list_.insert(0, "hello")
print(list_) # ["hello", 1, 2, 3]
list_.insert(2, 10) 
print(list_) # ["hello", 1, 10, 2, 3]
list_.insert(100, "bye")
print(list_) # ["hello", 1, 10, 2, 3, "bye"]

# pop удаляет элемент из списка по индексу и результатом отработанного метода будет удалененый элемент
list_ = [1,2,3,4,5,6,7]
popped = list_.pop()
print(list_, popped) # [1,2,3,4,5,6]  7
popped = list_.pop(1)
print(list_, popped) # [1,3,4,5,6]  2

# remove удаляет первый принятый элемент в списке
list_ = [1,2,34,1,2,3,1,2,4,1,2,6]
list_.remove(2)
print(list_) # [1, 3, 1, 2, 3, 1, 2, 4, 1, 2, 6]
print(str(list_))

# reverse изменяет список, расставляя его элементы в обратном порядке
list_ = [1,2,3,4,5]
list_.reverse()
print(list_) # [5,4,3,2,1]
new_list = list_[::-1] # [1,2,3,4,5]

# sort сортирует список, состоящий из элементов одного типа данных в возрастающем порядке (алфавитном для строк)
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort()
print(list_) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = ['a', 'c', 'd', 'b', 'f', 'e', 'A', 'C', 'B']
list_.sort()
print(list_) # ['A', 'B', 'C', 'a', 'b', 'c', 'd', 'e', 'f']

list_ = [1,2,3,'hello'] # TypeError: '<' not supported between instances of 'str' and 'int'
list_.sort()

# reverse=True сортирует по убыванию
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort(reverse=True) # [10,9,8,7,6,5,4,3,2,1]
