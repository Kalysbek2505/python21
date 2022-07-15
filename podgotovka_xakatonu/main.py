items = {}
shoppingdict = {}
# Добро пожаловать


username = input('Введите имя: ')
messagewel = f'Добро пожаловать в мой магазин {username}'
lenmsg = len(messagewel)
print('*'* lenmsg)
print(messagewel)
print('*'*lenmsg)

with open('podgotovka_xakatonu/grocery.txt') as file:
    # file_line = file.readline()
    items_file = file.readlines()
    # print(items_file)

    print('************Products***************')
    for item in items_file:
        item_name = item.split()[0]
        item_price = item.split()[1]
        print(f'{item_name}: {item_price}')
        items.update({item_name: item_price})
    # print(items)
    print('*'* 40)
processshop = input('Будешь покапать что-то Да/Нет')
if processshop.lower() == 'yes':
    item_add = input('Добавь вещь')
    if item_add in items:
        item_qty = int(input('Добавь количество: '))

    else:
        print('Нете такого товара')
else:
    print('Окей пока')

