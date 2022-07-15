"======================Class, static, instance methods=========================="
# instance метод - метод ,который принимает первым аргументом self(обьект). Вызываем instance методы у обьекта 

from attr import s


class A:
    def instance_method(self,):
        print("метод обьекта")
    
obj = A()
obj.instance_method() # вызываем у обьекта, и он автоматически пропадает как аргрумент в метод  
A.instance_method(obj) # вызываем у класса, нужно передать обьект


# class methods - метод, который принимает первым аргументом cls (класс).чтобы создать метод класса, нужно задекорировать @classmethod 

class A:
    @classmethod
    def class_method(cls):
        print(cls)
        print("метод класса")

A.class_method()
A().class_method()

class Pizza:

    def __init__(self, radius, *ingridients):
        self.ingridients = ingridients
        self.r = radius
    
    def cook(self):
        print(f'Пицца размером {self.r} см\nИнгредиенты\n{self.ingridients}')

    @classmethod
    def pepperoni(cls, r):
        return cls(r, "Пеперони", "Помидоры")

    @classmethod
    def four_cheeze(cls, r):
        return cls(r, "Моцарелла", "Дор Блю", "Сыр", "Сырчик")



pizza1 = Pizza(30, 'сыр', 'помидор', 'грибы')
pizza2 = Pizza.pepperoni(30)
pizza3 = Pizza.pepperoni(35)
pizza4 = Pizza.four_cheeze(30)
pizza5 = Pizza.four_cheeze(40)
pizzas =  [pizza1, pizza2, pizza3, pizza4, pizza5]
for pizza in pizzas:
    pizza.cook()

# stasic method просто функции внутри класса которые не взаимодецствуют ни с классом ни с объектом

class Square:
    def __init__(self, a):
        self.a = a
        self.s = self.get_s(a)

    @staticmethod
    def get_s(a):
        return a ** 2

obj = Square(4)
print(obj.s)
