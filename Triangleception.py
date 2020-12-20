import turtle
import random
T = turtle.Turtle()
T.speed(4)
couleurs = ["cyan", "purple", "green", "blue"]
taillecarre = 50
largeur = 5
hauteur = 5
def carre(taillecarre):
    for _ in range(0,3):
        T.color(random.choice(couleurs))
        T.forward(taillecarre)
        T.left(120)

def changePos(): 
    T.penup    
    T.forward(taillecarre)
    T.left(120)


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
        T.end_fill()
    changePos()
    for _ in range(largeur):
        carre(taillecarre)
        T.end_fill()
        T.filling()
        T.pu         
        T.forward(taillecarre)
        T.pd


groscarre()
