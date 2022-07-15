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
        if self.username == username and self.password == password:
            print('successfully createed')
        else:
            print('ERROR')
class Instagram(Proverka):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.count = 0
    def post_post(self, post_name, username, password):
        super().password_proverka(username, password)
        self.count += 1 
        print(f'Post name is {post_name}, username {self.username} password: {self.password}')
    
class TikTok(Proverka):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.count = 0
    def post_video(self, video, username, password):
        super().password_proverka(username, password)
        self.count += 1
        print(f'New Video {video}, username:{self.username}, password:{self.password}')
obj1 = Instagram('goodboy', 'ewq')
obj1.post_post('kal', 'goodboy', 'eq')
print(obj1.count)
obj2 = TikTok('rew', 'wq')
obj2.post_video('werw', 'rew', 'wq')
print(obj2.count)



    