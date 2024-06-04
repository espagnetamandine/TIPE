import matplotlib.pyplot as plt

# Fonction pour dessiner le graphe
def draw_graph(graph):
    fig, ax = plt.subplots()
    
    # Position des nœuds pour une disposition simple
    positions = { #visualiser avec le graphe creer par matplotlib
        1: (1, 2), # coord (x,y)
        2: (2, 3),
        3: (2, 1),
        4: (3, 2),
        5: (4, 2)
    }
    
    # Dessiner les nœuds
    for node, (x, y) in positions.items():
        ax.scatter(x, y, s=700, c='skyblue')
        ax.text(x, y, str(node), fontsize=15, ha='center', va='center', color='black')
    
    # Dessiner les arêtes
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            x1, y1 = positions[node]
            x2, y2 = positions[neighbor]
            ax.plot([x1, x2], [y1, y2], 'gray')
    
    plt.axis('off')
    plt.show()

# Dessiner le graphe
draw_graph(graph)

import numpy as np

def transfo_nom(depart : str, arrivee : str) -> (int, int) :
    """transforme les chaines de caractères des aéroclub en indice pour l'algo de dijstra
    """
    L = []
    return (L.index(depart), L.index(arrivee))

def aide_crea_grph() -> np.array :
    """facilite création big graph"""
    grph = []
    N = int(input('Nombre de points importants :'))
    for i in range(N) :
        L = []
        for j in range(N) :
            distance = int(input('dist'))
            temps = int(input('temps'))
            Vabs = int(input('Vabsolue'))
            Vrel = int(input('Vréelle'))
            vent = int(input('vent'))
            L.append((j, distance, temps, Vabs, Vrel, vent))
        grph.append(L)
    return grph




def dijkstra(grph : np.array, v_init) -> dict :
    """algorithme du plus court chemin (dijkstra)

    Entrée :
    --------
    grph : np.array, une matrice d'adjacence un peu remodelée : 0 si pas de liaison possible et un tuple avec les information pour aller au noeud suivant si arrête
    [[(0->0), (0->1), (0->2),],
    [],
    []
    ]

    Sortie :
    plus_cours : dict, dictionnaire avec comme clés les noeuds visités et les infos sur qu'il a fallu mettre à jour pour y arriver
    """
    plus_cours = {v_init : (0, 0, 0, 0, 0)} #distance, temps, Vabsolue, Vréelle, vent
    visited = {x : False for x in range(len(grph))}
    pred = {x : None for x in range(len(grph))}
    dist = {x : float('inf') for x in range(len(grph))}
    dist[v_init] = 0
    hq = [(0, plus_court[v_init])]
    heapq.heapify(hq)
    while len(hq) > 0 :
        dv, v = heapq.heappop(hq)
        if not visited[v] :
            visited[v] = True
            for w in grph[v] :
                if w != (0) :
                    if not visited[w[0]] :
                        dw = dv + w[1]
                        if dw < dist[w[0]] :
                            dist[w[0]] = dw
                            pred[w[0]] = v
                            heapq.heappush(hq, (dw, w))
    return plus_cours

