#Task 1
# list_ = [1, 2, 3, 4]
# result = sum(list_)
# print(result)
#Task 2
# list_ = [1, 5, -9, 6, -4] 
# result = all(i>3 for i in list_)
# print(result)
#Task 3
# list_ = [5, 8, 4, 6, 7]
# result = any(x< 0 for x in list_)
# print(result)
#Task 4
# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x*x, list_))
# print(result)
#Task 5
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x%2 == 0, list_))
# print(result)
#Task 6
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)
#Task 7
# from functools import reduce
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x, y: x*y,  list_)
# print(result)
#Task 8
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# list2 = len(list(filter(lambda x: x%2 == 0, list_)))
# list3 = len(list(filter(lambda x: x%2 == 1, list_)))
# result = (f'even: {list2}, odd: {list3}')
# print(result)
#Task 9
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: x>0, list_))
# print(result)
#Task 10
# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John']
# def names(a,b):
#     if len(a) > len(b):
#         return a
#     else:
#         return b
# result = (reduce(names, list_ ))
# print(result)



