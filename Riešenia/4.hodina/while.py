

# While
cislo = int(input("Zadaj cislo: "))
while cislo < 5:
    print("Cislo je",cislo)
    cislo = cislo + 1
print("Koniec programu")
# ()

cislo = int(input("Zadaj cislo: "))
while True:
    print("Cislo je", cislo)
    if cislo > 4:
        break
    cislo += 1

for i in range(10):
    #if i % 2 == 1:
        # continue
    print("Cislo je", i)
    
