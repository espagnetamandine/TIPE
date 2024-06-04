import numpy as np

annulaire = [("Saucats", True),
("Merignac", True),
("AntenneBdx", False),
("Andernos", True),
("Arcachon", True),
("Cazaux", False),
("Biscarrosse", True),
("Mimizan", True),
("Biarritz", True),
("Leyre", False),
("Garonne", False),
("Bordeaux", False),
("L.St Laurent", True),
("Soulac", True),
("Montendre", True),
("Jonzac", True),
("Yvrac", True),
("LibourneVille", False),
("Libourne", True),
("Chalais", True),
("Riberac", True),
("AntenneLib21", False),
("FoyLaGrande", True),
("Bergerac", True),
("Perigueux", True),
("Dronne", False),
("LaReole", True),
("Marmande", True),
("Autoroute", False),
("Agen", True),
("AntenneBisca", False),
]

def voisin(g) -> None :
    """ rempli le tab avec des 1 pour les couples de voisins """
    fini = 0
    while fini==0 :
        u, v = int(input("depart")), int(input("arrivee"))
        #♥
        g[u][v], g[v][u] = 1, 1
        fini = int(input("fini ?"))


def tableau_zeros() -> np.array :
    """structure ++ (tableaude 0 et de 1"""
    N = int(input('Nombre de points importants :'))
    g = [[0 for i in range(N)] for j in range(N)]
    return g

def crea_init(grph : np.array) -> np.array :
    """ structure graphe"""
    N = len(grph)
    for i in range(N):
        for j in range(N):
            if grph[i][j] == 0:
                grph[i][j]= (None)
            else :
                grph[i][j] = ["0", 0, 0, 0, 255, 'cst', 0, 0.]
    return grph




def aide_crea_points(grph : np.array, i_init : int) -> None:
    """facilite création big graph
    si on se gourre, on reprend de la ligne i_init ( du point i_init)"""
    N = len(grph)
    for i in range(i_init, N):
        for j in range(N):
            if (grph[i][j] != (None)) and (grph[i][j][0] == "0"):
                print(i,j)
                grph[i][j][0], grph[j][i][0] = annulaire[j][0], annulaire[i][0]
                distance = int(input('dist'))
                grph[i][j][1], grph[j][i][1] = distance,distance
                temps = int(input('temps'))
                grph[i][j][2], grph[j][i][2] = temps, temps
                essence = int(input('essence'))
                grph[i][j][3], grph[j][i][3] = essence, essence
                grph[i][j][6], grph[j][i][6] = annulaire[j][1], annulaire[i][1]
                interdit = float(input("zone interdite"))
                grph[i][j][7],grph[j][i][7] = interdit, interdit
        print('fin de ligne')
    return grph




######construction du graphe :
#grph = tableau_zeros()
#voisin(grph)
grph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0,
0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 1,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
0, 1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0
, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


grph = crea_init(grph)
#print(grph)
grph = aide_crea_points(grph,0)
#print(grph)


#info_grph = {0:"nom", 
#1:"dist", 
#2:"temps", 
#3:"essence", 
#4:"vitesse de l'avion", 
#5:"vitesse du vent", 
#6:"aerodrome", 
#7:"zone interdite"}


grph =[[None, ['Merignac', 16, 7, 3, 255, 'cst', True, 0.5], ['AntenneBdx', 13, 6, 2,255, 'cst', False, 0.0], None, None, None, None, None, None, ['Leyre', 45, 24, 9, 255, 'cst', False, 0.0], ['Garonne', 11, 6, 2, 255, 'cst', False, 0.0], None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 16, 7, 3, 255, 'cst', True, 0.5], None, ['AntenneBdx', 13, 6, 2, 255, 'cst', False, 0.0], ['Andernos', 26, 12, 4, 255, 'cst', True, 0.2], None, None, None, None, None, None, None, ['Bordeaux',11, 4, 1, 255, 'cst', False, 0.7], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 13, 6, 2, 255, 'cst', True, 0.0], ['Merignac', 13, 6, 2, 255, 'cst', True, 0.0], None, ['Andernos', 21, 9, 3, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None], [None, ['Merignac', 26, 12, 4, 255, 'cst', True, 0.2], ['AntenneBdx', 21, 9, 3, 255, 'cst', False,0.0], None, ['Arcachon', 16, 6, 2, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, ['Andernos', 16, 6, 2, 255, 'cst', True, 0.0], None, ['Cazaux', 6, 3, 1, 255, 'cst',False, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, ['Arcachon', 6, 3, 1, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['AntenneBisca', 13, 6, 2, 255, 'cst', False, 0.5]], [None, None, None, None, None, None, None, ['Mimizan', 23, 9, 3, 255, 'cst', True, 0.0], None, ['Leyre', 29, 13, 5, 255, 'cst', False, 0.2], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['AntenneBisca', 11,5, 2, 255, 'cst', False, 0.7]], [None, None, None, None, None, None, ['Biscarrosse', 23, 9, 3, 255, 'cst', True, 0.0], None, ['Biarritz', 71, 31, 11, 255, 'cst', True, 0.1], ['Leyre', 32, 13, 5, 255, 'cst', False, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, ['Mimizan', 71, 31, 11, 255, 'cst', True, 0.1], None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 45, 24, 9, 255, 'cst', True, 0.0], None, None, None, None, None, ['Biscarrosse', 29, 13, 5, 255, 'cst', True, 0.2], ['Mimizan', 32, 13, 5, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [['Saucats', 11, 6, 2, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Yvrac', 21, 9, 3, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, ['Merignac', 11, 4, 1, 255, 'cst',True, 0.7], None, None, None, None, None, None, None, None, None, None, ['L.St Laurent', 34, 15, 6, 255, 'cst', True, 0.0], None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None], [None,None, None, None, None, None, None, None, None, None, None, ['Bordeaux', 34, 15, 6, 255, 'cst', False, 0.0], None, ['Soulac', 32, 18, 7, 255, 'cst', True, 0.0], None, ['Jonzac', 42, 18, 7, 255, 'cst', True, 0.5], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, ['L.St Laurent', 32, 18, 7, 255, 'cst', True, 0.0], None, None, ['Jonzac', 45, 21, 8, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Jonzac', 21, 10, 4, 255, 'cst', True, 0.0], ['Yvrac', 39, 18, 7, 255, 'cst', True, 0.5], None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, ['L.St Laurent', 42, 18, 7, 255, 'cst', True, 0.5], ['Soulac', 45, 21, 8, 255, 'cst', True, 0.0], ['Montendre', 21, 10, 4, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, ['Garonne', 21, 9, 3, 255, 'cst', False, 0.0], None, None, None, ['Montendre', 39, 18, 7, 255, 'cst', True, 0.5], None, None, ['LibourneVille', 18, 9, 3, 255, 'cst', False, 0.5], ['Libourne', 27, 12, 4, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Yvrac', 18, 9, 3, 255, 'cst', True, 0.5], None, ['Libourne', 11, 5, 2, 255, 'cst', True, 0.0], None, None, None, ['FoyLaGrande', 29, 15, 6, 255, 'cst', True, 0.2], None, None, None, ['LaReole', 34, 18, 7, 255, 'cst', True, 0.2], None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Yvrac', 27, 12, 4, 255, 'cst', True, 0.0], ['LibourneVille', 11, 5, 2, 255, 'cst', False, 0.0], None, ['Chalais', 31, 13, 5, 255, 'cst', True, 0.0], None, ['AntenneLib21', 21, 9, 3, 255, 'cst', False, 0.0], None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Libourne', 31, 13, 5, 255, 'cst', True, 0.0], None,None, None, None, None, None, None, None, None, None, None, None], [None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Dronne', 18, 9, 3, 255, 'cst', False, 0.0], None, None, None, None, None], [None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Libourne', 21, 9, 3, 255, 'cst', True, 0.0], None, None, None, ['FoyLaGrande', 13, 6, 2, 255, 'cst', True, 0.0], None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['LibourneVille', 29, 15, 6, 255, 'cst', False, 0.2], None, None, None, ['AntenneLib21', 13, 6, 2, 255, 'cst', False, 0.0], None, ['Bergerac', 24, 10, 7, 255, 'cst', True, 0.1], None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['FoyLaGrande', 24, 10, 7, 255, 'cst', True, 0.1], None, ['Perigueux', 42, 18, 7, 255, 'cst', True, 0.0], None, None, ['Marmande', 39, 16, 6, 255, 'cst', True, 0.0], None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Bergerac', 42, 18, 7, 255, 'cst', True, 0.0], None, ['Dronne', 23, 10, 4, 255, 'cst', False, 0.0], None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Riberac', 18, 9, 3, 255, 'cst', True, 0.0], None, None, None, ['Perigueux',23, 10, 4, 255, 'cst', True, 0.0], None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['LibourneVille', 34, 18, 7, 255, 'cst', False, 0.2], None, None, None, None, None, None, None, None, None, ['Marmande', 19, 9, 3, 255, 'cst', True, 0.0], None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Bergerac', 39, 16, 6, 255, 'cst', True, 0.0], None, None, ['LaReole',19, 9, 3, 255, 'cst', True, 0.0], None, ['Autoroute', 23, 9, 3, 255, 'cst', False, 0.0], None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Marmande', 23, 9, 3, 255, 'cst', True, 0.0], None, ['Agen', 26, 12, 4, 255, 'cst', True, 0.0], None], [None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ['Autoroute', 26, 12,4, 255, 'cst', False, 0.0], None, None], [None, None, None, None, None, ['Cazaux', 13, 6, 2, 255, 'cst', False, 0.5], ['Biscarrosse', 11, 5, 2, 255, 'cst', True, 0.7], None, None, None, None, None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None, None, None]]