'==============Полиморфизм=================='
# Полиморфизм - принцип ООП в котором методы в разных классах называется одинаково. (один интерфейс - разный функционал)

class Dog:
    def speak(self):
        print('gav-gav')

class Cat:
    def speak(self):
        print('may-may')

class Frog:
    def speak(self):
        print('kva-kva')

animals = [Cat(), Dog(), Frog(), Dog()]

for animal in animals:
    animal.speak()        

print(dir(list))
print(dir(str))
print(dir(dict))
