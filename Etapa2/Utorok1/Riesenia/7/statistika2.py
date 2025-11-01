# Legenda: meno,priezvisko,zapasy,goly,asistencie
with open("hraci.txt", mode="r") as file:
    riadky = file.readlines()
    sucet = 0
    asistencie = 0
    for riadok in riadky:
        # Odstranit specialny znak noveho
        # riadka na konci kazdeho riadku
        riadok = riadok.rstrip()
        udaje = riadok.split(",")
        # ["Juraj", "Slafkovky", "80", "20", "30"]
        pocet_zapasov = int(udaje[2])
        # print(udaje)
        # print(pocet_zapasov)
        sucet = sucet + pocet_zapasov

        # 2.
        # pocet_asistencii = int(udaje[4])
        if pocet_zapasov >= 10:
            pocet_asistencii = int(udaje[4])
            print(pocet_asistencii)
            asistencie = asistencie + pocet_asistencii
            

    # 2. Spocitajte pocet asistencii hracov ktori
    # odohrali aspon 10 alebo viac zapasov
    print("Pocet asistencii hracov nad 10 zapasov", asistencie)

    # 1. Spocitaj pocet zapasov co nasi hraci odohrali
    print("Nasi hraci odohrali", sucet, 'zapasov')
