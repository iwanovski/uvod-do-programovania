# Legenda: meno,priezvisko,zapasy,goly,asistencie
ga_hodnoty = []
slovnik_pomer_hraci = {}

with open("hraci.txt", mode="r") as file:
    riadky = file.readlines()
    for riadok in riadky:
        # Odstranit specialny znak noveho
        # riadka na konci kazdeho riadku
        riadok = riadok.rstrip()
        udaje = riadok.split(",")

        goly = int(udaje[3])
        asistencie = int(udaje[4])
        zapasy = int(udaje[2])
        pomer = round((goly + asistencie) / zapasy,2)
        ga_hodnoty.append(pomer)


        #vysledny_riadok = udaje[0] + " " + udaje[1]+ " " + str(pomer) + "\n"
        # F-string - viete pouzit realne premenne, ktorym sa nahradia
        # hodnoty do stringu
        vysledny_riadok = f"{udaje[0]} {udaje[1]} {pomer}\n"
        print(vysledny_riadok)
        if pomer in slovnik_pomer_hraci.keys():
            slovnik_pomer_hraci[pomer].append(vysledny_riadok)
        else:
            slovnik_pomer_hraci[pomer] = [vysledny_riadok]
        print(ga_hodnoty)


    # 4. Tiez ratame G/A
    # Ale vo vystupnom subore chceme mat hracov zoradenych od
    # najvacsieho G/A po najmensie

with open("pomer.txt", mode="w") as file2:
    zoradeny_pomer_ga = []
    zoradene_riadky = []

    # Zoradenie hodnot pomerov pomocou INDEX sort
    for hodnota in ga_hodnoty:
        # Ak je zoznam zoradenych cisel prazdny, len pridaj aktualnu hodnotu
        if len(zoradene_riadky) == 0:
            zoradene_riadky = [hodnota]
            continue
        # Inak
        # Kym nenajdes cislo vacsie ako to ktore ma HODNOTA, tak pokracuj
        # ked najdes tak prirad hodnotu na poziciu
        for i in range(len(zoradene_riadky)):
            if hodnota <= zoradene_riadky[i]:
                zoradene_riadky.insert(i, hodnota)
                break
    
    # prejde zoradene GA pomery a na zaklade slovnika prirad hracov
    print(zoradene_riadky)
    for pomer in zoradene_riadky:
        hraci = slovnik_pomer_hraci[pomer]
        # Zisti ktory hrac ma dany pomer
        if len(hraci) == 1:
            hrac = hraci[0]
        else:
            # Ak ma viac hracov rovnaky pomer, zober prveho a potom ho vymaz zo zoznamu
            hrac = hraci[0]
            slovnik_pomer_hraci[pomer] = hraci[1:]
        file2.write(hrac)

    


