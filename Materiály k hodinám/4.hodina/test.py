with open("hraci.txt","r") as file:
    lines = [line.rstrip() for line in file.readlines()]
    print(lines[0])


with open("results.txt","w") as file:
    for i in range(10):
        file.write(str(i) + "\n")
