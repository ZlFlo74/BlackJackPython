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
            valeur = int(input('1 ou 11 ? '))
    elif ('valet' in carte) or ('dame' in carte) or ('roi' in carte):
        valeur = 10
    else:
        liste = carte.split(' ')
        valeur = int(liste[0])
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
    return pioche

def piocheCarte(p, x=1):
    """Recoit en argument la pioche, et le nombre de cartes à piocher (par
    defaut 1), et retourne les x premieres cartes de la pioche (en les
    retirant)."""
    cartesPiochees = []
    for i in range(x):
        cartesPiochees.append(p[0])
        p.pop(0)
    return cartesPiochees

#Partie A2

def initJoueur(n, n_IA):
    """Demande à l'utilisateur le nom des joueurs"""
    liste_joueurs = []
    for i in range(n):
        nom = input('Nom du joueur '+str(i+1)+' : ')
        liste_joueurs.append(nom)
    for i in range(n_IA):
        nom = 'IA_'+str(i+1)
        liste_joueurs.append(nom)
    return liste_joueurs

def initScores(joueurs,v=0):
    """Initialise le score de chaque joueur en début de partie"""
    scores = {}
    for joueur in joueurs:
        scores[joueur] = v
    return scores

def argent_init(joueurs):
    """On créer un dictionnaire dans lequel on stock toute les mise de chaque joueur"""
    argent_initial = int(input("Entrez l'argent initial de chaque joueur : "))
    argent = {}
    for joueur in joueurs:
        argent[joueur]= argent_initial
    return argent


def premierTour(pioche,joueurs,argent):
    """Simule le premier tour de la partie"""
    scores = initScores(joueurs)
    mises = {}
    for joueur in joueurs :
        print(joueur)
        cartes_piochees = piocheCarte(pioche,x=2)
        for carte in cartes_piochees :
            scores[joueur] += valeurCarte(carte)
        print('Valeur de vos cartes : '+str(scores[joueur]))
        if 'IA_' in joueur :
            if scores[joueur]<=13 :
                mise = int(argent[joueur]/6)
            elif scores[joueur]<=17 :
                mise = int(argent[joueur]/8)
            elif scores[joueur]<=20 :
                mise = int(argent[joueur]/4)
            else :
                mise = int(argent[joueur]/2)
            print("Mise du joueur :",mise)
        else :
            mise = int(input("Entrez votre mise : "))
        argent_initial = argent[joueur]
        argent[joueur] = argent_initial - mise
        mises[joueur]=mise
    return scores, mises

def gagnants(scores,score_croupier):
    """Retourne le gagnant d'un tour"""
    score_max = 0
    gagnant = []
    if score_croupier>21 :
        a_battre = 0
    else:
        a_battre = score_croupier
    for joueur in scores.keys():
        if scores[joueur]<22 and scores[joueur]>=a_battre:
            gagnant.append(joueur)
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

def tourJoueur(joueurs,j,scores,pioche,score_croupier):
    print(j)
    print('Votre score : '+str(scores[j]))
    if 'IA_' in j:
        continu = True
        while continu :
            if scores[j]<12:
                scores[j] += valeurCarte(piocheCarte(pioche)[0])
                print("L'IA continue")
            elif scores[j]==12:
                if score_croupier>=4 and score_croupier<=6 :
                    continu = False
                    print("L'IA s'arrete")
                    joueurs.remove(j)
                else :
                    scores[j] += valeurCarte(piocheCarte(pioche)[0])
                    print("L'IA continue")
            elif scores[j]<17:
                if score_croupier<7:
                    continu = False
                    print("L'IA s'arrete")
                    joueurs.remove(j)
                else :
                    scores[j] += valeurCarte(piocheCarte(pioche)[0])
                    print("L'IA continue")
            else :
                continu = False
                print("L'IA s'arrete")
                joueurs.remove(j)
    else :
        if continuer():
            scores[j] += valeurCarte(piocheCarte(pioche)[0])
            if scores[j] >= 21 :
                joueurs.remove(j)
        else:
            joueurs.remove(j)

#Partie B2

def tourComplet(joueurs,scores,pioche,score_croupier):
    """Donne un tour de jeu à chaque joueur dans la partie"""
    for joueur in joueurs:
        tourJoueur(joueurs,joueur,scores,pioche,score_croupier)

def partieFinie(joueurs):
    if len(joueurs)==0:
        return True
    else :
        return False

def partieComplete(joueurs):
    tour = 1
    argent = argent_init(joueurs)
    ok = True
    while ok :
        joueurs_en_jeu = list(joueurs)
        pioche = initPioche(len(joueurs))
        print("Récapitulatif de l'argent des joueurs : ")
        for joueur in joueurs :
            print(joueur,':',argent[joueur])
        print('')
        score_croupier, carte_cachee = initCroupier(pioche)
        print('Tour',tour)
        print('La premiere carte du croupier a une valeur de',score_croupier,"\n")
        scores, mises = premierTour(pioche,joueurs_en_jeu,argent)
        print('')
        while not partieFinie(joueurs_en_jeu):
            tourComplet(joueurs_en_jeu,scores,pioche,score_croupier)
        print('')
        score_croupier += valeurCarte(carte_cachee)
        score_croupier = tourCroupier(pioche, score_croupier)
        print('Scores finaux : ')
        for joueur in joueurs :
            print(joueur,':',scores[joueur])
        print('Croupier :',score_croupier)
        gagnant = gagnants(scores,score_croupier)
        for g in gagnant :
            argent[g] += 2*mises[g]
            print(g,'remporte la mise !\n')
        nouvelle_partie = 0
        while nouvelle_partie != 'oui' and nouvelle_partie != 'non' :
            nouvelle_partie = input('Voulez vous rejouer ? (oui/non) ')
        for joueur in argent.keys():
            if argent[joueur] <= 0 :
                ok = False
            if nouvelle_partie == 'non': #On crée une autre boucle pour ne pas demander une nouvelle partie si un joueur n'a plus d'argents
                ok = False
        tour += 1

    print("Score final : ")
    for joueur in argent.keys() :
        print(joueur,':',argent[joueur])

#Partie Croupier
def initCroupier(pioche):
    cartes_croupier = piocheCarte(pioche,x=2)
    carte_cachee = cartes_croupier[1]
    score_croupier = valeurCarte(cartes_croupier[0])
    return score_croupier, carte_cachee

def tourCroupier(pioche, score_croupier):
    while score_croupier < 17 :
        score_croupier += valeurCarte(piocheCarte(pioche)[0])
    return score_croupier

#main
def main():
    nb_joueurs = int(input("Combien y'a t-il de joueurs ? "))
    nb_IA = int(input("Combien voulez-vous d'IA ?"))
    joueurs = initJoueur(nb_joueurs, nb_IA)
    partieComplete(joueurs)

main()
