zoznam_cisel = [4,8,12,9,54,10]
zoznam_zoznamov = [[1,2,3],[],[8,4,6,4]]

osoba_udaje = ["Meno", "Priezvisko", "Vek"]
osoba1 = ["Ivan", "Havran", "26"]
osoba2 = ["Peter", "Havran", "36"]


# Slovniky
# mnozstvo dvojic KLUC a HODNOTA
osoba_slovnik = {"meno": "Ivan", "priezvisko": "Havran", "vek":26}
# kluc je unikatny a je iba jeden
# jeden kluc = jedna hodnota
# jedna hodnota moze byt vo viacerych klucoch

# Prazdny slovnik
osoba = {}

# Vytvorenie kluca s hodnotou
osoba["meno"] = "Peter"
print(osoba)

# Vypis kluca
print(osoba["meno"])

# Pozor, ak kluc neexistuje, dostaneme chybu
# print(osoba["vek"])

# Hodnota moze byt aj slovnik/zoznam
osoba["adresa"] = {"ulica": "Vymyslena 457", "mesto": "Bratislava"}
print(osoba)
