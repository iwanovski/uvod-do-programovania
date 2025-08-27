

# Slovniky
# zlozitejsia datova struktura

zoznam = [1,236,3,12,3]

zoznam_studentov = ["Ivan Havran 26", "Karol Sebo 49"]

zoznam_mien = ["Ivan", "Karol"]
zoznam_priezvisiek = ["Havran", "Sebo"]
zoznam_vek = [26, 49]

# datova struktura, ktora obsahuje
# dvojice kluc a hodnota
# nie je zoradeny

student1 = {
    "meno": "Ivan",
    "priezvisko": "Havran",
    "vek": 26
}

student2 = {"meno": "Karol", "priezvisko": "Sebo","vek": 49}
# Kazdy kluc moze existovat raz
# priadenie slovnik[kluc] = hodnota
student2["meno"] = "Eva"
print(student2)

# Hodnota sa moze opakovat
# Pristup k hodnote na kluci
print(student1["meno"])

# Neexistujuci kluc hodi chybu
# print(student1["adresa"])

# Bezpecny pristup ku klucu
print(student1.get("adresa"))

# Dlzka = pocet klucov
print(len(student1))

# Prechadzanie slovnika
for kluc, hodnota in student1.items():
    print(kluc,hodnota)


