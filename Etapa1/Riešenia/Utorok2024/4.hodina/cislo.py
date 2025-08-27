import io
from random import randint
# Vymyslime si cislo

magicke_cislo = randint(1,100)

# Vypytaj si od uzivatela cislo
meno = input("Zadaj svoje meno: ")
cislo = int(input("Zadaj cislo: "))

# Pokial cislo a magicke_cislo nie su rovnake
# tak povezd uzivatelovi ci jeho cislo je
# vacsie alebo mensie a daj mu moznost
# zadat nove cislo

# != - opak porovnania ==
while magicke_cislo != cislo:
    if magicke_cislo > cislo:
        print("Zadal si prilis male cislo")
    else:
        print("Zadal si prilis velke cislo")
    cislo = int(input("Zadaj cislo: "))

#print("Gratulujem,"+ meno +" uhadol si cislo")
#print("Gratulujem,",meno,"uhadol si cislo")
print(f"Gratulujem,{meno} uhadol si cislo")

with open("zaznam.txt","a") as file:
    file.write(f"Gratulujem,{meno} uhadol si cislo\n")
