# Zorad ludi s bodmi od najmensieho poctu bodov
# r = read = citanie
# w = write = zapis
# Otvorenie suboru
#file = open("body.txt", "r")

with open("body.txt", "r") as file:
    riadky = file.readlines()

    # Prechadzanie riadkov
    zoznam_mien = []
    zoznam_bodov = []
    zoradene_body = []
    for i in range(len(riadky)):
        riadok = riadky[i].rstrip()

        zoznam = riadok.split(",")
        meno = zoznam[0]
        body = int(zoznam[1])
        zoznam_mien.append(meno)
        zoznam_bodov.append(body)
        
        zoradene_body.append(body)
    zoradene_body.sort()
    print(zoznam_mien)
    print(zoznam_bodov)
    print(zoradene_body)
            

    with open("zoradene.txt", "w") as file2:
        for i in range(len(zoradene_body)):
            body = zoradene_body[i]
            pocet = zoznam_bodov.count(body)
            delete = False
            index = zoznam_bodov.index(body)
            if pocet != 1:
                delete = True
            meno = zoznam_mien[index]
            if delete:
                zoznam_mien[index] = ""
                zoznam_bodov[index] = -1
            file2.write(meno + "," + str(body) + "\n")

