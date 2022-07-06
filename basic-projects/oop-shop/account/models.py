import permissions

class User:
    objects = []
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
        User.objects.append(self)
    
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