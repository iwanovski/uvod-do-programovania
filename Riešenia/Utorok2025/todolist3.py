# Uloha bude slovnik
# ktory bude vyzerat nasledovne
# {
#   "nazov": "Vyhod smeti",
#   "dokedy": "7.3.2025",
# }

import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

# Vytvorenie tabulky
# cur.execute("CREATE TABLE ulohy(nazov, dokedy)")

def vytvor_ulohu(nazov, dokedy):
    cur.execute(f"INSERT INTO ulohy VALUES ('{nazov}','{dokedy}')")
    con.commit()
    
def ulohy_z_db():
    result = cur.execute("SELECT * FROM ulohy")
    return result.fetchall()

def zmaz_ulohu(nazov):
    cur.execute(f"DELETE FROM ulohy WHERE nazov = '{nazov}' ")
    con.commit()
