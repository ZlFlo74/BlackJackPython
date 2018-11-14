import random
import sys
import tkinter as tk

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
        valeur = 0 #Inisialisation de la variable
        while valeur!=1 and valeur!=11:
            valeur = int(input('1 ou 11 ?')) #Choix de la valeur de l'As
    elif ('valet' in carte) or ('dame' in carte) or ('roi' in carte):
        valeur = 10 #Valeur des têtes
    else:
        valeur = str(carte.split(' ')[0]) #Valeur des autres cartes
    return valeur

def initPioche(n):
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
    return cartesPiochees

### Partie A2 ###

def initJoueurs(n):
    liste_joueurs = []
    for i in range(n):
        ask = tk.Tk() #Cree une fenetre demandant le nom du joueur

        question = tk.Label(ask, text='Nom du joueur '+str(i+1)+' : ')
        question.pack()
        
        nom = tk.StringVar()
        entree_nom = tk.Entry(ask, textvariable=nom)
        entree_nom.pack()

        bouton_valider = tk.Button(ask, text='Valider', command=lambda:liste_joueurs.append(entree_nom.Get()))
        bouton_valider.pack()
        
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

def partie():
    liste_joueurs = initJoueurs(5)
    pioche = initPioche(5)
    scores = premierTour(liste_joueurs, pioche)
    
############################
### FONCTIONS GRAPHIQUES ###
############################

#----------Section Menu-------------#

def nouvelle_partie(main, can, menu):
    """Lance une nouvelle partie de Blackjack"""
    for widget in main.winfo_children():
        if widget.winfo_class() == 'Button' :
            tk.Button.destroy(widget)
    can.delete(main, menu)
    creerBoutons(main, can)

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
        bouton_reprendre.config(state=tk.DISABLED) #Desactive le bouton reprendre au demarrage du jeu

#----------Section Boutons----------#

def splitter():
    """Action servant à splitter deux cartes identiques."""
    pass

def rester():
    """Permet au joueur d'arreter son tour."""
    pass

def tirer():
    """Permet au joueur de tirer une carte."""
    pass

def doubler():
    """Permet au joueur de doubler sa mise et tirer une unique carte."""
    pass

def creerBoutons(main, can):
    """Creer les boutons permettant au joueur d'interagir."""
    k = main.winfo_screenwidth()/5 #Ecart des boutons
    y = main.winfo_screenheight()-30 #Hauteur des boutons
    
    #Bouton splitter
    #bouton_splitter = tk.Button(main, text='Splitter', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=splitter)
    #bouton_splitter_win = can.create_window(k, y, window=bouton_splitter)

    #Bouton rester
    bouton_rester = tk.Button(main, text='Rester', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=rester)
    bouton_rester_win = can.create_window(2*k, y, window=bouton_rester)

    #Bouton tirer
    bouton_tirer = tk.Button(main, text='Tirer', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=tirer)
    bouton_tirer_win = can.create_window(3*k, y, window=bouton_tirer)

    #Bouton doubler
    #bouton_doubler = tk.Button(main, text='Doubler', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=doubler)
    #bouton_doubler_win = can.create_window(4*k, y, window=bouton_doubler)

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

def prog_script():
    pass

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
