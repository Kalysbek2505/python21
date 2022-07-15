
import sqlite3
# // FOR CREATING RECORDS FUNCTION DEFINITION

from models import Cars

def create():
    try:
        Cars(str(input("Введите марку: ")), str(input("Введите модель: ")), int(input("Введите год выпуска: ")), round(float(input("Введите обьем двигателя: ")),1), str(input("Укажите цвет: ")), input("Укажите тип кузова\n*седан\n*универсал.купе\n*хэтчбэк\n*минивен\n*внедорожник\n*пикап\n====================\n "), int(input("Введите пробег: ")), round(float(input("Введите цену: ")),2))
        con = sqlite3.connect("xacaton/data.db")
        cursor = con.cursor()
        while True:
            print('*' * 40)
            for o in Cars.objects:
                data = (o.marka, o.model, o.year, o.engine_volume, o.color, o.cusov, o.probeg, o.price,)
            print('*' * 40)
            query = "INSERT into USERS (marka, model, year, engine_volume, color, cusov, probeg, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, data)
            con.commit()
            ch = input("Do You want to Add More Records(Y/N): ")
            if ch == "N" or ch == "n":
                cursor.close()
                break
            else:
                pass
    except:
        print("Error in Record Creation")

# FOR READING ONE RECORD FUNCTION DEFINITION
def read_one():
    con = sqlite3.connect("xacaton/data.db")
    cursor = con.cursor()
    ids = int(input("Enter Your ID: "))
    query = "SELECT * from USERS WHERE id = ?"
    result = cursor.execute(query, (ids,))
    if (result):
        for i in result:
            print('*' * 40)
            print(f"Марка: {i[1]}")
            print(f"Модель: {i[2]}")
            print(f"Год выпуска: {i[3]}")
            print(f'Объем двигателя: {i[4]}')
            print(f"Цвет: {i[5]}")
            print(f"Тип кузова: {i[6]}")
            print(f"Пробег: {i[7]}")
            print(f'Цена: {i[8]}')
            print('*'*40)
    else:
        print("Roll Number Does not Exist")
        cursor.close()

# FOR READING ALL RECORDS FUNCTION DEFINITION
def read_all():
    con = sqlite3.connect("xacaton/data.db")
    cursor = con.cursor()
    query = "SELECT * from USERS"
    result = cursor.execute(query)
    if (result):
        print("\n<===Available Records===>")
        for i in result:
            print('*' * 40)
            print(f"Марка: {i[1]}")
            print(f"Модель: {i[2]}")
            print(f"Год выпуска: {i[3]}")
            print(f'Объем двигателя: {i[4]}')
            print(f"Цвет: {i[5]}")
            print(f"Тип кузова: {i[6]}")
            print(f"Пробег: {i[7]}")
            print(f'Цена: {i[8]}')
            print('*' * 40)
    else:
        pass
    
# FOR UPDATING RECORDS FUNCTION DEFINITION
def update():
    con = sqlite3.connect("xacaton/data.db")
    cursor = con.cursor()
    idd = int(input("Enter ID: "))
    marka = input("Введите марку: ")
    model = (input("Введите модель: "))
    year = int(input("Введите год выпуска: "))
    engine_volume = round(float(input('Введите объем двигателя: ')),1)
    color = input("Введите цвет: ")
    cusov = input('Введите кузов (варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): ')
    probeg = int(input('Введите пробег: '))
    price = round(float(input('Введите цену: ')),2)
    data = (marka, model, year, engine_volume, color, cusov, probeg, price, idd,)
    query = "UPDATE USERS set marka = ?, model = ?, year = ?, engine_volume = ?, color = ?, cusov = ?, probeg = ?, price = ? WHERE id = ?"
    result = cursor.execute(query, data)
    con.commit()
    cursor.close()
    if (result):
        print('*' * 20)
        print("Records Updated")
        print('*' * 20)
    else:
        print("Something Error in Updation")

# FOR DELETING RECORDS FUNCTION DEFINITION
def delete():
    con = sqlite3.connect("xacaton/data.db")
    cursor = con.cursor()
    idd = int(input("Enter ID: "))
    query = "DELETE from USERS where ID = ?"
    result = cursor.execute(query, (idd,))
    con.commit()
    cursor.close()
    if (result):
        print("One record Deleted")
    else:
        print("Something Error in Deletion")