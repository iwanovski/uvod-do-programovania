
import sqlite3
# Import nahodneho generovania ID parametra
from uuid import uuid4


# Pripojenie k databazy (aj vytvori
# subor, ak neexistuje)
con = sqlite3.connect("moja_databaza.db")

# Vytvorenie kurzoru
# sluzi na pracu s databazou
cur = con.cursor()

# Vytvorit tabulku
# 1. SQL prikaz = CREATE TABLE
# user -> nazov tabulky
# (id, meno, priezvisko, vek) -> stlpce tabulky
# cur.execute("CREATE TABLE users(id, meno, priezvisko, vek)")

# 6. SQL prikaz = DROP TABLE <nazov>
# zmaz tabulku
# cur.execute("DROP TABLE users") 

# vytvorenie uzivatela Ivan,Havran,26
# vygeneruj ID ked chces niekoho vytvorit
# po vygenerovani prevediem UUID na retazec pomocou str
gener_id = str(uuid4())
# 2. SQL prikaz = INSERT INTO
# vloz riadok/riadky do tabulky <nazov>
cur.execute(f"INSERT INTO users VALUES ('{gener_id}','Ivan','Havran',26)")
# Potvrdenie transakcie - COMMIT
# con.commit()

# 3. SQL prikaz = SELECT 
# vyber riadok/riadky z databaze
# SELECT <co> FROM <tabulka>/<tabulky>
# * vsetky stlpce + (riadky)
result = cur.execute("SELECT * FROM users")
# zober iba niektore stlpce
# result = cur.execute("SELECT meno,vek FROM users")
# filter riadkov WHERE 
# result = cur.execute("SELECT meno,vek FROM users WHERE vek > 30")
# result.fetchall() -> vrati ZOZNAM vsetkych riadkov
zoznam_uzivatelov = result.fetchall()
print(zoznam_uzivatelov)

# Premenime zoznam na .csv subor, ktory vieme otvorit napr v Exceli
#with open("uzivatelia.csv","w") as file:
    #for uzivatel in zoznam_uzivatelov:
        #file.write(f"{uzivatel[1]},{uzivatel[2]},{uzivatel[3]}\n")

# 4. SQL prikaz = UPDATE
# upravit riadok/riadky na zaklade nejakej podmienky, vieme upravit
# jeden alebo viac hodnot v stlpcoch

# zmenim meno Ivan na Peter
# UPDATE <tabulka>  SET <stlpec> = <hodnota> WHERE podmienka
cur.execute("UPDATE users SET meno = 'Peter', vek = 15 WHERE meno = 'Ivan' AND vek = 40")
con.commit()

# 5. SQL prikaz = DELETE
# mazanie riadka/riadkov na zaklade podmienky
# DELETE FROM <tabulka> WHERE podmienka
cur.execute("DELETE FROM users WHERE meno = 'Peter' OR meno = 'Ivan'")
con.commit()
result = cur.execute("SELECT * FROM users")
zoznam_uzivatelov = result.fetchall()
print(zoznam_uzivatelov)

# pridaj_uzivatela(meno, priezvisko, vek):














