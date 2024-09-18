import heapq
from rumano import graph
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