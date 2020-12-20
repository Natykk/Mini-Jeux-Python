import sys
import os
from tkinter import *
from tkinter.messagebox import *
import random
MyWindow = Tk()
MyWindow.title('Pong')
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#-------------------Fonction pour les mouvement avec le clavier ------------#
def KeyBoard(event):
    global PosX,PosY,PosX2,PosY2,PosX1,PosY1
    Key = event.keysym
    if Key == 'Up': #Haut
        if PosY >10:
            PosY -= 20
    if Key == 'Down': #Bas
        if PosY<310:
            PosY +=20
    if Key == 'Right': #Droite
        if PosX<460:
            PosX += 20
    if Key == 'Left': #Gauche
        if PosX>10:
            PosX -= 20
    if Key == 'z': #Haut
        if PosY2 >10:
            PosY2 -= 20
    if Key == 's': #Bas
        if PosY2<250:
            PosY2+=20
    if Key == 'Up': #Haut
        if PosY1 >10:
            PosY1 -= 20
    if Key == 'Down': #Bas
        if PosY1<250:
            PosY1 +=20
    MyCanvas.coords(raquette,PosX1 -10, PosY1, PosX1 +10, PosY1 +72)
    MyCanvas.coords(raquette2,PosX2 -10, PosY2, PosX2 +10, PosY2 +72)
#--------------------------------------------------------------------------#
#-----------Toute les Variables-------------#
PosY1 = 150 # raquette 1
PosX1 = 460 # raquette 1
PosX2 = 20  # raquette 2
PosY2 = 150 # raquette 2
PosX = 160 # Position x aléatoire des balles.
PosY = 200 # Position y aléatoire des balles.
sensX = 1
sensY = 1
#--------------------------------------------#
#---------Dessine les différente figure---------#
MyCanvas = Canvas(MyWindow, width = 480, height =320, bg ='white')
raquette2= MyCanvas.create_rectangle(PosX2-10,PosY2,PosX2+10,PosY2+72,width=5,outline='blue',fill='blue')
raquette= MyCanvas.create_rectangle(PosX1-10,PosY1,PosX1+10,PosY1+72,width=5,outline='red',fill='red')
balle = MyCanvas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,outline='grey',fill='grey')
#-----------------------------------------------#
#---------------Fonction de déplacement --------#
def deplacement():
    global sensX , sensY , PosX , PosY
    if PosX == 480:
        popup()
        sensX = -1
    elif PosX == 0:
        popup()
        sensX = +1
    if PosY == 320:
        sensY = -1
    elif PosY == 0:
        sensY = +1
    if (PosY <= PosY1+70 or PosY <= PosY1) and(PosX == 450):
        sensX = -1
    if (PosY <= PosY2+70 or PosY <= PosY2) and(PosX == 30):
        sensX = +1
    PosX += sensX
    PosY += sensY
    MyCanvas.move(balle,sensX,sensY)
    MyWindow.after(5,deplacement) 
#-----------------------------------------------#
def popup():
    fInfos = Toplevel()		  # Popup -> Toplevel()
    fInfos.title('PERDU!')
    Button(fInfos, text='Quitter', command=restart_program).pack()
    fInfos.transient(MyWindow) 	  # Réduction popup impossible 
    fInfos.grab_set()		  # Interaction avec fenetre jeu impossible
    MyWindow.wait_window(fInfos)   # Arrêt script principal
#-----------------------------------------------#
MyCanvas.focus_set()
MyCanvas.bind('<Key>',KeyBoard)
MyCanvas.pack(padx =25, pady =25)
Button(MyWindow, text ='Quitter', command = MyWindow.destroy).pack(side=LEFT,padx=10,pady=5)
deplacement()
MyWindow.mainloop()
