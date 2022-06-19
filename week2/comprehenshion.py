#Task 1
# list_ = [val for val in range(1, 101)]
# print(list_)

#Task 2
# list_ = [val for val in range(1, 51) if val % 2 == 1]
# print(list_)

#Task 3
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x for x in list_ if x % 2 ==0 and x > 0]
# print(int_list)

#Task 4
# list_ = [x ** 2 for x in range(1, 26)] 
# print(list_)

#Task 5
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x) for x in str_list]
# print(int_list)

# Task 6
# list_ = [x*x if x % 2 == 0 else x for x in range(1,11)]
# print(list_)
#Task 7
# list_ = [False if i % 2 else True for i in range(1,11)]
# print(list_)
#Task 8
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [ 'shorter' if len(i) <=4 else 'longer' for i in list_name]
# print(new_list)
#Task 10
# n = int(input())
# dict_ = {i: i*i  for i in range(1,501) if i%9==0 }
# print(dict_) 
#Task 11
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {
#     key : list(range(1, value + 1))
#     for key, value in a.items() 
# }
# print(dict_)
#Task 12
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {key:'even'  if value % 2 == 0 else 'odd' for key,value in dict_.items()}
# print(a)
#Task 13
string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_ = [list_ for list_ in str.split(string_) if list_.isdigit()]
print(list_)
#Task 14
# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# new_dict = {key:
#     str(list(({inner_key: inner_value for inner_key, inner_value in value.items() if inner_value == max(list(value.values()))}).keys())).lstrip("['").rstrip("]'")
#     for key, value in dict_.items()``}
# print(new_dict)
#Task15
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {key: val2 for key, val in my_dict.items() for val2 in val.values()}
# print(dict_)
# Task16
# list_ = [x / 2 for x in range(0,11) if x % 2 == 0  ]
# print(list_)
#Task 17
# dict_ = {1:'a', 2:'broo', 3:'re'}
# res = {key:len(val) **3 if key % 2!=0 else len(val) for key,val in dict_.items()  }
# print(res)
#Task
# from random import shuffle
# sa = list(range(1,21))
# sb = list(range(1,21))
# shuffle(sa)
# shuffle(sb)
# a = {sa.pop() for _ in range(10)}
# b = {sb.pop() for _ in range(10)}
# ab = a | b
# n = len(ab)
# print(ab)
# print(f'В этом сете было {20-n} повторения, его длина составляет {n}')

# set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
# full_set = set.union(set1,set2)
# n = len(full_set)   
# print(full_set)
# print(f'В этом сете было {20-n} повторения, его длина составляет {n}')
