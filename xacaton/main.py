
from views import create, read_one, read_all, update, delete
# MAIN BLOCK
def main_block():
    try:
        while (True):
            print("1). Create Records: ")
            print("2). Read Records: ")
            print("3). Update Records: ")
            print("4). Delete Records: ")
            print("5). Exit")
            ch = int(input("Enter Your Choice: "))
            if ch == 1:
                create()
            elif ch == 2:
                print("1). Read Single Record")
                print("2). Read All Records")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    read_one()
                elif choice == 2:
                    read_all()
                else:
                    print("Wrong Choice Entered")
            elif ch == 3:
                update()
            elif ch == 4:
                delete()
            elif ch == 5:
                break
            else:
                print("Enter Correct Choice")
    except:
        print("Database Error")
main_block()


