

# LEGENDA suboru:
# meno,priezvisko,zapasy,goly,asistencie

with open("hraci.txt", mode="r") as file:
    # precitam cely subor
    riadky = file.readlines()
    # 1. uloha
    # Vypocitajte, kolko dokopy zapasov
    # odohrali nasi hraci za sezonu
    print(riadky)
    for riadok in riadky:
        # print(riadok)

        # Rozdelenie retazca
        # split()
        # vrati nam zoznam podretazcov
        # rozdeli na zaklade
        udaje = riadok.split(",")
        # udaje == [meno,priezvisko,zapasy,goly,asistencie]
        # vytiahni udaje z indexu 2 == zapasy
        pocet_zapasov = int(udaje[2])
        print(pocet_zapasov)


    # vysledok
    print("Nasi hraci odohrali", 0, 'zapasov')
