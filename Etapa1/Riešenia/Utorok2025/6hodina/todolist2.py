# Uloha bude slovnik
# ktory bude vyzerat nasledovne
# {
#   "nazov": "Vyhod smeti",
#   "dokedy": "7.3.2025",
# }

zoznam_uloh = []

def nacitaj_ulohy():
    with open("ulohy.txt", "r") as file:
        riadky = [riadok.rstrip() for riadok in file.readlines()]
        
        #upravene_riadky = []
        #for riadok in riadky:
            #upravene_riadky.append(riadok.rstrip())

        for riadok in riadky:
            udaje = riadok.split(',')
            slovnik = {}
            slovnik["nazov"] = udaje[0]
            slovnik["dokedy"] = udaje[1]
            zoznam_uloh.append(slovnik)

nacitaj_ulohy()    

def vytvor_ulohu(nazov, dokedy):
    slovnik = {}
    slovnik["nazov"] = nazov
    slovnik["dokedy"] = dokedy
    zoznam_uloh.append(slovnik)
    with open("ulohy.txt", "a") as file:
        file.write(f"{nazov},{dokedy}\n")

def vylistuj_ulohy():
    for i in range(len(zoznam_uloh)):
        print("Uloha cislo",int(i)+1)
        print(zoznam_uloh[i])

def zmaz_ulohu(nazov):
    # Zistit index kde sa nachadza
    # uloha s nazvom
    # Pomocou pop odstranit prvok na
    # tomto indexe
    for i in range(len(zoznam_uloh)):
        if zoznam_uloh[i]["nazov"] == nazov:
            zoznam_uloh.pop(i)
            break
        
    riadky = []
    with open('ulohy.txt','r') as file:
        riadky = [riadok.rstrip() for riadok in file.readlines()]
    print(riadky)

    filtrovane_riadky = []
    for riadok in riadky:
        udaje = riadok.split(',')
        if udaje[0] != nazov:
            filtrovane_riadky.append(riadok)
    
    with open('ulohy.txt', 'w') as file:
        for riadok in filtrovane_riadky:
            file.write(f"{riadok}\n")
    
        

def zmen_dokedy(nazov, dokedy):
    for i in range(len(zoznam_uloh)):
        if zoznam_uloh[i]["nazov"] == nazov:
            zoznam_uloh[i]['dokedy'] = dokedy
            break
