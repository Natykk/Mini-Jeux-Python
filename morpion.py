from tkinter import *
a=42 

# Trace les 4 lignes servant à délimiter les cases du plateau
def tracePlateau():
    MyCanvas.create_line(200, 0, 200,300)#vertical 2
    MyCanvas.create_line(100, 300, 100,0)# vertical 1
    MyCanvas.create_line(300,100,0,100)# horizontal 1
    MyCanvas.create_line(0,200,300,200)# horizontal 2

# Dessine une croix bleue à la position x,y
        #     <------0------->    <------1------->   <------2------->
# plateau =     [[0, 1, 2],          [0, 1, 2],         [0, 1, 2]]      


def traceCroix():
    global a 
    if a == 0:
        MyCanvas.create_line(23.3,76.7,76.7,23.3)
        MyCanvas.create_line(23.3,23.3,76.7,76.7)
        testGagne()
        
    if a == 1:
        MyCanvas.create_line(123.3,76.7,176.7,23.3)
        MyCanvas.create_line(123.3,23.3,176.7,76.7)
        testGagne()
        
    if a == 2:
        MyCanvas.create_line(223.3,76.7,276.7,23.3)
        MyCanvas.create_line(223.3,23.3,276.7,76.7)
        testGagne()
        
    if a == 3:
        MyCanvas.create_line(23.3,176.7,76.7,123.3)
        MyCanvas.create_line(23.3,123.3,76.7,176.7)
        testGagne()
        
    if a == 4:
        MyCanvas.create_line(123.3,176.7,176.7,123.3)
        MyCanvas.create_line(123.3,123.3,176.7,176.7)
        testGagne()
    if a == 5:
        MyCanvas.create_line(223.3,176.7,276.7,123.3)
        MyCanvas.create_line(223.3,123.3,276.7,176.7)
        testGagne()
        
    if a == 6:
        MyCanvas.create_line(23.3,276.7,76.7,223.3)
        MyCanvas.create_line(23.3,223.3,76.7,276.7)
        testGagne()
        
    if a == 7:
        MyCanvas.create_line(123.3,276.7,176.7,223.3)
        MyCanvas.create_line(123.3,223.3,176.7,276.7)
        testGagne()

        
    if a == 8:
        MyCanvas.create_line(223.3,276.7,276.7,223.3)
        MyCanvas.create_line(223.3,223.3,276.7,276.7)
        testGagne()
        
    

# Dessine un rond rouge à la position x,y
def traceRond():
    global a
    if a == 0:
        MyCanvas.create_oval(23.3,76.7,76.7,23.3)
        MyCanvas.create_oval(23.3,23.3,76.7,76.7)
        testGagne()
    if a == 1:
        MyCanvas.create_oval(123.3,76.7,176.7,23.3)
        MyCanvas.create_oval(123.3,23.3,176.7,76.7)
        testGagne()
    if a == 2:
        MyCanvas.create_oval(223.3,76.7,276.7,23.3)
        MyCanvas.create_oval(223.3,23.3,276.7,76.7)
        testGagne()
    if a == 3:
        MyCanvas.create_oval(23.3,176.7,76.7,123.3)
        MyCanvas.create_oval(23.3,123.3,76.7,176.7)
        testGagne()
    if a == 4:
        MyCanvas.create_oval(123.3,176.7,176.7,123.3)
        MyCanvas.create_oval(123.3,123.3,176.7,176.7)
        testGagne()
    if a == 5:
        MyCanvas.create_oval(223.3,176.7,276.7,123.3)
        MyCanvas.create_oval(223.3,123.3,276.7,176.7)
        testGagne()
    if a == 6:
        MyCanvas.create_oval(23.3,276.7,76.7,223.3)
        MyCanvas.create_oval(23.3,223.3,76.7,276.7)
        testGagne()
    if a == 7:
        MyCanvas.create_oval(123.3,276.7,176.7,223.3)
        MyCanvas.create_oval(123.3,223.3,176.7,276.7)
        testGagne()
    if a == 8:
        MyCanvas.create_oval(223.3,276.7,276.7,223.3)
        MyCanvas.create_oval(223.3,223.3,276.7,276.7)
        testGagne()
        
    



# Repond à l'évènement button-1 quand le joueur clique dans le canvas
#   Déterminer les coordonnées de la case cliquée
#   Mettre une croix ou un rond dedans suivant le joueur en cours
#   Mettre à jour la liste plateau
#   Tester si le joueur a gagné
#   Tester si le plateau est rempli
#   Changer le joueur en cours
def clickFenetre(event):
    global joueur, plateau , a
    xe = event.x
    ye = event.y
    if 0<xe<100:
        if 0<ye<100:
            print("0")
            if joueur == 0 :
                a=0
                joueur = 1
                plateau[0][0] = 1
                traceCroix()
            else:
                a=0
                joueur = 0
                plateau[0][0] = 0
                traceRond()
        if 100<ye<200:
            print("3")
            if joueur == 0 :
                a=3
                joueur = 1
                plateau[1][0] = 1
                traceCroix()
            else:
                a=3
                joueur = 0
                plateau[1][0] = 0
                traceRond()
        if 200<ye<300:
            print("6")
            if joueur == 0 :
                a=6
                joueur = 1
                plateau[2][0] = 1
                traceCroix()
            else:
                a=6
                joueur = 0
                plateau[2][0] = 0
                traceRond()
    if 100<xe<200:
        if 0<ye<100:
            print("1")
            if joueur == 0 :
                a=1
                joueur = 1
                plateau[0][1] = 1
                traceCroix()
            else:
                a=1
                joueur = 0
                plateau[0][1] = 0
                traceRond()
        if 100<ye<200:
            print("4")
            if joueur == 0 :
                a=4
                joueur = 1
                plateau[1][1] = 1
                traceCroix()
            else:
                a=4
                joueur = 0
                plateau[1][1] = 0
                traceRond()
        if 200<ye<300:
            print("7")
            if joueur == 0 :
                a=7
                joueur = 1
                plateau[2][1] = 1
                traceCroix()
            else:
                a=7
                joueur = 0
                plateau[2][1] = 0
                traceRond()
    if 200<xe<300:
        if 0<ye<100:
            print("2")
            if joueur == 0 :
                a=2
                joueur = 1
                plateau[0][2] = 1
                traceCroix()
            else:
                a=2
                joueur = 0
                plateau[0][2] = 0
                traceRond()
        if 100<ye<200:
            print("5")
            if joueur == 0 :
                a=5
                joueur = 1
                plateau[1][2] = 1
                traceCroix()
            else:
                a=5
                joueur = 0   
                plateau[1][2] = 0 
                traceRond()
        if 200<ye<300:
            print("8")
            if joueur == 0 :
                a=8
                joueur = 1
                plateau[2][2] = 1
                traceCroix()
            else:
                a=8
                joueur = 0
                plateau[2][2] = 0
                traceRond()
# Teste les différentes combinaisons gagnantes et affiche un message si un joueur gagne
#           [[0, 1, 2],   [0][0],[0][1],[0][2] // [1][0],[1][1],[1][2] // [2][0],[2][1],[2][2] // [0][0],[1][0],[2][0] // [0][1],[1][1],[2][1] // [0][2],[1][2],[2][2] 
#           [3, 4, 5],    [0][0],[1][1],[2][2] // [0][2],[1][1],[2][0]
#           [6, 7, 8]]    Les combinaisons gagnantes sont : 012/345/678/036/147/258/048/246     Egalité : 0 3 1 2 4 7 6 8 5
#
def testGagne():
    plateauRempli()
    global jeuTermine
    if plateau[0][0] == 0 and plateau[0][1] == 0  and plateau[0][2] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    if plateau[1][0] == 0 and plateau[1][1] == 0  and plateau[1][2] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    if plateau[2][0] == 0 and plateau[2][1] == 0  and plateau[2][2] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    if plateau[0][0] == 0 and plateau[1][0] == 0  and plateau[2][0] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    if plateau[0][1] == 0 and plateau[1][1] == 0  and plateau[2][1] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    if plateau[0][2] == 0 and plateau[1][2] == 0  and plateau[2][2] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    if plateau[0][0] == 0 and plateau[1][1] == 0  and plateau[2][2] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    if plateau[0][2] == 0 and plateau[1][1] == 0  and plateau[2][0] == 0:
        svLabel.set("O WIN !")
        print(plateau)
    
    if plateau[0][0] == 1 and plateau[0][1] == 1  and plateau[0][2] == 1:
        svLabel.set("X WIN !")
        print("X1")
        print(plateau)
    if plateau[1][0] == 1 and plateau[1][1] == 1  and plateau[1][2] == 1:
        svLabel.set("X WIN !")
        print("X2")
        print(plateau)
    if plateau[2][0] == 1 and plateau[2][1] == 1  and plateau[2][2] == 1:
        svLabel.set("X WIN !")
        print("X3")
        print(plateau)
    if plateau[0][0] == 1 and plateau[1][0] == 1 and plateau[2][0] == 1:
        svLabel.set("X WIN !")
        print("X4")
        print(plateau)
    if plateau[0][1] == 1 and plateau[1][1] == 1  and plateau[2][1] == 1:
        svLabel.set("X WIN !")
        print("X5")
        print(plateau)
    if plateau[0][2] == 1 and plateau[1][2] == 1  and plateau[2][2] == 1:
        svLabel.set("X WIN !")
        print("X6")
        print(plateau)
    if plateau[0][0] == 1 and plateau[1][1] == 1  and plateau[2][2] == 1:
        svLabel.set("X WIN !")
        print("X7")
        print(plateau)
    if plateau[0][2] == 1 and plateau[1][1] == 1  and plateau[2][0] == 1:
        print(plateau)
        svLabel.set("X WIN !")
        print("X8")

# Teste s'il reste une case libre dans le plateau et affiche un message sinon
def plateauRempli():
    global jeuTermine
    #if plateau.count(42) == 0:
    #    print(plateau)
    #    print("egalité")
    #    jeuTermine = True
    #    svLabel.set("EGALITE !")
        
def popup():
    fInfos = Toplevel()		  # Popup -> Toplevel()
    fInfos.title('Tableau Rempli')
    Button(fInfos, text='Quitter', command=reset).pack()
    fInfos.transient(MyWindow) 	  # Réduction popup impossible 
    fInfos.grab_set()		  # Interaction avec fenetre jeu impossible
    MyWindow.wait_window(fInfos)   # Arrêt script principal

# Réinitialise le jeu
#   Vide la liste plateau
#   Efface le canvas
#   Ré-affiche le plateau
def reset():
    global joueur, plateau, jeuTermine
    plateau = [[None, None, None],[None, None, None], [None, None, None]]
    MyCanvas.create_rectangle(0,0,500,500,fill='white',outline ='white')
    tracePlateau()
    joueur = 0
    jeuTermine = False
    svLabel.set("Jeu en cours...")
    
        

#crée la fenêtre
MyWindow = Tk()
MyWindow.title('Morpion')
# crée le canvas dans la fenêtre
MyCanvas = Canvas(MyWindow, width = 300, height = 300, bg ='white')
MyCanvas.pack(padx =5, pady =5)
MyCanvas.focus_set()

# Crée les deux boutons de la fenêtre
Button(MyWindow, text ='Exit', command = MyWindow.destroy).pack(side=RIGHT,padx=5,pady=5)
Button(MyWindow, text ='Reset', command = reset).pack(side=LEFT,padx=5,pady=5)

#Crée le label qui servira à informer les joueurs
svLabel = StringVar()
texteLabel = Label(MyWindow, textvariable=svLabel)
texteLabel.pack(side = BOTTOM, pady=15)
svLabel.set("Jeu en cours...")

# Bind le bouton de la souris vers la procedure clickFenetre
MyCanvas.bind("<Button-1>", clickFenetre)

# Initialise les variables
joueur = 0
jeuTermine = False
plateau = [[None, None, None],
           [None, None, None], 
           [None, None, None]]


# Dessine le pateau
tracePlateau()

# Boucle principale de tkinter - Lance le jeu
MyWindow.mainloop()
