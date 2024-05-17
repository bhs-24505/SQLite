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
    print(results)
    db.close()


