import random
import sys
import tkinter as tk
import time

### Partie A1 ###

def paquet():
    """Initialise et renvoie un paquet de 52 cartes."""
    couleurs = ['carreau','pique','trefle','coeur']
    rangs = ['as','2','3','4','5','6','7','8','9','10','valet','dame','roi']
    cartes = []
    for couleur in couleurs :
        for rang in rangs :
            cartes.append(rang+' de '+couleur) #Nomination de la carte en fonction de sa couleur et valeur
    return cartes

def valeurCarte(carte):
    """Pour une carte donnée, renvoie sa valeur en points."""
    if 'as' in carte :
        valeur = 11 #Inisialisation de la variable
    elif ('valet' in carte) or ('dame' in carte) or ('roi' in carte):
        valeur = 10 #Valeur des têtes
    else:
        valeur = int(str(carte.split(' ')[0])) #Valeur des autres cartes
    return valeur

def initPioche(n=8):
    """Prend un nombre de paquets egal au nombre de joueurs puis melange
    les cartes pour creer la pioche."""
    pioche_non_melangees = n*paquet()
    pioche = [] #Initialisation de la pioche melangee
    quantite = len(pioche_non_melangees) #Nb de cartes à trier
    for i in range(quantite):
        carte = random.choice(pioche_non_melangees)
        pioche.append(carte) #Ajoute une carte aléatoire dans la pioche mélangée
        pioche_non_melangees.remove(carte) #Et la retire de la pioche à mélanger
    return pioche

def piocheCarte(p, x=1):
    """Recoit en argument la pioche, et le nombre de cartes à piocher (par
    defaut 1), et retourne les x premieres cartes de la pioche (en les
    retirant)."""
    cartesPiochees = []
    for i in range(x):
        cartesPiochees.append(p.pop(0)) #Tire une carte de la pioche
    if x==1:
        return cartesPiochees[0]
    else :
        return cartesPiochees

### Partie A2 ###
    
def initJoueurs():
    liste_joueurs = []
    global nb_joueurs
    nb_joueurs = 0

    #Fenetre d'initialisation des joueurs
    ask_joueurs = tk.Tk()
    ask_joueurs.overrideredirect(1)
    ask_joueurs.geometry('200x300+600+200')
    ask_joueurs.title('Initialisation des joueurs')
    ask_joueurs.wm_attributes("-topmost", 1)

    #Etiquette nombre joueurs
    label_nb_joueurs = tk.Label(ask_joueurs, text='Nombre de joueurs :')
    label_nb_joueurs.pack()

    #Entree du nombre de joueurs
    entree_nb = tk.IntVar()
    entree_nb_joueurs = tk.Entry(ask_joueurs, textvariable=entree_nb)
    entree_nb_joueurs.pack()

    #Bouton valider le nombre de joueur
    bouton_valider_nb = tk.Button(ask_joueurs, text='Valider', command=lambda:valider_nb(ask_joueurs, entree_nb_joueurs))
    bouton_valider_nb.pack()

    #Etiquette joueur 1
    label_joueur1 = tk.Label(ask_joueurs, text='Joueur 1 :')
    label_joueur1.pack()

    #Entree joueur 1
    joueur1 = tk.StringVar()
    joueur1.set('Joueur 1')
    entree_joueur1 = tk.Entry(ask_joueurs, textvariable=joueur1, state='disabled')
    entree_joueur1.pack()

    #Etiquette joueur 2
    label_joueur2 = tk.Label(ask_joueurs, text='Joueur 2 :')
    label_joueur2.pack()

    #Entree joueur 2
    joueur2 = tk.StringVar()
    joueur2.set('Joueur 2')
    entree_joueur2 = tk.Entry(ask_joueurs, textvariable=joueur2, state='disabled')
    entree_joueur2.pack()

    #Etiquette joueur 3
    label_joueur3 = tk.Label(ask_joueurs, text='Joueur 3 :')
    label_joueur3.pack()

    #Entree joueur 3
    joueur3 = tk.StringVar()
    joueur3.set('Joueur 3')
    entree_joueur3 = tk.Entry(ask_joueurs, textvariable=joueur3, state='disabled')
    entree_joueur3.pack()

    #Etiquette joueur 4
    label_joueur4 = tk.Label(ask_joueurs, text='Joueur 4 :')
    label_joueur4.pack()

    #Entree joueur 4
    joueur4 = tk.StringVar()
    joueur4.set('Joueur 4')
    entree_joueur4 = tk.Entry(ask_joueurs, textvariable=joueur4, state='disabled')
    entree_joueur4.pack()

    #Etiquette joueur 5
    label_joueur5 = tk.Label(ask_joueurs, text='Joueur 5 :')
    label_joueur5.pack()

    #Entree joueur 5
    joueur5 = tk.StringVar()
    joueur5.set('Joueur 5')
    entree_joueur5 = tk.Entry(ask_joueurs, textvariable=joueur5, state='disabled')
    entree_joueur5.pack()

    #Bouton valider joueurs
    bouton_valider_joueurs = tk.Button(ask_joueurs, text='Valider', command=lambda:valider_joueurs(ask_joueurs,liste_joueurs,entree_joueur1,entree_joueur2
                                                                                                   ,entree_joueur3,entree_joueur4,entree_joueur5))
    bouton_valider_joueurs.pack()

    ask_joueurs.mainloop()
    
    return liste_joueurs

def initScores(joueurs,v=0):
    scores = {}
    for joueur in joueurs :
        scores[joueur] = v
    return scores

def premierTour(joueurs, pioche):
    scores = initScores(joueurs)
    for joueur in joueurs:
        cartes_piochees = piocheCarte(pioche,x=2)
        for carte in cartes_piochees :
            scores[joueur] += valeurCarte(carte)
    return scores

def gagnants(scores):
    maxi = 0
    gagnants = []
    for joueur in scores.keys() :
        if scores[joueur] <=21 and scores[joueur]>maxi:
            maxi = scores[joueur]
            gagnants = []
            gagnants.append(joueur)
        if scores[joueur] == maxi:
            gagnants.append(joueur)
    return gagnants

### Partie B1 ###

def continuer():
    global continuer
    continuer = -1
    while continuer!=0 and continuer!=1:
        pass
    if continuer == 0:
        return False
    else:
        return True

def tourJoueur(j, scores, pioche):
    while scores[j]<21 and continuer():
        scores[j] += valeurCarte(piocheCarte(pioche))
    return scores

### Partie B2 ###

def tourComplet(joueurs, scores, pioche):
    for j in joueurs:
        scores = tourJoueur(j, scores, pioche)
    return scores

def partieComplete():
    joueurs = initJoueurs()
    scores = initScores(joueurs)
    pioche = initPioche()
    scores = tourComplet(joueurs, scores, pioche)
    gagnants = gagnants(score)
    return gagnants 
    
############################
### FONCTIONS GRAPHIQUES ###
############################

#----------Section Menu-------------#

   #----------------------------------#
def valider_nb(fenetre, entree):
    global nb_joueurs
    nb_joueurs = int(entree.get())
    i = 0
    for widget in fenetre.winfo_children() :
        if widget.winfo_class() == 'Entry' :
            if i > 0 and i <= nb_joueurs:
                widget.config(state='normal')
            i += 1

def valider_joueurs(fenetre,liste,entree1,entree2,entree3,entree4,entree5):
    liste.append(entree1.get())
    liste.append(entree2.get())
    liste.append(entree3.get())
    liste.append(entree4.get())
    liste.append(entree5.get())
    fenetre.destroy()
    can.delete(main, menu)
 
def nouvelle_partie(main, can, menu):
    """Lance une nouvelle partie de Blackjack"""
    for widget in main.winfo_children():
        if widget.winfo_class() == 'Button' :
            tk.Button.destroy(widget)

    gagnants = partieComplete()
    can.delete(main, menu)
    creerBoutons(main, can)

   #----------------------------------#

def reprendre_partie(main, can, menu):
    """Reprend la partie interrompue"""
    for widget in main.winfo_children():
        if widget.winfo_class() == 'Button' :
            tk.Button.destroy(widget)
    can.delete(main, menu)
    creerBoutons(main, can)

def menu(main, can, resume=True):
    """Affiche le menu au demarrage du jeu"""
    w = main.winfo_screenwidth() #Largeur de l'ecran
    h = main.winfo_screenheight() #Hauteur de l'ecran
    
    #Suppression des boutons de partie
    for widget in main.winfo_children():
        if widget.winfo_class() == 'Button' :
            tk.Button.destroy(widget)
    
    #Fond noirci du menu
    menu = can.create_rectangle(0,0,w,h,width=1,fill="black",stipple="gray75")

    #Bouton quitter
    bouton_quitter = tk.Button(main, text='Quitter', bg='black', fg='yellow', activebackground='yellow', activeforeground='black', command=main.destroy)
    bouton_quitter_win = can.create_window(w/2, 3*h/4, window=bouton_quitter)

    #Bouton nouvelle partie
    bouton_nouvelle_partie = tk.Button(main, text='Nouvelle Partie', bg='black', fg='yellow', activebackground='yellow', activeforeground='black',
                                       command=lambda:nouvelle_partie(main,can,menu))
    bouton_nouvelle_partie_win = can.create_window(w/2, h/4, window=bouton_nouvelle_partie)

    #Bouton reprendre partie
    bouton_reprendre = tk.Button(main, text='Reprendre', bg='black', fg='yellow', activebackground='yellow', activeforeground='black',
                                       command=lambda:nouvelle_partie(main,can,menu))
    bouton_reprendre_win = can.create_window(w/2, h/2, window=bouton_reprendre)

    if not resume :
        bouton_reprendre.config(state='disabled') #Desactive le bouton reprendre au demarrage du jeu

#----------Section Boutons----------#

def splitter():
    """Action servant à splitter deux cartes identiques."""
    pass

def rester():
    """Permet au joueur d'arreter son tour."""
    global continuer
    continuer = 0

def tirer():
    """Permet au joueur de tirer une carte."""
    global continuer
    continuer = 1

def doubler():
    """Permet au joueur de doubler sa mise et tirer une unique carte."""
    pass

def creerBoutons(main, can):
    """Creer les boutons permettant au joueur d'interagir."""
    k = main.winfo_screenwidth()/5 #Ecart des boutons
    y = main.winfo_screenheight()-30 #Hauteur des boutons
    
    #Bouton splitter
    bouton_splitter = tk.Button(main, text='Splitter', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=splitter)
    bouton_splitter_win = can.create_window(k, y, window=bouton_splitter)

    #Bouton rester
    bouton_rester = tk.Button(main, text='Rester', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=rester)
    bouton_rester_win = can.create_window(2*k, y, window=bouton_rester)

    #Bouton tirer
    bouton_tirer = tk.Button(main, text='Tirer', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=tirer)
    bouton_tirer_win = can.create_window(3*k, y, window=bouton_tirer)

    #Bouton doubler
    bouton_doubler = tk.Button(main, text='Doubler', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=doubler)
    bouton_doubler_win = can.create_window(4*k, y, window=bouton_doubler)

    #Bouton menu
    bouton_menu = tk.Button(main, text='Menu', bg='black', fg='yellow', activebackground='yellow', activeforeground='black',
                            command=lambda:menu(main,can))
    bouton_menu_win = can.create_window(40, 30, window=bouton_menu)

#----------Section Cartes-----------#
    
def associerCartes(cartes):
    """Associe chaque carte d'un paquet donné à son image sur l'application graphique."""
    association = {} #Initialisation du dictionnaire d'association
    for carte in cartes :
        couleur = carte.split(' ')[2] #Prends la couleur de la carte
        rang = carte.split(' ')[0][0] #Prends le rang de la carte (ou sa premiere lettre)
        if rang == '1' :
            rang = '10'
        association[carte] = rang+'-'+couleur+'.png' #Retrouve l'image correspondant à la carte
    return association

def trouverCarte(association, carte):
    """Trouve l'image d'une carte donnée dans une association carte/image."""
    return association[carte]

### Programme principal (brouillon et tests pour l'instant) ###

def main_prog():
    main = tk.Tk()
    w = main.winfo_screenwidth() #Largeur de l'ecran
    h = main.winfo_screenheight() #Hauteur de l'ecran
    main.title('Jeu de blackjack') #Creation de la fenetre
    main.attributes('-fullscreen', 1)
    main.resizable(height=False,width=False)
    
    table = tk.PhotoImage(file='Images/table_blackjack.gif') #Importation de l'arriere-plan
    fond = tk.Canvas(main, height=h, width=w, bg='black') #Creation du canvas allant accueillir l'interface graphique
    fond.pack()
    fond.create_image(0,0,anchor=tk.NW,image=table) #Image d'arriere-plan

    menu(main,fond,resume=False)
    
    main.mainloop()
    

main_prog()
