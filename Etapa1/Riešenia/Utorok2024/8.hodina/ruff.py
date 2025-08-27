# Praca s kniznicou ruff

# Najprv si ju musime nainstalovat ako externu python kniznicu

# Teda v terminali zavolat

# python3 -m pip install ruff

# alebo

# python -m pip install ruff

# Potom vieme pouzit pomocou

# ruff check <nazov_suboru.py> --select ALL

# Ale musime sa nachadzat v terminali v rovnakom subori ako mame ulozeny nas program

# Informacie o tomto nastroji najdeme na stranke https://docs.astral.sh/ruff/

# Mozeme skusit na tomto programe

def funkcia(zoznam=[]):
    zoznam.append(5)
    print(zoznam)

funkcia()
funkcia()
