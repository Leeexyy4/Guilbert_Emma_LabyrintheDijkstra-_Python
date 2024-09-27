"""
:mod:`algo` module
:date: mars-avril 2023
:auteurs: BEAUREPAIRE Paul, GUILBERT Emma, HENRION Mathilde, LAMOUR Adam

"""

import donnees
import outils

# chemin le plus court
def chemin_le_plus_court(laby: dict, depart : tuple, arrivee : tuple) -> list:
    """
    Cette fonction permet d'obtenir le chemin le plus cours de cases a parcourir entre deux cases d'un graphe

    Args:
        laby (dict): dictionnaire avec comme cle une case et en valeur les cases voisines
        depart (tuple): case de depart du chemin a parcourir
        arrivee (tuple): case d'arrivee du chemin a parcourir

    Returns:
        list: liste des cases pour faire le chemin le plus court
    """
    
    resultat = {depart : [depart]} # on crée un dictionnaire
    a_explorer = [depart] 
    trouve = False
    while trouve == False: 
        actuel = a_explorer[0] #on prend le point actuel comme celui étant au début de la file
        a_explorer = a_explorer[1:] 
        for voisins in laby[actuel]: #parcours des voisins de la case actuelle

            for i in resultat[actuel]: 

                if voisins not in resultat:
                    resultat[voisins] = resultat[actuel]+[voisins]
                    a_explorer = a_explorer + [voisins] 
                
                if i == arrivee: #si on trouve l'arrivee dans la liste des voisins
                    trouve = True

    return resultat[arrivee]

# algo du plus court

def algo_plus_court(dico_voisins_chemin_clients : dict, dico_sortie_magasin : dict, liste : list, dico_produit : dict) -> list:
    """
    Cette fonction permet de faire le chemin a parcourir pour realiser ses courses en se deplacant le moins possible.
    On part de l'entree, on fait la liste de course puis on va a la caisse et on sort en utilisant le couloir du fond.

    Args:
        dico_voisins_chemin_clients (dict): graphe des cases ou le client peut circuler
        dico_sortie_magasin (dict): graphe des cases apres le passage en caisse
        liste (list): liste de course
        dico_produit (dict): dictionnaire contenant les produits et leurs emplacements

    Returns:
        list: liste du chemin le plus court faire les courses
    """
    depart = (0, 0)
    chemin = [(0,0)]
    d_totale = 0
    # tant que la liste n'est pas vide
    while liste != []:
        d_min = 100
        prod_min = ""
        pos = 0
        # pour chaque produit de la liste
        for produit in liste:
            # case ou on obtient le produit
            arrivee = outils.cle_dico(dico_produit, produit)
            # calcul du chemin le plus court
            for i in range(len(arrivee)):
                chemin_plus_court = chemin_le_plus_court(dico_voisins_chemin_clients, depart, arrivee[i])
                distance = len(chemin_plus_court)
            # si la distance est plus petite on la remplace
                if distance<d_min:
                    d_min = distance
                    prod_min = produit
                    pos = i
        chemin += chemin_le_plus_court(dico_voisins_chemin_clients, depart, outils.cle_dico(dico_produit, prod_min)[pos])[1:]
        d_totale += d_min
        depart = chemin[-1]
        liste.remove(prod_min)

    # Apres avoir fini la liste de course on passe a la caisse
    c_min = 100
    caisse_min = ""
    pos = 0
    # pour chaque produit de la liste
    for caisse in donnees.caisses:
        # case ou on obtient le produit
        arrivee = outils.cle_dico(donnees.caisses, caisse)
        # calcul du chemin le plus court
        for i in range(len(arrivee)):
            chemin_plus_court = chemin_le_plus_court(dico_voisins_chemin_clients, depart, arrivee[i])
            distance = len(chemin_plus_court)
        # si la distance est plus petite on la remplace alors
            if distance<c_min:
                c_min = distance
                caisse_min = caisse
                pos = i
    chemin += chemin_le_plus_court(dico_voisins_chemin_clients, depart, outils.cle_dico(donnees.caisses, caisse_min)[pos])[1:]
    d_totale += c_min
    depart = chemin[-1]
    
    # On sort du supermarche
    chemin += chemin_le_plus_court(dico_sortie_magasin, depart, (0,0))[1:]
    return chemin

# Affichage de la liste de course aleatoire
liste_course = outils.liste_course_aleatoire(donnees.liste_produits, 25)
print("\n\nLa liste de course aléatoire est composée des produits suivants : \n", liste_course,"\n")

# Appel des fonctions pour l'algorithme
interdit = outils.cases_interdites(donnees.liste_produits, donnees.caisses)
graphe_deplacements_clients = outils.crea_graphe(outils.deplacements_possibles_clients(interdit, donnees.plan))
graphe_sortie_magasin = outils.crea_graphe(donnees.cases_pour_sortir)

# Variable chemin : Le parcours du graphe le plus rapide
chemin = algo_plus_court(graphe_deplacements_clients, graphe_sortie_magasin, outils.liste_course_aleatoire(donnees.liste_produits, 25), donnees.liste_produits)
print("Le chemin le plus court pour parcourir le supermarché est : \n", chemin, "\n")

# ---------------------- algorithme principal ---------------------------

# liste des coordonnées des produits dans le magasin

# affichage graphique avec des emojis

def graphique(produits: dict, caisses : dict):
    liste_des_rayons = []
    # Regarde tous les elements de la liste de course
    for a in produits.items():
        
        # Regarde si le produit est dans la liste
        liste_de_course = produits[a[0]]
        
        # Recupere uniquement le dictionnaire du produit
        for b in liste_de_course.keys():
            
            # Parcours les valeurs du dictionnaire de l'article et retourne sa position
            liste_des_rayons += [b]

    # Affichage du plan du supermarché vide
    affichage = [["⬛️" for i in range(25)] for j in range(25)]

    # Placement les rayons correspondants à chaque case
    for i in liste_des_rayons:
        if 1 <= i[0] <= 12 and i[1] == 24:
            affichage[i[0]][i[1]] = "🥩" #viande
        if 13 <= i[0] <= 22 and i[1] == 24:
            affichage[i[0]][i[1]] = "🐟" #poisson
        if 0 == i[0] and 18 <= i[1] <= 24:
            affichage[i[0]][i[1]] = "🍮" #cremerie
        if 0 == i[0] and 6 <= i[1] <= 10:
            affichage[i[0]][i[1]] = "🍞" #pain
        if 0 == i[0] and 13 <= i[1] <= 15:
            affichage[i[0]][i[1]] = "🌱" #bio
        if 3<=i[0]<=4 and 16<=i[1]<=21:
            affichage[i[0]][i[1]] = "🧹" #entretien
        if 7<=i[0]<=8 and 16<=i[1]<=21:
            affichage[i[0]][i[1]] = "🚿" #hygiene
        if 11<=i[0]<=12 and 16<=i[1]<=21:
            affichage[i[0]][i[1]] = "🏠" #maison
        if 15<=i[0]<=16 and 16<=i[1]<=21:
            affichage[i[0]][i[1]] = "🏁" #divers
        if 19<=i[0]<=20 and 16<=i[1]<=21:
            affichage[i[0]][i[1]] = "🧊" #surgelé
        if 3<=i[0]<=4 and 6<=i[1]<=13:
            affichage[i[0]][i[1]] = "🍇" #fruits/légumes
        if 7<=i[0]<=8 and 6<=i[1]<=13:
            affichage[i[0]][i[1]] = "🥐" #petit-dej
        if 15<=i[0]<=16 and 6<=i[1]<=13:
            affichage[i[0]][i[1]] = "🥫" #conserves
        if 19<=i[0]<=20 and 6<=i[1]<=13:
            affichage[i[0]][i[1]] = "🐶" #animaux
        if i[0]==23 and 4<=i[1]<=13:
            affichage[i[0]][i[1]] = "🍾" #boissons
        if i[0]==23 and 16<=i[1]<=24:
            affichage[i[0]][i[1]] = "🥘" #plats cuisinées
        if 11<=i[0]<=12 and 6<=i[1]<=13:
            affichage[i[0]][i[1]] = "🏪" #epicerie
        
    
    # Retourne les cases avec des caisses
    liste_des_caisses = []
    for a in caisses.items():
        caisses2 = caisses[a[0]]
        for b in caisses2.keys():
            liste_des_caisses += [b]
            
    # Parcours de la liste pour afficher les caisses
    for i in liste_des_caisses:
        affichage[i[0]][i[1]] = "🛒" #caisses
                
    affichage[0][0] = "🟫" #entree
    
    # Liste des coordonnees du parcours par l'algorithme
    chemin = algo_plus_court(graphe_deplacements_clients, graphe_sortie_magasin, outils.liste_course_aleatoire(donnees.liste_produits, 25), donnees.liste_produits)
    
    # Parcours de la liste en ajoutant les chemins
    for i in chemin :
        affichage[i[0]][i[1]] = "🟥"
    
    # Affichage final
    for i in range(len(affichage)-1, -1, -1):
        for j in range(len(affichage[0])):
            print(affichage[j][i], end=" ")
        print()

    return affichage

print("Représentation graphique du parcours :\n")
graphique(donnees.liste_produits,donnees.caisses)