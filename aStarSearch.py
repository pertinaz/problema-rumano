from rumano import graph,heuristic
import heapq

""" Metodo de busqueda algoritmo A* 
g(n) = funcion de costo
h(n) = funcion heuristica

f(n)=g(n)+h(n) = nodo de menor valor para explorar

"""

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