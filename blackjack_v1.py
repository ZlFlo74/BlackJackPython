import random
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

def piocheCarte(p, x=1):
    """Recoit en argument la pioche, et le nombre de cartes à piocher (par
    defaut 1), et retourne les x premieres cartes de la pioche (en les
    retirant)."""
    cartesPiochees = []
    for i in range(x):
        cartesPiochees.append(p.pop(0)) #Tire une carte de la pioche
    return cartesPiochees

### Partie A2 ###

############################
### FONCTIONS GRAPHIQUES ###
############################

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
    bouton_splitter = tk.Button(main, text='Splitter', bg='blue', fg='white', activebackground='white', activeforeground='blue', command=splitter)
    bouton_splitter_win = can.create_window(10, 500, anchor=tk.SW, window=bouton_splitter)

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
    main.title('Jeu de blackjack') #Creation de la fenetre
    main.geometry('1380x720+0+0')
    main.resizable(height=False,width=False)
    table = tk.PhotoImage(file='Images/BackgroundTemporaire.gif') #Importation de l'arriere-plan
    fond = tk.Canvas(main, height=table.height(), width=table.width(), bg='black') #Creation du canvas allant accueillir l'interface graphique
    fond.pack()
    fond.create_image(0,0,anchor = tk.NW, image=table) #Image d'arriere-plan
    creerBoutons(main, fond)
    main.mainloop()

