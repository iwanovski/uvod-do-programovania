# Uloha bude slovnik
# ktory bude vyzerat nasledovne
# {
#   "nazov": "Vyhod smeti",
#   "dokedy": "7.3.2025",
# }

zoznam_uloh = []

def vytvor_ulohu(nazov, dokedy):
    slovnik = {}
    slovnik["nazov"] = nazov
    slovnik["dokedy"] = dokedy
    zoznam_uloh.append(slovnik)

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

def zmen_dokedy(nazov, dokedy):
    for i in range(len(zoznam_uloh)):
        if zoznam_uloh[i]["nazov"] == nazov:
            zoznam_uloh[i]['dokedy'] = dokedy
            break
    
    
