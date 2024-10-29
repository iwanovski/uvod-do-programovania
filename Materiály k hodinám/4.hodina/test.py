with open("hraci.txt","r") as file:
    lines = [line.rstrip() for line in file.readlines()]
    print(lines[0])
