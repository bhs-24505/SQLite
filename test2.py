#docstring - Eric Li - airplane database application
#imports
import sqlite3

#contants and variables
DATABASE = "SQLite.db"

#functions
def print_all_aircrafts():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM fighter'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print(f'name                              speed   max_g climb  range payload')
    for fighter in results:
        print(f'{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}')
    #loop stops here
    db.close()

def print_all_aircrafts_by_speed():
    '''print all the aircraft sorted by speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM fighter ORDER BY speed DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print(f'name                              speed   max_g climb  range payload')
    for fighter in results:
        print(f'{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}')
    #loop stops here
    db.close()

def print_all_aircrafts_by_climb():
    '''print all the aircraft sorted by climb'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM fighter ORDER BY climb DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print(f'name                              speed   max_g climb  range payload')
    for fighter in results:
        print(f'{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}')
    #loop stops here
    db.close()

def print_all_aircrafts_by_max_g():
    '''print all the aircraft sorted by max_g'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM fighter ORDER BY max_g DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print(f'name                              speed   max_g climb  range payload')
    for fighter in results:
        print(f'{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}')
    #loop stops here
    db.close()

def print_all_aircrafts_by_range():
    '''print all the aircraft sorted by range'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM fighter ORDER BY range DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print(f'name                              speed   max_g climb  range payload')
    for fighter in results:
        print(f'{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}')
    #loop stops here
    db.close()

def print_all_aircrafts_by_payload():
    '''print all the aircraft sorted by payload'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM fighter ORDER BY payload DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print(f'name                              speed   max_g climb  range payload')
    for fighter in results:
        print(f'{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}')
    #loop stops here
    db.close()

#main code
while True:

    user_input = input(
"""
What would you like to do.
1. Print all aircrafts
2. Print all aircrafts sorted by speed
3. Print all aircrafts sorted by max_g
4. Print all aircrafts sorted by climb
5. Print all aircrafts sorted by range
6. Print all aircrafts sorted by payload
7. Exit
""")
    try:
        if user_input == '1':
            print_all_aircrafts()
        elif user_input == '2':
            print_all_aircrafts_by_speed()
        elif user_input == '3':
            print_all_aircrafts_by_max_g()
        elif user_input == '4':
            print_all_aircrafts_by_climb()
        elif user_input == '5':
            print_all_aircrafts_by_range()
        elif user_input == '6':
            print_all_aircrafts_by_payload()
        elif user_input == '7':
            break
        else:
            print('That was not an option\n')
    except:
        print('That was not an option\n')


