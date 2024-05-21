import sqlite3

#contants and variables
DATABASE = "airplanes.db"

#functions

def print_all_airplanes():
    '''print all the airplanes'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM airplanes'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<30}{airplane[2]:<8}{airplane[3]:<8}{airplane[4]:<8}{airplane[5]:<8}{airplane[6]:<8}{airplane[7]:<8}{airplane[8]:<8}')
    db.close()

def print_all_airplanes_by_wingspan():
    '''print all the airplanes sorted by wingspan'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM airplanes ORDER BY wingspan DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<30}{airplane[2]:<8}{airplane[3]:<8}{airplane[4]:<8}{airplane[5]:<8}{airplane[6]:<8}{airplane[7]:<8}{airplane[8]:<8}')
    db.close()

def print_all_airplanes_by_length():
    '''print all the airplanes sorted by length'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM airplanes ORDER BY length DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<30}{airplane[2]:<8}{airplane[3]:<8}{airplane[4]:<8}{airplane[5]:<8}{airplane[6]:<8}{airplane[7]:<8}{airplane[8]:<8}')
    db.close()

def print_all_airplanes_by_max_speed():
    '''print all the airplanes sorted by max speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM airplanes ORDER BY max_speed DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<30}{airplane[2]:<8}{airplane[3]:<8}{airplane[4]:<8}{airplane[5]:<8}{airplane[6]:<8}{airplane[7]:<8}{airplane[8]:<8}')
    db.close()

def print_all_airplanes_by_max_range():
    '''print all the airplanes sorted by max range'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM airplanes ORDER BY max_range DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<30}{airplane[2]:<8}{airplane[3]:<8}{airplane[4]:<8}{airplane[5]:<8}{airplane[6]:<8}{airplane[7]:<8}{airplane[8]:<8}')
    db.close()

def print_all_airplanes_by_max_passenger():
    '''print all the airplanes sorted by max passenger'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM airplanes ORDER BY max_passenger DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<30}{airplane[2]:<8}{airplane[3]:<8}{airplane[4]:<8}{airplane[5]:<8}{airplane[6]:<8}{airplane[7]:<8}{airplane[8]:<8}')
    db.close()

def print_all_airplanes_by_max_fuel():
    '''print all the airplanes sorted by max fuel'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM airplanes ORDER BY max_fuel DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<30}{airplane[2]:<8}{airplane[3]:<8}{airplane[4]:<8}{airplane[5]:<8}{airplane[6]:<8}{airplane[7]:<8}{airplane[8]:<8}')
    db.close()

#main code/user input
while True:

    user_input = input(
"""
What would you like to do.
1. Print all airplanes
2. Print all airplanes sorted by wingspan
3. Print all airplanes sorted by length
4. Print all airplanes sorted by max speed
5. Print all airplanes sorted by max range
6. Print all airplanes sorted by max passenger
7. Print all airplanes sorted by max fuel
8. Exit
""")
    try:
        if user_input == '1':
            print_all_airplanes()
        elif user_input == '2':
            print_all_airplanes_by_wingspan()
        elif user_input == '3':
            print_all_airplanes_by_length()
        elif user_input == '4':
            print_all_airplanes_by_max_speed()
        elif user_input == '5':
            print_all_airplanes_by_max_range()
        elif user_input == '6':
            print_all_airplanes_by_max_passenger()
        elif user_input == '7':
            print_all_airplanes_by_max_fuel()
        elif user_input == '8':
            break
        else:
            print('That was not an option\n')
    except:
        print('That was not an option\n')



