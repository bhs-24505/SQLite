import sqlite3
DATABASE = 'cars.db'
with sqlite3.connect(DATABASE) as db:
  cursor = db.cursor()
  sql = 'SELECT * FROM car;'
  cursor.execute(sql)
  results = cursor.fetchall()
  # print them nicely
  for car in results:
    print(f'Car: {car[1]} Top Speed: {car[2]}')
