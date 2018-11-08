import random

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
        cartesPiochees.append(p.pop(0))
    return cartesPiochees

### Fonctions Graphiques ###

def associerCartes(cartes):
    
