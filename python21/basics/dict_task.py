#Task 1
# a = {'x': 1, 'y': 2, 'z': 1}
# b = list(a)
# print(b[0])
#Task 2
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.pop('a')
# print(a)
 #Task 3
#  a = {'a': 1, 'b': 2, 'c': 1}
# a['f'] = 55
# print(a)
#Task4
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)
#Task5
# a = {'a': 1, 'b': 2, 'c': 1}
# b = list(a.keys())
# print(b)
#Task 6
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)
#Task 7
# a = {'a': 1, 'b': 2, 'c': 1}
# for i in a:
#     print(i)
#Task 8 
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for k,v in list(a.items):
#     if v % 2 == 0:
#         b.update({k:2})
#     else:
#         b.update({k:v})
# print(b)
#Task 10
# a = {1: None, 2: 'b', 3: None}
# for v in a.copy():
#     if a[v] == None:
#         a.pop(v)
# print(a)
#Task 11
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# temp = dict()
# for key in a:
#     temp[key] = a[key] / 5
# print(temp)
#Task 12
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for v in a.copy():
#     if a[v] % 2 == 0:
#         a.pop(v)
# print(a)
#Task 13
# a = {"a":1,"b":2,"c":3}
# b = {}
# for key,val in a.items():
#     b.update({val:key})
# print(b)
#Task 14
# a = {'a': 3, 'b': 2}
# b = sum(a.values())
# print(b)
#Task 15
# a1 = {'a':1}
# a2 = dict(a = 2)
# a3 = dict({('Russia', 'Moscow')})