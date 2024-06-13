import sqlite3

# importing in colorama to add color to the printed data 
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# contants and variables
DATABASE = "airplanes.db"



# functions

# function 1
def print_all_airplanes():
    '''print all the airplanes'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print all airplanes information 
    sql = 'SELECT * FROM airplanes'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color
    print(Fore.BLUE + f'model                      wingspan  length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(Fore.GREEN + f'{airplane[1]:<27}{airplane[2]:<10}{airplane[3]:<8}{airplane[4]:<11}{airplane[5]:<11}{airplane[6]:<15}{airplane[7]:<10}{airplane[8]:<8}')
    db.close()

# function 2
def print_all_airplanes_by_wingspan():
    '''print all the airplanes sorted by wingspan'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print airplanes by their wingspans from highest to lowest
    sql = 'SELECT * FROM airplanes ORDER BY wingspan DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color
    print(f'model                      '+ Fore.BLUE +'wingspan  '+ Style.RESET_ALL +'length  max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<27}{Fore.GREEN}{airplane[2]:<10}{Style.RESET_ALL}{airplane[3]:<8}{airplane[4]:<11}{airplane[5]:<11}{airplane[6]:<15}{airplane[7]:<10}{airplane[8]:<8}')
    db.close()

# function 3
def print_all_airplanes_by_length():
    '''print all the airplanes sorted by length'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print airplanes by their lengths from highest to lowest
    sql = 'SELECT * FROM airplanes ORDER BY length DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color
    print(f'model                      wingspan  '+ Fore.BLUE +'length  '+ Style.RESET_ALL +'max_speed  max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<27}{airplane[2]:<10}{Fore.GREEN}{airplane[3]:<8}{Style.RESET_ALL}{airplane[4]:<11}{airplane[5]:<11}{airplane[6]:<15}{airplane[7]:<10}{airplane[8]:<8}')
    db.close()

# function 4
def print_all_airplanes_by_max_speed():
    '''print all the airplanes sorted by max speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print airplanes by their max speed from highest to lowest
    sql = 'SELECT * FROM airplanes ORDER BY max_speed DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color
    print(f'model                      wingspan  length  '+ Fore.BLUE +'max_speed  '+ Style.RESET_ALL +'max_range  max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<27}{airplane[2]:<10}{airplane[3]:<8}{Fore.GREEN}{airplane[4]:<11}{Style.RESET_ALL}{airplane[5]:<11}{airplane[6]:<15}{airplane[7]:<10}{airplane[8]:<8}')
    db.close()

# function 5
def print_all_airplanes_by_max_range():
    '''print all the airplanes sorted by max range'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print airplanes by their max range from highest to lowest
    sql = 'SELECT * FROM airplanes ORDER BY max_range DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color 
    print(f'model                      wingspan  length  max_speed  '+ Fore.BLUE +'max_range  '+ Style.RESET_ALL +'max_passenger  max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<27}{airplane[2]:<10}{airplane[3]:<8}{airplane[4]:<11}{Fore.GREEN}{airplane[5]:<11}{Style.RESET_ALL}{airplane[6]:<15}{airplane[7]:<10}{airplane[8]:<8}')
    db.close()

# function 6
def print_all_airplanes_by_max_passenger():
    '''print all the airplanes sorted by max passenger'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print airplanes by their max passengers from highest to lowest
    sql = 'SELECT * FROM airplanes ORDER BY max_passenger DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color
    print(f'model                      wingspan  length  max_speed  max_range  '+ Fore.BLUE +'max_passenger  '+ Style.RESET_ALL +'max_fuel  manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<27}{airplane[2]:<10}{airplane[3]:<8}{airplane[4]:<11}{airplane[5]:<11}{Fore.GREEN}{airplane[6]:<15}{Style.RESET_ALL}{airplane[7]:<10}{airplane[8]:<8}')
    db.close()

# function 7
def print_all_airplanes_by_max_fuel():
    '''print all the airplanes sorted by max fuel'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print airplanes by their max fuel from highest to lowest
    sql = 'SELECT * FROM airplanes ORDER BY max_fuel DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color
    print(f'model                      wingspan  length  max_speed  max_range  max_passenger  '+ Fore.BLUE +'max_fuel  '+ Style.RESET_ALL +'manufacturer_id')
    for airplane in results:
        print(f'{airplane[1]:<27}{airplane[2]:<10}{airplane[3]:<8}{airplane[4]:<11}{airplane[5]:<11}{airplane[6]:<15}{Fore.GREEN}{airplane[7]:<10}{Style.RESET_ALL}{airplane[8]:<8}')
    db.close()

# function 8
def search_and_print_airplane():
    '''search and print airplanes by id'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql ='SELECT id, model FROM airplanes'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f'id    model')
    # print out the ids and models for the user to choose
    for model in results:
        print(f'{model[0]:<6}{model[1]:<12}')
    print()
    # a user input 
    id = int(input('Enter id to view details:\n'))
    sql = 'SELECT * FROM airplanes WHERE id=?'
    cursor.execute(sql, (id,))
    # only fetch the one which the user choose
    airplane = cursor.fetchone()
    # print out all inforamtion about that airplane/adding color
    if airplane:
        print(Fore.BLUE + f'Airplane information:')
        print(Fore.GREEN + f'Model: {airplane[1]}')
        print(Fore.GREEN + f'Wingspan: {airplane[2]}m')
        print(Fore.GREEN + f'length: {airplane[3]}m')
        print(Fore.GREEN + f'Max_speed: {airplane[4]}km/h')
        print(Fore.GREEN + f'Max range: {airplane[5]}km')
        print(Fore.GREEN + f'Max passenger: {airplane[6]}')
        print(Fore.GREEN + f'Max fuel: {airplane[7]}L')
        print(Fore.GREEN + f'Manufacturer id: {airplane[8]}')
    else:
        print(Fore.RED + f'No airplane found with id {id}')
    db.close()

# function 9
def print_all_manufacturers():
    '''print all the manufacturers'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # print all manufacturers information
    sql = 'SELECT * FROM manufacturers'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results/adding color
    print(Fore.BLUE + f'id    name')
    for manufacturer in results:
        print(Fore.GREEN + f'{manufacturer[0]:<6}{manufacturer[1]:<12}')
    db.close()

# main code/user input
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
8. Print all information of one particular airplane
9. Print all manufacturers
10. Exit
""")
# run different defs depending in user's input
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
        search_and_print_airplane()
    elif user_input == '9':
        print_all_manufacturers()
    elif user_input == '10':
        break
    else:
        print('That was not an option\n')
   



