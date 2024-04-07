fruit = str(input("Fruit Name: "))
fruit_color = str(input("what is your fruit color: "))

if fruit == "Banana":
    if fruit_color == "Green":
        print("UnRipe")
    elif fruit_color == "Yellow":
        print("Ripe")
    elif fruit_color == "Brown":
        print("OverRipe")
    exit()

print("we don't have another Fruits only add Banana")