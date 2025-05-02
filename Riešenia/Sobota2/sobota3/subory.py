# Vyrataj, kolko bodov ziskali vsetci dokopy
# r = read = citanie
# w = write = zapis
# Otvorenie suboru
file = open("body.txt", "r")

riadky = file.readlines()
print(riadky)

# Prechadzanie riadkov
sucet = 0
for i in range(len(riadky)):
    riadok = riadky[i].rstrip()

    # <retazec>.split(<znak>)
    zoznam = riadok.split(",")
    body = zoznam[1]
    sucet = sucet + int(body)
    print(body)

print("Sucet bodov vsetkych je:", sucet)

# Zatvorenie suboru
file.close()

