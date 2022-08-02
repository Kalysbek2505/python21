
from views import create, read_one, read_all, update, delete
#MENU
def menu_block():
    try:
        while (True):
            print("1). Create: ")
            print("2). Read: ")
            print("3). Update: ")
            print("4). Delete: ")
            print("5). Exit")
            ch = int(input("ВЫБЕРИ ЧТО ТЫ ХОЧЕШЬ СДЕЛАТЬ: "))
            if ch == 1:
                create()
            elif ch == 2:
                print("1). ЧИТАЕТ ТОЛЬКО ОДИН")
                print("2). ЧИТАЕТ ВСЁ")
                choice = int(input("ВЫБЕРИ ЧТО ТЫ ХОЧЕШЬ СДЕЛАТЬ: "))
                if choice == 1:
                    read_one()
                elif choice == 2:
                    read_all()
                else:
                    print("ОШИБКА ПРИ ВЫБОРЕ")
            elif ch == 3:
                update()
            elif ch == 4:
                delete()
            elif ch == 5:
                break
            else:
                print("ОШИБКА ВЫБОРЕ")
    except:
        print("ОШИБКА БАЗЫ ДАННЫХ")
menu_block()


