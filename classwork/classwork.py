#Classwork 1
# from datetime import datetime


# class Smartphone:
#     def call(self, phone):
#         self.phone = phone
#         print(f'Calling is {self.phone}')
#     def where_to_wear(self):
#         print('You can keep me anywhere')
# class Watch:
#     def see_time(self):
#         print(f'{datetime.now()}')
#     def where_to_wear(self):
#         print('You should wear me on your hand')
# class SmartWatch(Smartphone, Watch):
#     pass
# smart = SmartWatch()
# smart.call(+996705465252)
# smart.where_to_wear()
# smart.see_time()
#Classwork 2
class Proverka:
    def password_proverka(self, username, password):
        
class Instagram(Proverka):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def post_post(self, post_name):
        self.post_name = post_name
        print(f'Post name is {self.post_name}, username {self.username} password: {self.password}')
    
class TikTok(Proverka):
    pass

    