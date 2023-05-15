#NAHMAN MARTINA L:13685
#Graph = Array(n,LinkedList())
from collections import deque
#EJERCICIO 1
#lista de vertices y lista de aristas
#recorrer toda la lista de vertices y en ese recorrido que devuelva
#  una lista con todas nodos que tienen como primer componente el vertice con el que estamos 
def createGraph(LA,LV):
    l_ady=[]
    for vertices in LV:
        lis=[]
        lis.append(vertices)
        l_ady.append(lis)
    for vertice in l_ady:
    #recorremos los vertices
        for aristas in LA:
            vertice[0]
            if vertice[0]==aristas[0]:
                vertice.append(aristas[1])
    return(l_ady)

#EJERCICIO 2
#operación existe camino que busca si existe un camino entre los vértices v1 y v2
def existPath(Grafo, v1, v2): 
    list= DFS(Grafo)
    if (v1 in list) and ( v2 in list):
        return True
    else:
        return False

#RECORRIDO DFS (PROFUNDIDAD)
def DFS(grafo):
    vertice = None
    visitados = []
    dfsR(grafo,visitados,vertice)
    return visitados

def dfsR(grafo, visitados,vertice):
    for i in range (len(grafo)):
        #chequeamos que los vertices tengan vertices adyacentes
        if len(grafo[i]) != 1:
            for j in range (len(grafo[i])):
                if grafo[i][j] not in visitados:
                    vertice=grafo[i][j]
                    visitados.append(vertice)
                    dfsR(grafo, visitados, vertice)
    # Retornar la lista de vértices visitados
    return visitados

#EJERCICIO 3
#Implementa la operación es conexo
def isConnected(Grafo):
    listA= DFS(Grafo)
    if len(listA) == len(Grafo):
        return True
    else:
        return False
    
#EJERCICIO 4
#Implementa la operacion es arbol
#arbol: aciclico / conexo / n-1 aristas
def isTree(Grafo,LA):
    conexo = isConnected(Grafo)
    #chequeo aristas = n-1
    
    if (len(Grafo)-1) == (len(LA)/2):
        checkedge = True

    if (conexo and checkedge) == True:
        return True
    else: return False

#EJERCICIO 5
#Implementa operacion arbol completo
#Arbol completo: existe una arista entre todo par de vértices.
def isComplete(Grafo):
    #verificar si cumple con: n (n-1)/2 aristas
    vertices= Grafo[0]
    for i in range (len(vertices)):
        for j in range(i+1,len(vertices)):
            if vertices[j] not in Grafo[vertices[i]]:
                return False
    # Si se recorren todas las combinaciones posibles de vértices
    # y no se encuentra ninguna que no esté conectada por una arista, se devuelve True
    return True

#EJERCICIO 6 VEEEEEEEEER!!!!!!!
#Implementar una función que dado un grafo 
#devuelva una lista de aristas que si se eliminan el grafo se convierte en un árbol
def convertTree(Grafo):
    aristasArbol = []
    for vertice in Grafo:
        for aristas in Grafo[vertice]:
            Grafo[vertice].pop(vertice)
            Grafo[aristas].pop(aristas)
            
            #verificamos si el grafo es conexo:
            if isConnected(Grafo) == True:
                tupla=(vertice,aristas)
                aristasArbol.append(tupla)
            #restauramos la arista eliminada    
            Grafo[vertice].append(vertice)
            Grafo[aristas].append(aristas)
    return aristasArbol

#EJERCICIO 7 
#número de componentes conexas que componen el grafo.
def countConnections(Grafo):
    #será longitud visitados???????????
    connections = DFS(Grafo)
    return (len(connections))

#EJERCICIO 8 

#EJERCICIO 10
# Encuentra el camino más corto, en caso de existir, entre dos vértices
def bestRoad(Grafo, v1, v2):
    visitados = []
    queue = deque([v1])
    parent = [v1]
    while queue:
        #popleft() de la cola deque elimina y devuelve el primer elemento de la cola
        values = queue.popleft()
        if values == v2:
            way = []
            while values is not None:
                way.append(values)
                values = parent[values]
            way.reverse()
            return way
        for vecino in Grafo[values]:
            if vecino not in visitados:
                visitados.append(vecino)
                parent[vecino] = values
                queue.append(vecino)
    return None
