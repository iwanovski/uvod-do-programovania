# Zoznam = prvy komplexnejsi typ, ktory sa naucime

# String, int a bool boli vsetko jednoduche typy = ulozili sme do
# premennej vzdy jednu informaciu

# Zoznam nam umoznuje ukladat viacero informacii do jednej premennej

# Vytvorenie zoznamu
zoznam1 = [1,5,8,23,78]
prazdny_zoznam = []

# Operacie so zoznamom
# Nie kazda funkcia funguje bez typu - existuju funkcie, ktore
# funguju len na nejakom type, a take si teraz ukazeme
# volame ich pomocou .<nazov_funkcie>() na konkretnom objekte/premennej

# Funkcia append = pridanie na koniec zoznamu
print(zoznam1)
print("Teraz pridame cislo 5 na koniec")
zoznam1.append(5)
print(zoznam1)

# Zoznam ma jasne dane poradie - prvky su usporiadane
# Ked chceme pristupit ku konkretnemu prvku, potrebujeme nato
# tzv. INDEX = je to hodnota, ktora sa rovne pozicii od ktorej odratame jedna
# Napr. v nasom zoznam [1,5,8,23,78] je cislo 8 na pozicii 3
# ale na INDEXe 2
print("Cislo 8")
# Na pristup ko konkretnemu indexu sluzi []
print(zoznam1[2])

# Ak sa pamatate for cyklus, kde sa riadiaca premmena (pocitadlo) zacina
# vzdy od 0, teraz sa nam to hodi

# Priklad - vypis prvky zoznamu
for i in range(len(zoznam1)):
    print(zoznam1[i])
