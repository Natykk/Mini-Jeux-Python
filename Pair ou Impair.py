valeur = 0
nombre = 0
valeur = int(input("Met un nombre"))
def pair(nombre):
    if nombre % 2  == 0:
        return True
    else:
        return False

if pair(valeur):
    print("PAIR")
else:
    print("IMPAIR")

