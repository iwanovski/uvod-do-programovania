try:
    undefined = 10
    print(undefined)
    print(undefined // 0)
except NameError:
    print("Premenna neexistuje")
except ZeroDivisionError:
    print("Nulou nedelime")
# except Exception - chyti vsetky chyby, pouzivat opatrne
