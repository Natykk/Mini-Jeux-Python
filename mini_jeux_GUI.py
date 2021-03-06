from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import *
import random
list_joueur=[""]
list_débat=["Beurre Doux ou Demi-sel","Céréal Avant ou Après le lait","Pain au Chocolat ou Chocolatine"]
#e1 = joueur
#e2 = débat
#def show_e1():
#    print("Liste des Joueurs: %s" % (list_joueur))
#def show_e2():
#    print("Liste des Mini-Débats: %s" % (list_débat))

def add_e1():
    temp = e1.get()
    list_joueur.append(temp)

def add_e2():
    temp2 = e2.get()
    list_débat.append(temp2)

#def tirage_e2():
#    print(random.choice(list_débat))


#def tirage_e1():
#    print(random.choice(list_joueur))

def popup_quel_debat():
    fInfos = Toplevel()		  # Popup -> Toplevel()
    fInfos.title('DEBAT !')
    rd_debat = random.choice(list_débat)
    Button(fInfos, text='Quitter', command=fInfos.destroy).pack(padx=20, pady=20)
    tk.Label(fInfos,text=rd_debat).pack(padx=10, pady=10)
    fInfos.transient(master) 	  # Réduction popup impossible 
    fInfos.grab_set()		  # Interaction avec fenetre jeu impossible
    master.wait_window(fInfos)   # Arrêt script principal

def popup_intru():
    fInfos = Toplevel()		  # Popup -> Toplevel()
    fInfos.title('INTRUS !')
    rd_intru = random.choice(list_joueur)
    Button(fInfos, text='Quitter', command=fInfos.destroy).pack(padx=20, pady=20)
    tk.Label(fInfos,text=rd_intru).pack(padx=10, pady=10)
    fInfos.transient(master) 	  # Réduction popup impossible 
    fInfos.grab_set()		  # Interaction avec fenetre jeu impossible
    master.wait_window(fInfos)   # Arrêt script principal



def popup_pj():
    fInfos = Toplevel()		  # Popup -> Toplevel()
    fInfos.title('Infos')
    Button(fInfos, text='Quitter', command=fInfos.destroy).pack(padx=20, pady=20)
    tk.Label(fInfos,text=list_joueur).pack(padx=10, pady=10)
    fInfos.transient(master) 	  # Réduction popup impossible 
    fInfos.grab_set()		  # Interaction avec fenetre jeu impossible
    master.wait_window(fInfos)   # Arrêt script principal

def popup_debat():
    fInfos = Toplevel()		  # Popup -> Toplevel()
    fInfos.title('Infos')
    Button(fInfos, text='Quitter', command=fInfos.destroy).pack(padx=20, pady=1)
    tk.Label(fInfos,text=list_débat).pack(padx=10, pady=10)
    fInfos.transient(master) 	  # Réduction popup impossible 
    fInfos.grab_set()		  # Interaction avec fenetre jeu impossible
    master.wait_window(fInfos)   # Arrêt script principal

master = tk.Tk()
master.title('Mini-Jeu')
tk.Label(master,text="Ajouter des joueurs").grid(row=0)
tk.Label(master,text="Ajouter des Mini-Débats").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)



tk.Button(master, text='Ajouter les joueurs', command=add_e1).grid(row=2)#row=4, column=1, sticky=tk.W, pady=2) # Bouton pour ajouter des joueurs dans list_joueur
tk.Button(master,text="Tirage de L\'intrus",command=popup_intru).grid(row=2,column=1)#row=3, column=0, sticky=tk.W, pady=4) # Bouton pour tiré en mode random  le joueur intrus
tk.Button(master, text='Quel joueur son inscrit ?', command=popup_pj).grid(row=2,column=3)#row=3, column=1, sticky=tk.W, pady=1) # Bouton pour Afficher la fenetre qui montre tout les joueurs



tk.Button(master, text='Ajouter des Mini-débats', command=add_e2).grid(row=3)#row=4, column=2, sticky=tk.W, pady=2) # Bouton pour Ajouter des débats dans list_débat
tk.Button(master,text='Tirage du Débat', command=popup_quel_debat).grid(row=3,column=1)#row=2, column=0, sticky=tk.W, pady=4) # Bouton pour
tk.Button(master,text='Quel Mini-débat sont inscrit ?', command=popup_debat).grid(row=3,column=3)#row=3, column=2, sticky=tk.W, pady=1) # Bouton pour

tk.Button(master,text='Quitter',command=master.quit).grid(row=5,column=1)#row=4, column=0, sticky=tk.W, pady=4) # Bouton pour 

tk.mainloop()