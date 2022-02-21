import random
import time

pocitacVyhra = 0
hracVyhra = 0
remiza = 0
konec = 0

while True:

    volby = ["kamen", "papir", "nuzky"]

    hracVolba = input("kamen, nuzky, papir, or konec\n")

    pocitacVolba = (random.choice(volby))
    print(pocitacVolba)

    if hracVolba == pocitacVolba:
        print("remiza!\n")
        remiza += 1
        konec += 1

    elif hracVolba == "kamen":
        if pocitacVolba == "papir":
            print("Pocitac vyhral!\n")
            pocitacVyhra +=1
            konec += 1

        else:
            print("Hrac vyhral!\n")
            hracVyhra += 1
            konec += 1

    elif hracVolba == "papir":
        if pocitacVolba == "kamen":
            print("Hrac vyhral!\n")
            hracVyhra += 1
            konec += 1

        else:
            print("Pocitac vyhral!\n")
            pocitacVyhra += 1
            konec += 1

    elif hracVolba == "nuzky":
        if pocitacVolba == "kamen":
            print("Pocitac vyhral!\n")
            pocitacVyhra += 1
            konec += 1

        else:
            print("Hrac vyhral!\n")
            hracVyhra += 1
            konec += 1

    elif hracVolba == "konec":
            volby.append("konec")
            print("\nKonec Hry!\n")
            print("Pocitac: ", pocitacVyhra, "vyher!")
            print("Hrac: ", hracVyhra, "vyher!")
            print("remiz: ", remiza, "remiza!")
            break
