import csv

db = []
id = 0
    
def init_db(file_name='DB.csv'):
    global db
    db_file_name = file_name
    db.clear()

    with open(db_file_name, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if(row[0] != 'ID'):
                db.append(row)
                if(int(row[0]) > id):
                    id = int(row[0])

def show_db(file_name='DB.csv'):
    with open(file_name) as f:
        reader = csv.reader(f,delimiter='|')
        headers = next(reader)
        print(headers)
        for row in reader:
            print(row)

def write_db():
    global id
    global count
    input_data = []
    
    id =+ 1
    input_data.append(id)

    first_name = input('Введите имя: ')
    if(first_name  == ''):
        print('Поле не может быть пустым!')
        return
    input_data.append(first_name)
    last_name = input('Введите Фамилию: ')
    if(last_name == ''):
        print('Поле не может быть пустым!')
        return
    input_data.append(last_name)   
    phone_num = give_int('Введите телефон: ')
    if(phone_num  == ''):
        print('Поле не может быть пустым!')
        return        
    input_data.append(phone_num)
    comment = input('Введите комментарий: ')
    input_data.append(comment)

    file = open ('DB.csv', 'a')
    file.write(f'{input_data[0]}|{input_data[1]}|{input_data[2]}|{input_data[3]}|{input_data[4]}\n')
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
