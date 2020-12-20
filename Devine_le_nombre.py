from random import randint

nmb = randint(0, 20000)
nmb2 = 0
compteur = 0
while nmb != nmb2:
    compteur += 1
    nmb2 = int(input("Ecrire un nombre"))
    if nmb2 > nmb:
        print("Trop Grand")
    elif nmb2 < nmb:
        print("Trop Petit")
    else:
        print("Gagné avec ", compteur, " coups")



