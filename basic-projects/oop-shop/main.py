from models import User, Product, Comment


user1 = User('test@gmail.com', 'hello', 'female')
user1.register('12345678', '12345678')
user1.login('12345678')
print(user1.is_authenticated)
user1.logout()
print(user1.is_authenticated)


product1 = Product('Iphone 10', 123456, '......', 10)
comment1 = Comment(user1, product1, 'goluboi')
print(comment1)