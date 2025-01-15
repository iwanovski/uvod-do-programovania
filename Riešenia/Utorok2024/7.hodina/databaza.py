import sqlite3
from uuid import uuid4

# Pripojenie databazy a vytvorenie kurzoru
con = sqlite3.connect("db.db")
cur = con.cursor()

# Vytvorenie tabulky
# cur.execute("CREATE TABLE user(id, name, age)")

# Vrat vsetky tabulky
result = cur.execute("SELECT name from sqlite_master")
print(result.fetchall())

def pridaj_uzivatela(meno, vek):
    my_id = uuid4()
    result = cur.execute(f"INSERT INTO user VALUES ('{my_id}','{meno}',{vek})")
    con.commit()

# pridaj_uzivatela("Ivan", 25)

# Vrat vsetkych uzivatelov v tabulke

result = cur.execute("SELECT * FROM user")
print(result.fetchall())

def aktualizacia_uzivatela(my_id, vek):
    result = cur.execute(f"UPDATE user SET age = {vek} WHERE id = '{my_id}'")
    con.commit()

aktualizacia_uzivatela("c235957b-6310-4c22-9ac7-ed74b1e02387", 45)

# Vrat vsetkych uzivatelov v tabulke

result = cur.execute("SELECT * FROM user")
print(result.fetchall())
