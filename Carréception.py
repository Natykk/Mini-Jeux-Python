import turtle
import random
T = turtle.Turtle()
window = turtle.Screen()
T.speed(4)
couleurs = ["cyan", "purple", "green", "blue"]
taillecarre = int(input("taille du carré ? >"))
largeur = int(input("combien de carré de large ? >"))
hauteur = int(input("combien de carré de hauteur ? >"))
def carre(taillecarre):
    T.fillcolor('blue')
    T.begin_fill()
    for _ in range(0,4):
        T.color(random.choice(couleurs))
        T.forward(taillecarre)
        T.left(90)
    T.end_fill()


def changePos():
    T.penup    
    T.forward(taillecarre)
    T.left(90)


def groscarre():
    for _ in range(largeur):
        carre(taillecarre)
        T.pu         
        T.forward(taillecarre)
        T.pd
    changePos()
    for _ in range(hauteur):
        T.forward(taillecarre)
        carre(taillecarre)
    changePos()
    for _ in range(largeur):
        carre(taillecarre)
        T.pu         
        T.forward(taillecarre)
        T.pd
    changePos()
    for _ in range(hauteur):
        T.forward(taillecarre)
        carre(taillecarre)
groscarre()
window.exitonclick()