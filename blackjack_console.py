import random

#Partie A1
def paquet():
    """Initialise et renvoie un paquet de 52 cartes."""
    couleurs = ['carreau','pique','trefle','coeur']
    rangs = ['as','2','3','4','5','6','7','8','9','10','valet','dame','roi']
    cartes = []
    for couleur in couleurs :
        for rang in rangs :
            cartes.append(rang+' de '+couleur)
    return cartes

def valeurCarte(carte):
    """Pour une carte donnée, renvoie sa valeur en points."""
    if 'as' in carte :
        valeur = 0
        while valeur!=1 and valeur!=11:
            valeur = int(input('1 ou 11 ?'))
    elif ('valet' in carte) or ('dame' in carte) or ('roi' in carte):
        valeur = 10
    else:
        liste = carte.split(' ')
        valeur = str(liste[0])
    return valeur

def initPioche(n):
    """Prend un nombre de paquets egal au nombre de joueurs puis melange
    les cartes pour creer la pioche."""
    pioche_non_melangees = n*paquet()
    pioche = []
    quantite = len(pioche_non_melangees)
    for i in range(quantite):
        carte = random.choice(pioche_non_melangees)
        pioche.append(carte)
        pioche_non_melangees.remove(carte)

def piocheCarte(p, x=1):
    """Recoit en argument la pioche, et le nombre de cartes à piocher (par
    defaut 1), et retourne les x premieres cartes de la pioche (en les
    retirant)."""
    cartesPiochees = []
    for i in range(x):
        cartesPiochees.append(p)
    return cartesPiochees

#Partie A2

def initJoueur(n):
    """Demande à l'utilisateur le nom des joueurs"""
    liste_joueurs = []
    for i in range(n):
        nom = input('Nom du joueur '+str(i+1)+' : ')
        liste_joueurs.append(nom)
    return liste_joueurs

def initScores(joueurs,v=0):
    """Initialise le score de chaque joueur en début de partie"""
    scores = {}
    for joueur in joueurs:
        scores[joueur] = v
    return scores

#def mise_init(joueurs):
    #"""On créer un dictionnaire dans lequel on stock toute les mise de chaque joueur"""
    #mise_initial= int(input("Entrez la mise initial de chaaque joueur"))
    #mise = {}
    #for joueur in joueurs:
        #mise[joueur]= mise_initial
    #return mise


def premierTour(pioche,joueurs):
    """Simule le premier tour de la partie"""
    scores = initScores(joueurs)
    #mise = mise_init(joueurs)
    for joueur in joueurs :
        cartes_piochees = piocheCarte(pioche,x=2)
        #la_mise = int(input("Entrez votre mise"))
       # mise_initial = mise[joueur]
        #mise[joueur] = mise_initial - la_mise
        #mise_initial = mise[joueur]
        for carte in cartes_piochees :
            scores[joueur] += valeurCarte(carte)
    return scores

def gagnant(scores):
    """Retourne le gagnant d'un tour"""
    score_max = scores[scores.keys()[0]]
    gagnant = scores.keys()[0]
    for joueur in scores.keys():
        if scores[joueur]>score_max:
            gagnant = joueur
            score_max = scores[joueur]
    return gagnant

#Partie B1

def continuer():
    rep = 0
    while rep!='oui' and rep!='non':
        rep = input('Voulez-vous continuer ? (oui/non) ')
    if rep == 'oui':
        return True
    else :
        return False

def tourJoueur(joueurs,j,tour,scores,pioche,mise):
    print('Tour '+str(tour))
    print(j)
    print('Votre score : '+str(scores[j]))
    if continuer():
        scores[j] += valeurCarte(piocheCarte(pioche))
        if scores[j] >= 21 :
            joueurs.remove(j)
    else:
        joueurs.remove(j)

#Partie B2

def tourComplet(joueurs,tour,scores,pioche):
    """Donne un tour de jeu à chaque joueur dans la partie"""
    for joueur in joueurs:
        tourJoueur(joueurs,joueur,tour,scores,pioche)

def partieFinie(joueurs):
    if len(joueurs)==0:
        return True
    else :
        return False

def partieComplete(joueurs,nb_victoires):
    joueurs_en_jeu = joueurs
    tour = 1
    pioche = initPioche(len(joueurs))
    scores = premierTour(pioche,joueurs_en_jeu)
    while not partieFinie(joueurs_en_jeu):
        tourComplet(joueurs_en_jeu,tour,scores,pioche)
    gagnant = gagnant(joueurs)
    


#main

joueurs = ['rachid','mouloud']
partieComplete(joueurs,1)
