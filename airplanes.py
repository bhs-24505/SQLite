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