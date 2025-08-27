

def vydel(cislo1, cislo2):
    try:
        vysledok = cislo1 / cislo2
    except ZeroDivisionError:
        print("Nulou nedelime")
        return
    return vysledok


print(vydel(4,2))
print(vydel(4,0))

def test():
    zoznam_cisel = [1,5,4,6,8,5]
    try:
        cislo = zoznam_cisel[5]
    except IndexError:
        print("Nemas 6 cisel")
        return -1
    return cislo


def vydel_x_krat(cislo1, cislo2, x):
    if cislo2 == 0:
        print("Cislo2 je 0")
        return None
    
    vysledok = cislo1 / cislo2
    for i in range(x-1):
        vysledok = cislo1 / cislo2
    print(vysledok)
    return vysledok
    



