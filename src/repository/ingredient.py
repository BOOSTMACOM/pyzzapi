import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='pizzapidb',
    user='root',
    password=''
)

cursor = db.cursor(dictionary=True)

def get_all() -> list :
    query = "SELECT * FROM ingredient"
    cursor.execute(query)
    return cursor.fetchall()

def get(id: int) -> dict:
    query = "SELECT * FROM ingredient WHERE id = %s"
    cursor.execute(query,(id,))
    return cursor.fetchone()

def insert(data: dict) -> int:
    query = "INSERT INTO ingredient (label) VALUES (%(label)s)"
    cursor.execute(query, data)
    db.commit()
    return cursor.lastrowid

def update(data: dict):
    query = "UPDATE ingredient SET label = %(label)s WHERE id = %(id)s"
    cursor.execute(query, data)
    db.commit()

