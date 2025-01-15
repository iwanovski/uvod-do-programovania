with open("hraci.txt","r") as file:
    riadky = [line.rstrip() for line in file.readlines()]
    print(riadky)
    # Toto nebudeme menit

    # Prva uloha
    # Vypis pocet hracov, ktori hrali v NHL v minulej sezone
    print("Pocet hracov v minulej sezone:",len(riadky))

    # Druha uloha
    # Kolko dali nasi hraci dokopy golov
    # Ale iba hraci, ktori dali viac ako 5 golov
    print(riadky[0])
    sucet_golov = 0
    sucet_golov_vsetkych = 0
    sucet_zapasov = 0
    print(riadky)
    for riadok in riadky:
        print(riadok)
        pocet_golov = int(riadok.split(",")[3])
        pocet_zapasov = int(riadok.split(",")[2])
        if pocet_golov >= 5:
            sucet_golov += pocet_golov
        sucet_golov_vsetkych += pocet_golov
        sucet_zapasov += pocet_zapasov
    print("Vsetci, co dali viac ako 5 golov, dali spolu",sucet_golov)

    # Tretia uloha
    # Vypis priemer golu nasich hracov na zapas
    print("Pocet golov",sucet_golov_vsetkych)
    print("Pocet zapasov",sucet_zapasov)
    print("Priemer golu na zapas", sucet_golov_vsetkych / sucet_zapasov)

    
    
