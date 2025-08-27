# Otvorenie suboru
file = open("body.txt")

#meno = file.read(5)
#print(meno)
# subor = file.read()
# print(subor)

riadky = file.readlines()
print(riadky)

# Zavretie suboru
file.close()

# Konstrukt with
with open("body.txt") as file:
    riadky = file.readlines()
    print(riadky)

    for i in range(len(riadky)):
        riadok = riadky[i]
        riadky[i] = riadok.rstrip()
        print(riadok)
    print(riadky)

    # Sucet bodov vsetkych ludi
    sucet = 0
    for i in range(len(riadky)):
        riadok = riadky[i]
        udaje = riadok.split(",")
        print(udaje)
        body = int(udaje[1])
        sucet += body
    print("Sucet bodov", sucet)
        

    

