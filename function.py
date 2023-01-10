import csv
from telegram import Update
from telegram.ext import CallbackContext
import os.path

db = []
id = 0
    
def init_db(file_name='DB.csv'):
    global db
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    # if(int(row[0]) > id):
                    #     id = int(row[0])
            else:
                open(db_file_name, 'w', newline='').close()
    return None

def show_db(update: Update, context: CallbackContext, file_name='DB.csv'):
    with open(file_name) as f:
        reader = csv.reader(f,delimiter='|')
        headers = next(reader)
        print(headers)
        for row in reader:
            print(row)


def write_db(update: Update, context: CallbackContext):
    global id
    global db
    
    id += 1
    db.append(id)
        
    first_name = input('Введите имя: ')
    if(first_name  == ''):
        print('Поле не может быть пустым!')
        return
    db.append(first_name)
    last_name = input('Введите Фамилию: ')
    if(last_name == ''):
        print('Поле не может быть пустым!')
        return
    db.append(last_name)   
    phone_num = give_int('Введите телефон: ')
    if(phone_num  == ''):
        print('Поле не может быть пустым!')
        return        
    db.append(phone_num)
    comment = input('Введите комментарий: ')
    db.append(comment)

    file = open ('DB.csv', 'a')
    file.write(f'{db[0]}|{db[1]}|{db[2]}|{db[3]}|{db[4]}\n')
    file.close()

def give_int(input_number) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number))  
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

# def creating():
#     file = open ('DB.csv', 'w')
#     # with open (file, 'a') as data_csv:
#     file.write('id | first_name | last_name | phone_num | comment\n')
# creating()
