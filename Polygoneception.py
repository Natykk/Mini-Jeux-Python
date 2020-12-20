import turtle
T = turtle.Turtle()
T.speed(4)
taille = int(input("la taille du segment >"))
nb_cotes = 0
nb_cotes = int(input("Le Nombre de Coté >"))
def forme(nb_cotes):
    for i in range (0,nb_cotes):
        T.forward(taille)
        T.left(360/nb_cotes)
def big_forme():
    longeurcote = int(input("nombre de forme sur le coté ? >"))
    for i in range(nb_cotes):
        for _ in range(longeurcote):
            forme(nb_cotes)
            T.pu
            T.forward(taille)
            T.pd
        T.left(360/nb_cotes)
big_forme()