"""
:mod:`donnees` module
:date: mars-avril 2023
:auteurs: BEAUREPAIRE Paul, GUILBERT Emma, HENRION Mathilde, LAMOUR Adam

"""

# structure de donnees pour la liste de course
""" 
"nom du produit" : { emplacement du produit : [cases ou on accede au produit] }
"""

# creation d'un plan vierge avec toutes les cases accessibles
plan = [(i, j) for i in range(25) for j in range(25)]

# liste des produits disponible dans le supermarche ainsi que les cases où on peut y acceder
liste_produits = {
    # viandes
    "boeuf" :  {(1, 24) : [(1, 23), (2, 23)]},
    "canard" : {(2, 24) : [(1, 23), (2, 23), (3, 23)]},
    "porc" :  {(3, 24) : [(2, 23), (3, 23), (4, 23)]},
    "caille" : {(4, 24) : [(3, 23), (4, 23), (5, 23)]},
    "poulet" :  {(5, 24) : [(4, 23), (5, 23), (6, 23)]},
    "pigeon" : {(6, 24) : [(5, 23), (6, 23), (7, 23)]},
    "dinde" :  {(7, 24) : [(6, 23), (7, 23), (8, 23)]},
    "oie" : {(8, 24) : [(7, 23), (8, 23), (9, 23)]},
    "jambon" :  {(9, 24) : [(8, 23), (9, 23), (10, 23)]},
    "mouton" : {(10, 24) : [(9, 23), (10, 23), (11, 23)]},
    "lapin" :  {(11, 24) : [(10, 23), (11, 23), (12, 23)]},
    "cheval" : {(12, 24) : [(11, 23), (12, 23), (13, 23)]},

    # poissons
    "saumon" :  {(13, 24) : [(12, 23), (13, 23), (14, 23)]}, 
    "truite" : {(14, 24) : [(13, 23), (14, 23), (15, 23)]},
    "marquereau" :  {(15, 24) : [(14, 23), (15, 23), (16, 23)]}, 
    "nemo" : {(16, 24) : [(15, 23), (16, 23), (17, 23)]},
    "sardine" :  {(17, 24) : [(16, 23), (17, 23), (18, 23)]},
    "dory" : {(18, 24) : [(17, 23), (18, 23), (19, 23)]},
    "crevette" :  {(19, 24) : [(18, 23), (19, 23), (20, 23)]},
    "thon " : {(20, 24) : [(19, 23), (20, 23), (21, 23)]},
    "colin" :  {(21, 24) : [(20, 23), (21, 23), (22, 23)]}, 
    "homard sebastien" : {(22, 24) : [(21, 23), (22, 23)]},

    # fruits
    "pomme" : {(3, 6) : [(2, 7), (2, 6), (2, 5), (3, 5), (4, 5)]},
    "banane" : {(3, 7) : [(2, 8), (2, 7),(2, 6)]},
    "poire" : {(3, 8) : [(2, 7), (2, 8), (2, 9)]},
    "orange" : {(3, 9) : [(2, 8), (2, 9), (2, 10)]},
    "clementine" : {(3, 10) : [(2, 9), (2, 10), (2, 11)]},
    "melon" : {(3, 11) : [(2, 10), (2, 11), (2, 12)]},
    "ananas" : {(3, 12) : [(2, 11), (2, 12), (2, 13)]},
    "raisin" : {(3, 13) : [(2, 12), (2, 13), (2, 14), (3, 14), (4, 14)]},

    # legumes
    "pomme de terre" : {(4, 6) : [(3, 5), (4, 5), (5, 5), (5, 6), (5, 7)]},
    "carotte" : {(4, 7) : [(5, 6),(5, 7),(5, 8)]},
    "tomate" : {(4, 8) : [(5, 7),(5, 8),(5, 9)]},
    "chou-fleur" : {(4, 9) : [(5, 8),(5, 9),(5, 10)]},
    "brocoli" : {(4, 10) : [(5, 9),(5, 10),(5, 11)]},
    "champignon" : {(4, 11) : [(5, 10),(5, 11),(5, 12)]},
    "courgette" : {(4, 12) : [(5, 11),(5, 12),(5, 13)]},
    "salade" : {(4, 13) : [(5, 12),(5, 13),(5, 14),(3, 14),(4, 14)]},

    # conserves
    "haricots vert" : {(15, 6) : [(14, 5),(15, 5),(16, 5),(14, 6),(14, 7)]},
    "haricots blanc" : {(15, 7) : [(14, 6),(14, 7),(14, 8)]},
    "haricots rouge" : {(15, 8) : [(14, 7),(14, 8),(14, 9)]},
    "petit pois" : {(15, 9) : [(14, 8),(14, 9),(14, 10)]},
    "thon" : {(15, 10) : [(14, 9),(14, 10),(14, 11)]},
    "olive" : {(15, 11) : [(14, 10),(14, 11),(14, 12)]},
    "maïs" : {(15, 12) : [(14, 11),(14, 12),(14, 13)]},
    "sauce tomate" : {(15, 13) : [(14, 12),(14, 13),(14, 14),(15, 14),(16, 14)]},
    "raviolis" : {(16, 7) : [(17,6), (17, 7), (17, 8)]},
    "cassoulet" : {(16, 8) : [(17,7), (17, 8), (17, 9)]},
    "lentilles en conserve" : {(16, 9) : [(17,8), (17, 9), (17, 10)]},
    "peche au sirop" : {(16, 10) : [(17, 9), (17, 10), (17, 11)]},
    "salade de fruits" : {(16, 11) : [(17, 10), (17, 11), (17, 12)]},
    "champignons en conserve" : {(16, 12) : [(17, 11), (17, 12), (17, 13)]},
    "petit pois carottes" : {(16, 13) : [(17, 12), (17, 13), (17, 14), (16, 14), (15, 14)]},
    "poire au sirop" : {(16, 6) : [(15, 5), (16, 5), (17, 5), (17, 6), (17, 7)]},

    # epicerie 
    "sel" : {(12, 6) : [(11, 5),(12, 5),(13, 5),(13, 6),(14, 6)]},
    "pates" : {(11, 6) : [(10, 5),(11, 5),(12, 5),(10, 6),(10, 7)]},
    "riz" : {(11, 7) : [(10, 6),(10, 7),(10, 8)]},
    "puree" : {(11, 8) : [(10, 7),(10, 8),(10, 9)]},
    "semoule" : {(11, 9) : [(10, 8),(10, 9),(10, 10)]},
    "farine" : {(11, 10) : [(10, 9),(10, 10),(10, 11)]},
    "lentille" : {(11, 11) : [(10, 10),(10, 11),(10, 12)]},
    "sauce andalouse" : {(11, 12) : [(10, 11),(10, 12),(10, 13)]},
    "poivre" : {(11, 13) : [(10, 12),(10, 13),(10, 14),(11, 14),(12, 14)]},
    "curry" : {(12, 7) : [(13, 6),(13, 7),(13, 8)]},
    "moutarde" : {(12, 8) : [(13, 7),(13, 8),(13, 9)]},
    "mayonnaise" : {(12, 9) : [(13, 8),(13, 9),(13, 10)]},
    "ketchup" : {(12, 10) : [(13, 9),(13, 10),(13, 11)]},
    "huile" : {(12, 11) : [(13, 10),(13, 11),(13, 12)]},
    "vinaigre" : {(12, 12) : [(13, 11),(13, 12),(13, 13)]},
    "pain tresse" : {(12, 13) : [(7, 14), (8, 14)]},

    # surgele
    "frite" : {(19, 16) : [(20, 15),(19, 15),(18, 15),(18, 16),(18, 17)]},
    "petit pois surgele" : {(19, 17) : [(18, 16),(18, 17),(18, 19)]},
    "haricot surgele" :  {(19, 18) : [(18, 17),(18, 18),(18, 19)]}, 
    "glacon" : {(19, 19) : [(18, 18),(18, 19),(18, 20)]},
    "steack hache" : {(19, 20) : [(18, 19),(18, 20),(18, 21)]}, 
    "soupe surgele" : {(19, 21) : [(18, 20),(18, 21),(19, 22),(20, 22)]},
    "poisson pane" : {(20, 16) : [(19, 15),(20, 15),(21, 15),(21, 16),(21, 17)]},
    "biscuit surgele" : {(20, 17) : [(21, 16),(21, 17),(21, 18)]},
    "pizza surgele" : {(20, 18) : [(21, 17),(21, 18),(21, 19)]}, 
    "macaron surgele" : {(20, 19) : [(21, 18),(21, 19),(21, 20)]},
    "glace" : {(20, 20) : [(21, 19),(21, 20),(21, 21)]}, 
    "pain surgele" : {(20, 21) : [(21, 20),(21, 21),(19, 22),(20, 22),(21, 22)]},

    # boissons
    "eau" : {(23, 4) : [(23, 3),(22, 3),(22, 4),(22, 5)]},
    "sirop" : {(23, 5) : [(22, 4),(22, 5),(22, 6)]},
    "jus de fruits" : {(23, 6) : [(22, 5),(22, 6),(22, 7)]},
    "limonade" : {(23, 7) : [(22, 6),(22, 7),(22, 8)]},
    "lait" : {(23, 8) : [(22,7),(22, 8),(22, 9)]},
    "vin" : {(23, 9) : [(22, 8),(22, 9),(22, 10)]},
    "biere" : {(23, 10) : [(22, 9),(22, 10),(22, 11)]},
    "vodka" : {(23, 11) : [(22, 10),(22, 11),(22, 12)]},
    "captain" : {(23, 12) : [(22, 11),(22, 12),(22, 13)]},
    "coca" : {(23, 13) : [(22, 12),(22, 13),(22, 14),(23, 14)]},

    # pain
    "baguette" : {(0, 6) : [(0, 5),(1, 5),(1, 6),(1,7)]},
    "petit pain" : {(0,7) : [(1, 6),(1,7),(1, 8)]},
    "croissant" : {(0, 8) : [(1,7),(1, 8),(1, 9)]},
    "chausson au pommes" : {(0, 9) : [(1, 8),(1, 9),(1, 10)]},
    "boule coupee" : {(0, 10) : [(0, 11),(1, 9),(1, 10),(1, 11)]},

    # bio
    "lait d'amande" : {(0, 13) : [(0, 12),(1, 12),(1, 13),(1, 14)]},
    "viandes de soja" : {(0, 14) : [(1, 13),(1, 14),(1, 15)]},
    "huile BIO" : {(0, 15) : [(1, 14),(1, 15),(1, 16),(0, 16)]},

    # hygiene
    "gel douche" : {(7, 21) : [(6, 20), (6, 21), (6, 22), (7, 22), (8, 22)]},
    "shampoing" : {(7, 20) : [(6, 21), (6, 20), (6, 19)]},
    "coton-tige" : {(7, 19) : [(6, 20), (6, 19), (6, 18)]},
    "gel coiffant" : {(7, 18) : [(6, 19), (6, 18), (6, 17)]},
    "deodorant" : {(7, 17) : [(6, 18), (6, 17), (6, 19)]},
    "rasoirs" : {(7, 16) : [(6, 17), (6, 16), (6, 15), (7, 15), (8, 15)]},
    "mousse a raser" : {(8, 16) : [(7, 15), (8, 15), (9, 15), (9, 16), (9, 17)]},
    "brosse a dents" : {(8, 17) : [(9, 18), (9, 17), (9, 16)]},
    "dentifrice" : {(8, 18) : [(9, 19), (9, 18), (9, 17)]},
    "dissolvant" : {(8, 19) : [(9, 20), (9, 19), (9, 18)]},
    "stick levres" : {(8, 20) : [(9, 21), (9, 20), (9, 19)]},
    "couches" : {(8, 21) : [(7, 22), (8, 22), (9, 22), (9, 21), (9, 20)]},

    # divers
    "bombe anti-crevaison" : {(15, 16) : [(14, 17), (14, 16), (14, 15), (15, 15), (16, 15)]},
    "bombe anti-rouille" : {(15, 17) : [(14, 18), (14, 17), (14, 16)]},
    "nettoyant vitres" : {(15, 18) : [(14, 19), (14, 18), (14, 17)]},
    "nettoyant jantes" : {(15, 19) : [(14, 20), (14, 19), (14, 18)]},
    "mousse lavage carroserie" : {(15, 20) : [(14, 19),(14, 20),(14, 21)]}, 
    "rateau" : {(15, 21) : [(14, 20),(14, 21),(14, 22)]},
    "stylo raccord peinture" : {(16, 16) : [(15, 15), (16, 15), (17, 15), (17, 16), (17, 17)]},
    "leds habitacle" : {(16, 17) : [(17, 16), (17, 17), (17, 18)]},
    "anti-insectes" : {(16, 18) : [(17, 17), (17, 18), (17, 19)]},
    "bouteille de gaz" : {(16, 19) : [(17, 18), (17, 19), (17, 20)]},
    "charbon de bois" : {(16, 20) : [(17, 19), (17, 20), (17, 21)]}, 
    "pied de biche" : {(16, 21) : [(17, 20), (17, 21), (17, 22), (15, 22),(16, 22)]},

    # petit dejeuner
    "cacao" : {(8, 8) : [(9,7), (9, 8), (9, 9)]}, 
    "the noir" : {(8, 9) : [(9, 8), (9, 9), (9, 10)]},
    "the vert" : {(8, 6) : [(7, 5), (8, 5), (9, 5), (9, 6), (9,7)]}, 
    "confiture fraise" : {(8,7) : [(9, 6), (9,7), (9, 8)]},
    "cafe" : {(7,7) : [(6, 6), (6,7), (6, 8)]}, 
    "sucre" : {(7, 6): [(6, 5), (6, 6), (6,7), (7, 5), (8, 5)]},
    "cereales" : {(7, 8) : [(6,7), (6, 8), (6, 9)]},
    "brioche" : {(7, 9) : [(6, 8), (6, 9), (6, 10)]},
    "gateaux" : {(7, 10) : [(6, 9), (6, 10), (6, 11)]},
    "confiture d'abricot" : {(7, 11) : [(6, 10), (6, 11), (6, 12)]},    
    "pate a tartiner" : {(7, 12) : [(6, 11), (6, 12), (6, 13)]}, 
    "cassonade" : {(7, 13) : [(6, 12), (6, 13)]}, 
    "miel" : {(8, 10) : [(9, 9), (9, 10), (9, 11)]},
    "biscottes" : {(8, 11) : [(9, 10), (9, 11), (9, 12)]},
    "pain de mie" : {(8, 12) : [(9, 11), (9, 12), (9, 13)]}, 
    "confiture de pommes" : {(8, 13) : [(9, 12), (9, 13), (9, 14), (8, 14), (7, 14)]},

    # entretien
    "eponges" : {(3, 16) : [(2, 15), (3, 15), (4, 15), (2, 16), (2, 17)]},
    "liquide vaisselle" : {(4, 16) : [(3, 15), (4, 15), (5, 15), (5, 16), (5, 17)]},
    "lessive" : {(3, 17) : [(2, 16), (2, 17), (2, 18)]},
    "sacs poubelle" : {(3, 18) : [(2, 17), (2, 18), (2, 19)]},
    "papier alu" : {(3, 19) : [(2, 18), (2, 19), (2, 20)]},
    "vinaigre blanc" : {(3, 20) : [(2, 19), (2, 20), (2, 21)]},
    "papier sulfurise" : {(4, 17) : [(5, 16), (5, 17), (5, 18)]},
    "bicarbonate" : {(4, 18) : [(5, 17), (5, 18), (5, 19)]},
    "javel" : {(4, 19) : [(5, 18), (5, 19), (5, 20)]},
    "essuie-tout" : {(4, 20) : [(5, 19), (5, 20), (5, 21)]},
    "papier toilette" : {(3, 21) : [(3, 22), (4, 22), (2, 22), (2, 21), (2, 20)]}, 
    "pastilles vaisselle" : {(4, 21) : [(3, 22), (4, 22), (5, 22),(5, 21), (5, 20)]},

    # cremerie
    "creme fraiche" : {(0,18) : [(0,17), (1,17), (1,18), (1,19)]},     
    "yaourts" : {(0,19) : [(1,18), (1,19), (1,20)]},  
    "beurre" : {(0,20) : [(1,19), (1,20), (1,21)]},
    "oeufs" : {(0,21) : [(1,20), (1,21), (1,22)]},   
    "fromage" : {(0,22) : [(1,21), (1,22), (1,23)]}, 
    "fromage blanc" : {(0,23) : [(1,22), (1,23)]},
    "gouda" : {(0,24) : [(1,23)]},

    # animaux
    "patee chat" : {(19,6) : [(20,5), (19,5), (18,5), (18,6), (18,7)]},
    "litiere" : {(19,7) : [(18,6), (18,7), (18,8)]},
    "arbre a chat" : {(19,8) : [(18,7), (18,8), (18,9)]},
    "panier" : {(19,9) : [(18,8), (18,9), (18,10)]},
    "friandises" : {(19,10) : [(18,9), (18,10), (18,11)]},
    "nourriture chien" : {(19,11) : [(18,10), (18,11), (18,12)]},
    "nourriture chat" : {(19,12) : [(18,11), (18,12), (18,13)]},
    "nourriture oiseaux" : {(19,13) : [(20,14), (19,14), (18,14), (18,13), (18,12)]},
    "nourriture poissons" : {(20,6) : [(19,5), (20,5), (21,5), (21,6), (21,7)]},
    "nourriture tortue" : {(20,7) : [(21,6), (21,7), (21,8)]},
    "nourriture poules" : {(20,8) : [(21,7), (21,8), (21,9)]},
    "nourriture serpent" : {(20,9) : [(21,8), (21,9), (21,10)]},
    "nourriture chevre naine" : {(20,10) : [(21,9), (21,10), (21,11)]},
    "nourriture cameleon casque du Yemen" : {(20,11) : [(21,10), (21,11), (21,12)]},
    "nourriture koala" : {(20,12) : [(21,11), (21,12), (21,13)]},
    "nourriture crocodile" : {(20,13) : [(21,12), (21,13), (21,14), (20,14), (19,14)]},

    # maison
    "piles" : {(11,17) : [(10,16), (10,17), (10,18)]}, 
    "poele" : {(11,16) : [(10,15), (10,16), (10,17), (11,15), (12,15)]},
    "ampoules" : {(11,18) : [(10,17), (10,18), (10,19)]},  
    "scotch" : {(11,19) : [(10,18), (10,19), (10,20)]},  
    "enveloppes" : {(11,20) : [(10,19), (10,20), (10,21)]}, 
    "casserole" : {(11,21) : [(10,20), (10,21), (10,22), (11,22), (12,22)]}, 
    "stylos" : {(12,17) : [(13,16), (13,17), (13,18)]}, 
    "cuillere a soupe" : {(12,16) : [(13,17), (13,16), (13,15), (12,15), (11,15)]}, 
    "cartouche d'encre" : {(12,18) : [(13,17), (13,18), (13,19)]}, 
    "assiettes" : {(12,19) : [(13,18), (13,19), (13,20)]},
    "papier" : {(12,20) : [(13,19), (13,20), (13,21)]}, 
    "plat a tarte" : {(12,21) : [(13,20), (13,21), (13,22), (12,22), (11,22)]}, 

    # plats cuisines
    "lasagnes" : {(23,16) : [(22,15), (23,15), (22,16), (22,17)]}, 
    "croque monsieur" : {(23,17) : [(22,16), (22,17), (22,18)]}, 
    "boeuf bourguignon" : {(23,18) : [(22,17), (22,18), (22,19)]}, 
    "magret de canard" : {(23,19) : [(22,18), (22,19), (22,20)]}, 
    "moule frite" : {(23,20) : [(22,19), (22,20), (22,21)]}, 
    "couscous" : {(23,21) : [(22,20), (22,21), (22,22)]}, 
    "blanquette de veau" : {(23,22) : [(22,21), (22,22), (22,23)]}, 
    "gigot d'agneau" : {(23,23) : [(22,22), (22,23)]}, 
    "cote de boeuf" : {(23,24) : [(22,23)]}, 
}

# cases finales pour l'acces aux caisses
caisses = {
    "caisse 1" : {(4, 3) : [(5, 3)]},
    "caisse 2" : {(6, 3) : [(7, 3)]},
    "caisse 3" : {(8, 3) : [(9, 3)]},
    "caisse 4" : {(10, 3) : [(11, 3)]},
    "caisse 5" : {(12, 3) : [(13, 3)]},
    "caisse 6" : {(14, 3) : [(15, 3)]},
    "caisse 7" : {(16, 3) : [(17, 3)]},
    "caisse 8" : {(18, 3) : [(19, 3)]},
    "caisse 9" : {(20, 3) : [(21, 3)]},
    "caisse 1_bis" : {(4, 2) : [(5, 2)]},
    "caisse 2_bis" : {(6, 2) : [(7, 2)]},
    "caisse 3_bis" : {(8, 2) : [(9, 2)]},
    "caisse 4_bis" : {(10, 2) : [(11, 2)]},
    "caisse 5_bis" : {(12, 2) : [(13, 2)]},
    "caisse 6_bis" : {(14, 2) : [(15, 2)]},
    "caisse 7_bis" : {(16, 2) : [(17, 2)]},
    "caisse 8_bis" : {(18, 2) : [(19, 2)]},
    "caisse 9_bis" : {(20, 2) : [(21, 2)]}
}

# pour sortir du magasin il faut obliger le client a emprunter le couloir du fond
# on indique dans une liste les cases pour sortir apres etre passe a la caisse
cases_pour_sortir = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0),
                     (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0),
                     (21, 0), (22, 0), (23, 0),
                     (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1),
                     (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1),
                     (21, 1), (22, 1), (23, 1),
                     (5, 2), (7, 2), (9, 2), (11, 2), (13, 2), (15, 2), (17, 2), (19, 2), (21, 2),
                     (5, 3), (7, 3), (9, 3), (11, 3), (13, 3), (15, 3), (17, 3), (19, 3), (21, 3)]
