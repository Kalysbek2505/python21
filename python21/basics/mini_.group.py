import random
number = 1 # random.randint(1,11)
choice = 'yes'
name = input('What is your name? ') 
choice = input('Do you want to play? yes/no ').lower()
number_of_tries = 0
while choice == 'yes':
    user_num = int(input())
    number_of_tries += 1
    if number > user_num:
        print('My number is bigger')
    elif number < user_num:
        print('My number is smaller')
    else:
        print('You guessed my number!')
        print(f'You have tried {number_of_tries} times to guess my number!')
        choice = input('Do you want to play? ').lower()
        number_of_tries = 0
else:
    print('Good bye!')