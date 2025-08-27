
# Funkcia = nejaky kus kodu
# ktory pre nas niekto napisal
# Zavolame pomocou
# <nazov> a ()
# do () davame vstup do funkcie

# Dva typy:
# cislo
# retazec

print("Hello1 slovo *")
print(26)

# Premenna
# <nazov_premennej> = <hodnota>
cislo = 15

# pouzitie premennej
print(cislo)

# Miniuloha
# Vypiste svoje meno a vek
# S tym ze pouzijete premenne
# meno = "Petra"
# print(meno)
# vek = 48
# print(vek)
# print(vek + 10)

# Vstup do programu
# vstup = input
meno = input("Zadaj svoje meno")
print(meno)

# Miniuloha
# Doplnme si na vstup vek
# Pretypovanie
# z retazca urobim cele cislo
# pomocou funkcie int
vek = int(input("Zadaj svoj vek"))
print(vek)
print(type(vek))
print(vek + 10)

# Podmienky
# Ak nieco plati, tak sa vykona
# nejaky kod
# Ak to neplati, tak sa kod nevykona

# if <vyraz>
# Miniuloha
# Chceme napisat podmienku
# Ze ak mas viac ako 16 rokov
# mozes mat vodicak na auto
if vek > 16:
    print("Mozes mat vodicak na auto")
print("Koniec programu")










