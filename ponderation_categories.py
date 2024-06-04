import numpy as np

g =[[None, ['Merignac', 16, 7, 3, 255, 'cst', True, 0.5], ['AntenneBdx', 13, 6, 2,255, 'cst', False, 0.0], None, None, None, None, None, None, ['Leyre', 45, 24, 9, 255, 'cst', False, 0.0], ['Garonne', 11, 6, 2, 255, 'cst', False, 0.0], None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 16, 7, 3, 255, 'cst', True, 0.5], None, ['AntenneBdx', 13, 6, 2, 255, 'cst', False, 0.0], ['Andernos', 26, 12, 4, 255, 'cst', True, 0.2], None, None, None, None, None, None, None, ['Bordeaux',11, 4, 1, 255, 'cst', False, 0.7], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 13, 6, 2, 255, 'cst', True, 0.0], ['Merignac', 13, 6, 2, 255, 'cst', True, 0.0], None, ['Andernos', 21, 9, 3, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None], [None, ['Merignac', 26, 12, 4, 255, 'cst', True, 0.2], ['AntenneBdx', 21, 9, 3, 255, 'cst', False,0.0], None, ['Arcachon', 16, 6, 2, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, ['Andernos', 16, 6, 2, 255, 'cst', True, 0.0], None, ['Cazaux', 6, 3, 1, 255, 'cst',False, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, ['Arcachon', 6, 3, 1, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['AntenneBisca', 13, 6, 2, 255, 'cst', False, 0.5]], [None, None, None, None, None, None, None, ['Mimizan', 23, 9, 3, 255, 'cst', True, 0.0], None, ['Leyre', 29, 13, 5, 255, 'cst', False, 0.2], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['AntenneBisca', 11,5, 2, 255, 'cst', False, 0.7]], [None, None, None, None, None, None, ['Biscarrosse', 23, 9, 3, 255, 'cst', True, 0.0], None, ['Biarritz', 71, 31, 11, 255, 'cst', True, 0.1], ['Leyre', 32, 13, 5, 255, 'cst', False, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, ['Mimizan', 71, 31, 11, 255, 'cst', True, 0.1], None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 45, 24, 9, 255, 'cst', True, 0.0], None, None, None, None, None, ['Biscarrosse', 29, 13, 5, 255, 'cst', True, 0.2], ['Mimizan', 32, 13, 5, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 11, 6, 2, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Yvrac', 21, 9, 3, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, ['Merignac', 11, 4, 1, 255, 'cst',True, 0.7], None, None, None, None, None, None, None, None, None, None, ['L.St Laurent', 34, 15, 6, 255, 'cst', True, 0.0], None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None], [None,None, None, None, None, None, None, None, None, None, None, ['Bordeaux', 34, 15, 6, 255, 'cst', False, 0.0], None, ['Soulac', 32, 18, 7, 255, 'cst', True, 0.0], None, ['Jonzac', 42, 18, 7, 255, 'cst', True, 0.5], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, ['L.St Laurent', 32, 18, 7, 255, 'cst', True, 0.0], None, None, ['Jonzac', 45, 21, 8, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Jonzac', 21, 10, 4, 255, 'cst', True, 0.0], ['Yvrac', 39, 18, 7, 255, 'cst', True, 0.5], None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, ['L.St Laurent', 42, 18, 7, 255, 'cst', True, 0.5], ['Soulac', 45, 21, 8, 255, 'cst', True, 0.0], ['Montendre', 21, 10, 4, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, ['Garonne', 21, 9, 3, 255, 'cst', False, 0.0], None, None, None, ['Montendre', 39, 18, 7, 255, 'cst', True, 0.5], None, None, ['LibourneVille', 18, 9, 3, 255, 'cst', False, 0.5], ['Libourne', 27, 12, 4, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Yvrac', 18, 9, 3, 255, 'cst', True, 0.5], None, ['Libourne', 11, 5, 2, 255, 'cst', True, 0.0], None, None, None, ['FoyLaGrande', 29, 15, 6, 255, 'cst', True, 0.2], None, None, None, ['LaReole', 34, 18, 7, 255, 'cst', True, 0.2], None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Yvrac', 27, 12, 4, 255, 'cst', True, 0.0], ['LibourneVille', 11, 5, 2, 255, 'cst', False, 0.0], None, ['Chalais', 31, 13, 5, 255, 'cst', True, 0.0], None, ['AntenneLib21', 21, 9, 3, 255, 'cst', False, 0.0], None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Libourne', 31, 13, 5, 255, 'cst', True, 0.0], None,None, None, None, None, None, None, None, None, None, None, None], [None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Dronne', 18, 9, 3, 255, 'cst', False, 0.0], None, None, None, None, None], [None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Libourne', 21, 9, 3, 255, 'cst', True, 0.0], None, None, None, ['FoyLaGrande', 13, 6, 2, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['LibourneVille', 29, 15, 6, 255, 'cst', False, 0.2], None, None, None, ['AntenneLib21', 13, 6, 2, 255, 'cst', False, 0.0], None, ['Bergerac', 24, 10, 7, 255, 'cst', True, 0.1], None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['FoyLaGrande', 24, 10, 7, 255, 'cst', True, 0.1], None, ['Perigueux', 42, 18, 7, 255, 'cst', True, 0.0], None, None, ['Marmande', 39, 16, 6, 255, 'cst', True, 0.0], None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Bergerac', 42, 18, 7, 255, 'cst', True, 0.0], None, ['Dronne', 23, 10, 4, 255, 'cst', False, 0.0], None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Riberac', 18, 9, 3, 255, 'cst', True, 0.0], None, None, None, ['Perigueux',23, 10, 4, 255, 'cst', True, 0.0], None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['LibourneVille', 34, 18, 7, 255, 'cst', False, 0.2], None, None, None, None, None, None, None, None, None, ['Marmande', 19, 9, 3, 255, 'cst', True, 0.0], None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Bergerac', 39, 16, 6, 255, 'cst', True, 0.0], None, None, ['LaReole',19, 9, 3, 255, 'cst', True, 0.0], None, ['Autoroute', 23, 9, 3, 255, 'cst', False, 0.0], None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Marmande', 23, 9, 3, 255, 'cst', True, 0.0], None, ['Agen', 26, 12, 4, 255, 'cst', True, 0.0], None], [None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Autoroute', 26, 12,4, 255, 'cst', False, 0.0], None, None], [None, None, None, None, None, ['Cazaux', 13, 6, 2, 255, 'cst', False, 0.5], ['Biscarrosse', 11, 5, 2, 255, 'cst', True, 0.7], None, None, None, None, None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None]]


def dist(grph : np.array, a : int, b : int) -> float :
    """ distance en km entre deux points, ramenée entre 0 et 1, 1 étant le plus favorable """
    if grph[a][b] is None : #☻  #♠
        return (-5)
    else :
        return (grph[a][b][1] /100)

#d = dist(g, 1, 5)
#d2 = dist(g, 1, 3)
#print(d, d2)


def tps(grph : np.array, a : int, b : int) -> float :
    """ distance en min entre deux points ramenée entre 0 et 1, 1 étant le plus favorable """
    if grph[a][b] is None : #☻
        return (-5)
    else :
        return (grph[a][b][2] /60)

#t = tps(g, 1, 5)
#t2 = tps(g, 1, 3)
#print(t, t2)


def deriv(grph : np.array, poids : np.array) -> float :
    return #quand cette fonction sera faite, il faudra utiliser la fonction ponderation mise en commentaire (avec le coef qui prend en compte l'angle de deviation) et modifier tous les appels à ponderation en rajoutant un paramètre

def aero(grph : np.array, a : int, b : int) -> float :
    """ 1 si le point est un aérodrome, 0 sinon """
    if grph[a][b] is None : #☻
        return (-5)
    else :
        if (grph[a][b][6]) : return 1
        else : return 0

#a = aero(g, 1, 5)
#a2 = aero(g, 1, 3)
#print(a, a2)


def zone(grph : np.array, a : int, b : int) -> float :
    """ zone à éviter définies par des réglementations officielles (exemple : Bordeaux = 0.7 > village = 0.2)
 """
    if grph[a][b] is None : #☻
        return (-5)
    else :
        return (1 - grph[a][b][7])

#z = zone(g, 1, 5)
#z2 = zone(g, 1, 3)
#print(z, z2)


#fonction ponderation avec l'angle de derivation :
# def ponderation(grph : np.array, depart: int, arrivee :int, coef0 : int, coef1 : int, coef2 : int, coef3 : int, coef4 : int) -> float :
#     """ renvoie la moyenne (pondérée des poids pondérée par les coefficients pris en paramètre) des 5 catégories prises en compte, entre 0 et 1 """
#     poids_global = (coef0*dist(g,depart,arrivee) + coef1*tps(g,depart,arrivee) + coef2*deriv(g,depart,arrivee) + coef3*aero(g,depart,arrivee) + coef4*zone(g,depart,arrivee)) / (coef0 + coef1 + coef2 + coef3 + coef4)
#     return poids_global

def ponderation(grph : np.array, depart: int, arrivee :int, coef0 : int, coef1 : int, coef3 : int, coef4 : int) -> float :
    """ renvoie la moyenne (pondérée des poids pondérée par les coefficients pris en paramètre) des 5 catégories prises en compte, entre 0 et 1 """
    poids_global = (coef0*dist(g,depart,arrivee) + coef1*tps(g,depart,arrivee) + coef3*aero(g,depart,arrivee) + coef4*zone(g,depart,arrivee)) / (coef0 + coef1 + coef3 + coef4)
    return poids_global

#p = ponderation(g, 1, 5, 1, 1, 1, 1)
#p2 = ponderation(g, 1, 3, 1, 1, 1, 1)
#print(p, p2)


def tab_poids(grph : np.array) :
    """ poids = matrice d'adjacence du graphe contenant les ponderations des arêtes du graphe """
    poids = [[0 for j in range(31)] for i in range(31)]
    for i in range(31) :
        for j in range(31) :
            poids[i][j] = ponderation(grph,i,j,1,1,1,1)
    return poids

#poids = tab_poids(g)



