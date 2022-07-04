import permissions


class Category:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

class Product:
    def __init__(self, title, price, description, quantity):
        self.title = title
        self.price = price
        self.desc = description
        self.quantity = quantity
    def __str__(self):
        return (f'{self.title} [{self.quantity}] - ${self.price}\n({self.desc[:20]})')
class Comment:
    def __init__(self, user, product, body):
        permissions.login_requered(user)
        from datetime import datetime
        self.user = user
        self.product = product
        self.body = body
        self.created_at = datetime.now()


class User:
    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex    
        self.__password = None
        self.is_authenticated = False
        print(f'sucsess {self.email}')
    def register(self, password, password_confrim):
        if password != password_confrim:
            raise Exception('Пароли не совпадают')
        self.__password = password
        print(f'registed {self.email}')
    
    def login(self, password):
        if self.__password != password:
            raise Exception('Пароли не верны')
        self.is_authenticated = True
        print(f'login {self.email}')    
    def logout(self):
        permissions.login_requered(self)
        self.is_authenticated = False


    def __str__(self):
        return self.email