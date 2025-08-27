# Otvorenie suboru
file = open("body.txt")

#meno = file.read(5)
#print(meno)
# subor = file.read()
# print(subor)

def znamka(pocet_bodov):
    if pocet_bodov > 75:
        return "1"
    elif pocet_bodov > 60:
        return "2"
    elif pocet_bodov > 40:
        return "3"
    elif pocet_bodov > 20:
        return "4"
    else:
        return "5"

riadky = file.readlines()
print(riadky)

# Zavretie suboru
file.close()

# Konstrukt with
with open("body.txt", "r") as file,open("znamky.txt", "w") as file2:
    riadky = file.readlines()
    print(riadky)

    for i in range(len(riadky)):
        riadky[i] = riadky[i].rstrip()
        riadok = riadky[i]  
        udaje = riadok.split(",")
        print(udaje)
        body = int(udaje[1])
        hodnotenie = znamka(body)
        print(hodnotenie)
        # file2.write(riadok + "," + hodnotenie + "\n")
        file2.write(f"{riadok},{hodnotenie}\n")
    print(riadky)

        
# "w" = zapis do suboru
# "a" = zapis na koniec suboru
    

