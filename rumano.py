import heapq

""" Metodo de busqueda algoritmo A* 
g(n) = funcion de costo
h(n) = funcion heuristica

f(n)=g(n)+h(n) = nodo de menor valor para explorar

"""
#  Mapa de rumania
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
}

# Distancias heurísticas en línea recta a Bucarest
heuristic = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Timisoara': 329,
    'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Rimnicu Vilcea': 193,
    'Fagaras': 176, 'Pitesti': 100, 'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80,
    'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
}

# Algoritmo A*

def aStarSearch(graph, start,goal):
    openList = []
    heapq.heappush(openList, (0,start))

    #diccionario de costos y padres
    gCosts = {start:0}
    parents = {start:None}

    while openList:
        currentF,currentCity = heapq.heappop(openList)

        # reconstruir el camino al llegar al destino
        if currentCity == goal:
            path = []
            while currentCity:
                path.append(currentCity)
                currentCity = parents[currentCity]
            return path[::-1]
        


        #explorar vecinos
        for neighbor, distance in graph[currentCity].items():
            newG = gCosts[currentCity] + distance
            if neighbor not in gCosts or newG < gCosts[neighbor]:
                gCosts[neighbor] = newG
                fCost = newG + heuristic[neighbor]
                heapq.heappush(openList, (fCost,neighbor))
                parents[neighbor] = currentCity
    
    return None 


aStarRute = aStarSearch(graph,'Arad','Bucharest')
print("Ruta más corta A*: ", aStarRute)



""" Metodo de busqueda Algoritmo de coste uniforme (UCS)

Coste real acumulado

"""

def uniformCostSearch(graph,start,goal):
    # Cola de prioridad para seleccionar el nodo con el menor costo acumulado (g(n))
    openList = []
    heapq.heappush(openList,(0,start)) # costo acumulado, ciudad)

    # diccionarios de costos y padres
    gCost = {start:0} # coste acumulado
    parents = {start:None} # almacenar y reconstruir el camino 

    while openList:
        currentG, currentCity = heapq.heappop(openList)

        #reconstruir el camino al llegar al destino
        if currentCity == goal:
            path = []
            while currentCity:
                path.append(currentCity)
                currentCity=parents[currentCity]
            return path[::-1] # invertir el camino para mostrar origen-destino
        
        # explorar vecinos 
        for neighbor, distance in graph[currentCity].items():
            newG = currentG + distance # costo total desde este vecino

            # si el camino es mas barato al examinar los otros vecinos, actualizamos
            if neighbor not in gCost or newG < gCost[neighbor]:
                gCost[neighbor] = newG
                fCost = newG + currentG
                heapq.heappush(openList,(fCost,neighbor))
                parents[neighbor] = currentCity

    return None

ucsRute = uniformCostSearch(graph,'Arad','Bucharest')
print("Ruta más corta usando UCS: ",ucsRute)