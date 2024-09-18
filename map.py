from rumano import graph # Mapa de Rumania con las distancias entre las ciudades
from rumano import ucsRute, aStarRute
import networkx as nx
print(nx.__version__)
import matplotlib.pyplot as plt

# Creación del grafo usando NetworkX
G = nx.Graph()

# Añadir nodos y aristas con los pesos (distancias)
for city, neighbors in graph.items():
    for neighbor, distance in neighbors.items():
        G.add_edge(city, neighbor, weight=distance)

# Posiciones aproximadas de las ciudades en un plano (solo para ilustración)
positions = {
    'Arad': (1, 5), 'Zerind': (2, 6), 'Oradea': (3, 7),
    'Sibiu': (3, 5), 'Timisoara': (1, 3), 'Lugoj': (2, 2),
    'Mehadia': (3, 1), 'Drobeta': (4, 0), 'Craiova': (6, 1),
    'Rimnicu Vilcea': (5, 4), 'Fagaras': (6, 5), 'Pitesti': (6, 3),
    'Bucharest': (8, 3), 'Giurgiu': (9, 2), 'Urziceni': (9, 4),
    'Hirsova': (10, 5), 'Eforie': (11, 6), 'Vaslui': (10, 7),
    'Iasi': (9, 8), 'Neamt': (8, 7)
}

# Rutas obtenidas por los algoritmos
aStarRute
ucsRute

# Dibujar el grafo completo
plt.figure(figsize=(10, 8))
nx.draw(G, pos=positions, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=labels)

# Dibujar la ruta de A* en rojo
aStarRute_edges = [(aStarRute[i], aStarRute[i+1]) for i in range(len(aStarRute)-1)]
nx.draw_networkx_edges(G, pos=positions, edgelist=aStarRute_edges, edge_color='red', width=3, label='Ruta A*')

# Dibujar la ruta de UCS en verde
ruta_ucs_edges = [(ucsRute[i], ucsRute[i+1]) for i in range(len(ucsRute)-1)]
nx.draw_networkx_edges(G, pos=positions, edgelist=ruta_ucs_edges, edge_color='green', width=3, label='Ruta UCS')

# Añadir leyenda y título
plt.legend(['Ruta A*', 'Ruta UCS'])
plt.title('Comparación de rutas: A* y Búsqueda de Costo Uniforme', fontsize=15)
plt.show()
