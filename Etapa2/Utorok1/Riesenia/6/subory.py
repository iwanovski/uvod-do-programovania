
# Praca so suborom

# Nacitanie suboru
# Otvorenie suboru


# Subor si viete otvorit tromi sposobmi
# r = read mode = citanie

# w = write mode = pisanie
# a = append mode = pisanie na koniec suboru

# file = open("dokument.txt", mode="r")
# otvorenie pomocou with
# subor sa sam zatvori na konci
file2 = open("novy_dokument.txt", mode="w")
with open("dokument.txt", mode="r") as file:
    # Citanie zo suboru
    # citanie pomocou read
    # bud precita cele a ulozi ako retazec
    # alebo precita X znakov ako retazec
    # retazec = file.read(5)

    # citanie pomocou readlines
    print(file)
    riadky = file.readlines()
    print(riadky)

    file.readlines()

    # Zatvorenie suboru
    # file.close()

    # write
    file2.write("hviezda123\n")

    # chod do noveho riadka = \n
    # writelines
    file2.writelines(["cesta\n","pre\n","auta\n"])
    
file2.close()

# with open("dokument.txt", mode="w") as file:
# file = open("zapis_dokument.txt", mode="w")
# zapisem co som precita
# ...
