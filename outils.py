"""
:mod:`outils` module
:date: mars-avril 2023
:auteurs: BEAUREPAIRE Paul, GUILBERT Emma, HENRION Mathilde, LAMOUR Adam

"""

import random
import donnees

def liste_course_aleatoire(dico_produits : dict, nb_prod : int) -> list:
    """
    Cette fonction cree une liste de course aleatoire avec le nombre de produits demande par le client.

    Args:
        dico_produits (dict): dictionnaire contenant les produits et leurs emplacements
    Returns:
        list: retourne une liste de noms de produits
    
    >>> liste_course_aleatoire({"pommes" : {(3, 6) : [(2, 7), (2, 6), (2, 5), (3, 5), (4, 5)]}}, 1)
    ['pommes']
    """
    produits = []
    for cle in dico_produits.keys():
        produits += [cle]
    liste_course = []
    for _ in range(nb_prod):
        prod = random.choice(produits)
        produits.remove(prod)
        liste_course.append(prod)
    return liste_course



def cases_interdites(dico_produits : dict, caisses : dict) -> list:
    """
    Cette fonction cree une liste contenant les rayons ou le client ne peut pas circuler.

    Args:
        dico_produits (dict): dictionnaire contenant les produits et leurs emplacements
        caisses (dict): dictionnaire contenant les caisses et leurs emplacements

    Returns:
        list: retourne une liste de coordonnees
        
    >>> cases_interdites({"pommes" : {(3, 6) : [(2, 7), (2, 6), (2, 5), (3, 5), (4, 5)]}}, {"caisse 1" : {(2, 4) : [(2, 5)]}})
    [(3, 6), (2, 4)]
    """
    cases = []
    for valeur in dico_produits.values():
        for cle in valeur.keys():
            cases += [cle]
    for val in caisses.values():
        for cle in val.keys():
            cases += [cle]
    return cases

def deplacements_possibles_clients(liste : list, plan : list) -> list:
    """
    Cette fonction retourne la liste des cases accessibles par le client.

    Args:
        liste (dict): liste des cases de produits non accessibles
        plan (list): liste de liste vide

    Returns:
        list: retourne une liste de coordonees
    
    >>> deplacements_possibles_clients([(1, 2), (1, 1)], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2)]
    """
    deplacement = []
    for a in plan:
        deplacement += [a]
    for i in range(len(liste)):
        deplacement.remove(liste[i])
    return deplacement


def crea_graphe(liste_cases_access : list) -> dict:
    """
    Cette fonction cree un dictionnaire permettant de relier les cases ou le client peut circuler (graphe).

    Args:
        liste_cases_access (list): liste de coordonnees ou le client peut circuler

    Returns:
        dico: dictionnaire avec comme cle une case et en valeur les cases voisines
        
    >>> crea_graphe([(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2)])
    {(0, 0): [(0, 1), (1, 0)], (0, 1): [(0, 2), (1, 0), (0, 0)], (0, 2): [(0, 1)], (1, 0): [(2, 1), (2, 0), (0, 0), (0, 1)], (2, 0): [(2, 1), (1, 0)], (2, 1): [(2, 2), (2, 0), (1, 0)], (2, 2): [(2, 1)]}
    """
    interdit = cases_interdites(donnees.liste_produits, donnees.caisses)
    dep = liste_cases_access
    dico = {}
    for case in dep:
        x = case[0]
        y = case[1]
        dico[case] = []
        if -1<x<24 and -1<y+1<25:
            if (x, y+1) in dep and (x, y+1) not in interdit:
                dico[case] += [(x, y+1)]
                
        if -1<x+1<24 and -1<y+1<25:
            if (x+1, y+1) in dep:
                dico[case] += [(x+1, y+1)]
                
        if -1<x+1<24 and -1<y<25:
            if (x+1, y) in dep:
                dico[case] += [(x+1, y)]
                
        if -1<x+1<24 and -1<y-1<25:
            if (x+1, y-1) in dep:
                dico[case] += [(x+1, y-1)]
                
        if -1<x<24 and -1<y-1<25:
            if (x, y-1) in dep:
                dico[case] += [(x, y-1)]
                
        if -1<x-1<24 and -1<y-1<25:
            if (x-1, y-1) in dep:
                dico[case] += [(x-1, y-1)]
                
        if -1<x-1<24 and -1<y<25:
            if (x-1, y) in dep:
                dico[case] += [(x-1, y)]
                
        if -1<x-1<24 and -1<y+1<25:
            if (x-1, y+1) in dep:
                dico[case] += [(x-1, y+1)]
    return dico


def cle_dico(dico_produits : dict, produit : str) -> list:
    """
    Cette fonction renvoie les cases ou le produit est accessible a partir de son nom.

    Args:
        dico_produits (dict): dictionnaire contenant les produits et leurs emplacements
        produit (str): le nom du produit

    Returns:
        list: liste des coordonnees des cases accessibles
    
    >>> cle_dico({"pommes" : {(3, 6) : [(2, 7), (2, 6), (2, 5), (3, 5), (4, 5)]}, "bananes" : {(3, 7) : [(2, 8), (2, 7),(2, 6)]}}, "bananes")
    [(2, 8), (2, 7), (2, 6)]
    """
    
    # Regarde tous les elements de la liste de course
    for a in dico_produits.items():
        
        # Regarde si le produit est dans la liste
        if a[0] == produit :
                        
            # Recupere uniquement le dictionnaire du produit
            dico = dico_produits[a[0]]            
            
            # Parcours les valeurs du dictionnaire de l'article et retourne sa position
            for b in dico.values():
                return b


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)


#####################################################################################################
#------------------------------------ EN COURS D'IMPLEMENTATION ------------------------------------#
#####################################################################################################

# FONCTION QUI CREE UNE LISTE CONTENANT LES CASES A PARTIR DESQUELLES LE CLIENT PEUT PRENDRE L'ARTICLE
def voisins_produits(produits, plan):
    acces = []
    for i in range (len(produits)):
        coord = produits[i]
        x = coord[0]
        y = coord[1]
        if plan[x-1][y] != coord:
            print("acces")
            acces.append(plan[x-1, y])
        if plan[(x+1, y)] != coord:
            print("acces")
            acces.append(plan[x-1, y])
        if plan[(x, y-1)] != coord:
            print("acces")
            acces.append(plan[x-1, y])
        if plan[(x, y+1)] != coord:
            print("acces")
            acces.append(plan[x-1, y])
    return acces  
#####################################################################################################