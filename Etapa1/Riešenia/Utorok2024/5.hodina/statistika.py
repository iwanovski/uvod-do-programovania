with open("hraci.txt","r") as file:
    riadky = [line.rstrip() for line in file.readlines()]
    print(riadky)
    # Toto nebudeme menit

    # Prva uloha
    # Vypis pocet hracov, ktori hrali v NHL v minulej sezone
    print("Pocet hracov v minulej sezone:",len(riadky))


    # Tretia uloha pridajme kazdemu hracovi aj pocet bodov
    # Body = Goly + Asistencie
    # pomocou split si rozdelit riadok, precitat pocet golov
    # a asitencii, zratat ho, a na koniec riadku pridat
    riadky2 = []
    for riadok in riadky:
        udaje = riadok.split(',')
        print(udaje)
        pocet_bodov = int(udaje[3]) + int(udaje[4])

        udaje.append(str(pocet_bodov))
        print(udaje)

        # Ako si spojime zoznam nas5 do retazca?
        retazec = ",".join(udaje)
        riadky2.append(retazec)

    # Druha uloha
    # Zapisme zoznam do noveho suboru
    # Ale pridajme na zaciatok 'legenda'
    
    with open("uprava.txt","w") as file2:
        riadky2 = [line+"\n" for line in riadky2]
        riadky2.insert(0,"Meno,Priezvisko,Zapasy,Goly,Asistencie,Body\n")
        #riadky2 = ["Meno,Priezvisko,Zapasy,Goly,Asistencie\n"] + riadky2
        file2.writelines(riadky2)

    
    
