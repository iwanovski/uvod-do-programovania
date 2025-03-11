# Mam ulohu, ulozit informaciu o mene a priezvisku pre 10 ludi

# Pouzijem premenne?
meno1 = "Ivan"
meno2 = "Peter"
priezvisko1 = "Havran"
priezvisko2 = "Havran"
# Velmi rychlo zisime, ako to nie je efektivne

# Pouzijeme zoznam?
osoba1 = ["Ivan", "Havran"]
osoba2 = ["Peter", "Havran"]
# Eefektivnejsie, ale musim si pamatat kde je co ulozene

# Slovniky

# nova datova struktura, je to mnozina dvojic KLUC:HODNOTA

osoba1 = {"meno": "Ivan", "priezvisko": "Havran"}
osoba2 = {"meno": "Peter", "priezvisko": "Havran"}

# kluce musia byt unikatne

# Praca so slovnikom

print(osoba1)
# Pristup ku hodnota na kluci 'meno'
print(osoba1["meno"])
#Pristup ku vsetkym klucom
print(osoba1.keys())
# Pristup ku vsetkym hodnotam
print(osoba1.values())
# Pocet klucov
print(len(osoba1))
# pridanie do slovnika
osoba1["vek"] = 25
print(osoba1)
# odstranenie kluca zo slovnika
osoba1.pop("vek")
print(osoba1)
# Pristup k prvku cez kluc, bezpecny
print(osoba1.get("adresa")) # - nehodi chybu ak kluc neexistuje
# 
