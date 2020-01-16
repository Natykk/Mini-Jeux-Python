from tkinter import *
from random import random
import os
from math import *
vitesseSaut = 30
vitesseMouton = 70

#------------------------------------------------
# Gestion du personnage
#------------------------------------------------

# initie le saut. La variable flagSaute sert à bloquer le déplacement latéral pendant le saut
def saute(event):
    MyCanvas.after(vitesseSaut,monte)
    print('saute')
# sens montée
# Si le personnage est en haut, il redescend
def monte():
    MyCanvas.move(personnage,-15.2,-14)
    if MyCanvas.coords(personnage)[1] < 105:
        MyCanvas.after(vitesseSaut,descend)
    else:
        MyCanvas.after(vitesseSaut,monte)
    print("monte")
# sens descente
# Si le personnage est en bas, le saut s'arrête
def descend():
    if MyCanvas.coords(personnage)[1] < 180:
        MyCanvas.move(personnage,-15.2,14)
        MyCanvas.after(vitesseSaut,descend)
    print('descend')
# Déplacement latéral
# Si un saut n'est pas en cours le personnage se déplace vers la droite
def droite(event):
    if MyCanvas.coords(personnage)[0] < 960:
        print('droite')
        MyCanvas.move(personnage,30,0)

#------------------------------------------------
# Gestion des moutons
#------------------------------------------------

# Crée un mouton si un nombre aléatoire est inférieur à 0.2
# le nouveau mouton est ajouté au début de la liste
def creeMouton():
    if random() < 0.2:
        listeMoutons.insert(0,MyCanvas.create_image(300, 290, image = mouton))
    MyCanvas.after(800,creeMouton)

# Déplace tous les moutons de la liste
# Déruit le premier mouton s'il est sorti de l'écran
def deplaceMoutons():
    for m in listeMoutons:
        MyCanvas.move(m,10,0)
    if len(listeMoutons)!= 0:
        if MyCanvas.coords(listeMoutons[-1])[0] > 1000:
            MyCanvas.delete(listeMoutons.pop())
    MyCanvas.after(vitesseMouton,deplaceMoutons)
#COLLISION
def collision():
    if len(MyCanvas.find_overlapping(MyCanvas.coords(personnage)[0],MyCanvas.coords(personnage)[1],MyCanvas.coords(personnage)[0]+82,MyCanvas.coords(personnage)[1]+149))>1:
        print("perdu")
    MyCanvas.after(100,collision)



#------------------------------------------------
# Lance le jeu
# Si le jeu n'a pas déjà été lancé,
# démarre la création des moutons et leur déplacement
#------------------------------------------------
def lanceJeu():
    global jeuLance
    if not jeuLance:
        MyCanvas.after(800,creeMouton)
        MyCanvas.after(vitesseMouton,deplaceMoutons)
        MyCanvas.after(1,collision)
        jeuLance = True


#variables globales
listeMoutons = []
flagSaute = False
jeuLance = False

#crée la fenêtre
MyWindow = Tk()
MyWindow.title('Saute-moutons')

# crée le canvas dans la fenêtre
MyCanvas = Canvas(MyWindow, width = 960, height = 320, bg ='white')
MyCanvas.pack(padx =50, pady =50)
MyCanvas.focus_set()
# Crée les images et affiche le personnage
mouton = PhotoImage(file='mouton.png')
perso = PhotoImage(file='personnage.png')
personnage = MyCanvas.create_image(800, 180,anchor=NW, image = perso)
# Crée les deux boutons de la fenêtre
Button(MyWindow, text ='Exit', command = MyWindow.destroy).pack(side=RIGHT,padx=5,pady=5)
Button(MyWindow, text ='Start', command = lanceJeu).pack(side=TOP,padx=5,pady=5)
# Affecte les fonctions aux touches
MyCanvas.bind("<space>", saute)
MyCanvas.bind("<Right>", droite)
# Boucle principale de tkinter
MyWindow.mainloop()
