with open("zapis1.txt", "w") as file:
    file.write("Ivan")
    file.write(str(48484))
    file.write("\n")

    file.writelines(["Petra\n","Ivan"])
    
