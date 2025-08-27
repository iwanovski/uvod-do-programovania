

# Vytvorte si jednoducho TODO aplikaciu

# co mate urobit = uloha
# do kedy to mate urobit = dokedy

def vytvor_todo(uloha, dokedy):
    todo = {"uloha": uloha, "dokedy": dokedy}
    todos.append(todo)

    with open("ulohy.txt","a") as file:
        file.write(f"\n{uloha},{dokedy}")


def vylistuj_todos():
    for i in range(len(todos)):
        todo = todos[i]
        print(todo["uloha"], todo["dokedy"])

def zmaz_todo(uloha):
    new_todos = []
    for i in range(len(todos)):
        todo = todos[i]
        if todo["uloha"] == uloha:
            # Nasiel som uloha s takym menom
            # todos.remove({"uloha": todo["uloha"], "dokedy": todo["dokedy"]})
            todos.pop(i)
            return

        # if todo["uloha"] != uloha:
            # new_todos.append(todo["uloha"])
    

def nacitaj_subor():
    with open("ulohy.txt") as file:
        todos = []
        riadky = file.readlines()
        for i in range(len(riadky)):
            riadok = riadky[i].rstrip()
            udaje = riadok.split(',')
            todos.append({"uloha": udaje[0], "dokedy": udaje[1]})
        return todos

todos = nacitaj_subor()
