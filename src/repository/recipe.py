import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='pizzapidb',
    user='root',
    password='')

cursor = db.cursor(dictionary=True)

def get_all_recipes() -> list :
    query = "SELECT * FROM recipe"
    cursor.execute(query)
    return cursor.fetchall()

def get_recipe(id: int) -> dict:
    query = "SELECT * FROM recipe WHERE id = %s"
    cursor.execute(query,(id,))
    return cursor.fetchone()

def create_new_recipe(data: dict) -> int:
    query = "INSERT INTO recipe (title) VALUES (%(title)s)"
    cursor.execute(query, data)
    db.commit()
    return cursor.lastrowid

def update_recipe(data: dict):
    query = "UPDATE recipe SET title = %(title)s WHERE id = %(id)s"
    cursor.execute(query, data)
    db.commit()

