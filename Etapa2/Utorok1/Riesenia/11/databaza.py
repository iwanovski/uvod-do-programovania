import sqlite3
from uuid import uuid4

con = sqlite3.connect("moja_databaza.db")
cur = con.cursor()

# cur.execute("CREATE TABLE users(id,meno,priezvisko,vek)")

# cur.execute("DROP TABLE users")

# 1. Vytvorenie uzivatela
def vytvor_uzivatela(meno, priezvisko, vek):
    # Validacia
    if isinstance(vek, str) and vek.isdecimal():
        vek = int(vek)
    # Ak mi toto neplati v tomto bude
    # porovnanie typu
    # isinstance(premenna, <typ>) = je premenna typu <typ>?
    if not isinstance(vek, int):
        print("Zadal si nevalidny vek")
        return
    if vek <= 0:
        print("Zadal si nevalidny vek")
        return
    
    gener_id = str(uuid4())
    cur.execute(f"INSERT INTO users VALUES ('{gener_id}','{meno}','{priezvisko}',{vek})")
    con.commit()

# 2. Listovanie uzivatelov
def vylistuj_uzivatelov():
    result = cur.execute("SELECT * FROM users")
    return result.fetchall()
    
# 3. Nacitaj jedneho uzivatela
def nacitaj_uzivatela(id_uzivatela):
    # Filter na urovni databazy
    # preferujeme filtrovanie na urovni databazy
    # rychlejsie, efektivnejsie
    result = cur.execute(f"SELECT * FROM users WHERE id = '{id_uzivatela}'")
    return result.fetchone()

    # Filter na urovni vysledku
    # obcas sa hodi, ked nemame vsetky potrebne
    # informacie na filtrovanie v databazi
    # result = cur.execute(f"SELECT * FROM users")
    # uzivatelia = result.fetchall()
    #for uzivatel in uzivatelia:
        # if uzivatel[0] == id_uzivatela:
            # return uzivatel

# def nacitaj_uzivatela_by_name_surname(meno ,priezvko):

# 4. Aktualizuj uzivatela
def aktualizuj_uzivatela(id_uzivatela, slovnik_udajov):
    # Aktualizacia podla zmenenych parametrov
    aktualizacia = f""
    # Poslal uzivatel meno na aktualizaciu?
    meno_uzivatela = slovnik_udajov.get("meno")
    if meno_uzivatela != None:
        # Ak ano, pridam spravny prikaz do volania
        aktualizacia = f"meno = '{meno_uzivatela}', "
    priezvisko = slovnik_udajov.get("priezvisko")
    if priezvisko != None:
        # Ak ano, pridam spravny prikaz do volania
        aktualizacia += f"priezvisko = '{priezvisko}'"
    # For cyklus + kontrola klucov ci existuju v tabulku
    
    cur.execute(f"UPDATE users SET {aktualizacia} WHERE id = '{id_uzivatela}'")
    con.commit()

# Aktualizacia cez poslanie celeho objektu
def aktualizacia_uzivatela2(uzivatel):
    id_uzivatela = uzivatel[0]
    meno = uzivatel[1]
    priezvisko = uzivatel[2]
    vek = uzivatel[3]

    cur.execute(f"UPDATE users SET meno = '{meno}', vek = {vek} WHERE id = '{id_uzivatela}'")
    con.commit()
    

# 5. Zmaz uzivatela
def vymaz_uzivatela(id_uzivatela):
    cur.execute(f"DELETE FROM users WHERE id = '{id_uzivatela}'")
    con.commit()

# cur.execute("UPDATE users SET meno = 'Peter', vek = 15 WHERE meno = 'Ivan' AND vek = 40")
# con.commit()

result = cur.execute("SELECT * FROM users")
zoznam_uzivatelov = result.fetchall()
print(zoznam_uzivatelov)

slovnik = {}
# 1. Zistim pred opytanim ci kluc existuje
# asking for permission
if "key" in slovnik.keys():
    print(slovnik["key"])
else:
    print("Kluc neexistuje")

# 2. Pocitam s chybou a reagujem na nu
# asking for forgivness
try:
    print(slovnik["key"])
# catch <aku chybu chcete odchytit>
except KeyError:
    print("Kluc neexistuje")
















