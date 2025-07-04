
import sqlite3
from uuid import uuid4

# Functions
con = sqlite3.connect("db.db", check_same_thread=False)
cur = con.cursor()

# cur.execute("CREATE TABLE user(id, name, surname, age)")

def vylistuj_uzivatelov():
    result = cur.execute("SELECT * from user")
    return result.fetchall()

def nacitaj_uzivatela(user_id):
    result = cur.execute(f"SELECT * from user WHERE id = '{user_id}'")
    return result.fetchone()

def pridaj_uzivatela(name, surname, age):
    my_id = str(uuid4())
    cur.execute(f"INSERT INTO user VALUES ('{my_id}','{name}','{surname}',{age})")
    con.commit()

def aktualizacia_uzivatela(my_id, name, surname, age):
    query = "UPDATE user SET name = ?, surname = ?, age = ? WHERE id = ?"
    cur.execute(query, (name, surname, age, my_id))
    con.commit()

def zmaz_uzivatela(my_id):
    cur.execute(f"DELETE FROM user WHERE id ='{my_id}'")
    con.commit()

