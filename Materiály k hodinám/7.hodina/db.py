import sqlite3
con = sqlite3.connect("testing.db")
cur = con.cursor()

# Vytvorenie tabulky
# cur.execute("CREATE TABLE movie(title, year, score)")

# Pridanie do tabulky
#cur.execute("""
    #INSERT INTO movie VALUES
        #('Monty Python and the Holy Grail', 1975, 8.2)
#""")
#con.commit()

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchall())

res = cur.execute("SELECT title,year FROM movie")
print(res.fetchall())

res = cur.execute("DELETE FROM movie where title = 'Monty Python and the Holy Grail'")
con.commit()
res = cur.execute("SELECT title,year FROM movie")
print(res.fetchall())
