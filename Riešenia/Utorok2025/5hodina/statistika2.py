# udaje = zoznam udajov

# Funkcie

# 1. nic nevracuju

# 2. ktore vracaju

def nacitaj(udaje):
    zoznam_udajov = ["meno", "priezvisko", "zapasy", "goly", "asistencie"]
    slovnik = {}
    for i in range(5):
        slovnik[zoznam_udajov[i]] = udaje[i]
    return slovnik
    

# Otvorenie suboru s automatickym zatvorenim
# Pozor, subor sa musi nachadzat v rovnakom adresari ako kod
# ktory ho otvara (v nasom pripade, vo vsebocnosti to tak nemusi
# byt ale je to narocnejsie osetrit)
with open("hraci.txt", "r")as subor:
    # Precitanie riadkov subora
    riadky = subor.readlines()
    # print(riadky)

    # Pre lahsie pouzivanie odstranime s kazdeho riadka
    # symbol \n ktory znamena NOVY RIADOK
    upravene_riadky = []
    for riadok in riadky:
        upravene_riadky.append(riadok.rstrip())
    print(upravene_riadky)

    # 1.uloha = vypis sucet zapasov vsetkych hracov v subore
    # pocet zapasov je informacia hned za priezviskom
    sucet_zapasov = 0
    for riadok in upravene_riadky:
        udaje = riadok.split(',')
        nacitane_udaje = nacitaj(udaje)
        print(nacitane_udaje)
        pocet_zapasov = int(nacitane_udaje["zapasy"])
        sucet_zapasov += pocet_zapasov
    print("Sucet zapasov hracov je", sucet_zapasov)

    # 2.uloha = sucet golov hracov, ktori mali aspon 30 zapasov
    sucet_golov = 0
    for riadok in upravene_riadky:
        udaje = riadok.split(',')
        pocet_zapasov = int(udaje[2])
        pocet_golov = int(udaje[3])
        if pocet_zapasov > 29:
            sucet_golov += pocet_golov
    print("Sucet golov hracov nad 30 zapsov je", sucet_golov)

    # 3.uloha = vytvorte novy subor, kde zapisete rovnaku tabulku
    # do ktorej pridate legendu (co znamenaju jednotlive udaje)
    # a rovnako doplniete pocet bodov
    # Body = Goly + Asistencie
    with open("upraveni_hraci.txt", "w")as subor2:
        subor2.write("Meno,Priezvisko,Zapasy,Goly,Asistencie,Body\n")
        for riadok in upravene_riadky:
            udaje = riadok.split(',')
            pocet_golov = int(udaje[3])
            pocet_asistencii = int(udaje[4])
            pocet_bodov = pocet_golov + pocet_asistencii
            # Tri moznosti ako zapisat body na koniec
            
            # 1.moznost - pridanie noveho udaju a spojenie na koniec
            #udaje.append(str(pocet_bodov))
            #subor2.write(",".join(udaje)+"\n")

            # 2.moznost - Spojenie retazca pomocou +
            subor2.write(riadok+","+str(pocet_bodov)+"\n")

            # 3.moznost - f-string
            #subor2.write(f"{riadok},{pocet_bodov}\n")
