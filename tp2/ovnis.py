import random
import sys
from collections import deque

class Grafo:

    """ Crea el grafo eligiendo si este va a ser o no dirigido, será dirigido por default """
    def __init__(self, dirigido=False, pesado=False):
        self.vertices = {}
        self.datos = {}
        self.esDirigido = dirigido
        self.esPesado = pesado

    """ Devuelve la cantidad de vertices que tiene el grafo """

    def __len__(self):
        return len(self.vertices)

    """ devuelve True si vertice existe en el grafo, caso contrario devuelve False """

    def existeVertice(self, vertice):
        return vertice in self.vertices

    """ devuelve True si existe la arista origen - destino. caso contrario devuelve False """

    def existeArista(self, origen, destino):
        if origen not in self.vertices:
            return False
        if destino not in self.vertices[origen]:
            return False
        return True
    """ Agrega el vertice (con su dato) al grafo en caso de no existir, caso contrario modifica el dato del vertice ya existente """

    def insertarVertice(self, vertice, dato=None):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
        self.datos[vertice] = dato

    """inserta una arista de origen a destino de peso. si alguno de los vertices no existe, lo agrega con dato None"""

    def insertarArista(self, origen, destino, peso=None):
        if not self.esPesado:
            peso = None
        if origen not in self.vertices:
            self.insertarVertice(origen)
        if destino not in self.vertices:
            self.insertarVertice(destino)
        self.vertices[origen][destino] = peso
        if not self.esDirigido:
            self.vertices[destino][origen] = peso

    """devuelve una lista con los adyacentes del vertice"""

    def adyacentes(self, vertice):
        if vertice in self.vertices:
            return list(self.vertices[vertice].keys())

    """elimina el vertice del grafo y devuelve su dato. si el vertice no existia devuelve False"""

    def borrarVertice(self, vertice):
        if vertice not in self.vertices:
            return False
        for i in self.vertices:
            if vertice in self.vertices[i]:
                self.vertices[i].pop(vertice)
        self.vertices.pop(vertice)
        return self.datos.pop(vertice)

    """elimina la arista origen - destino. si es un grafo no dirigido el orden de los vertices es indistinto. si alguno de esos vertices no existe devuelve False"""

    def borrarArista(self, origen, destino):
        if origen not in self.vertices or destino not in self.vertices:
            return False
        self.vertices[origen].pop(destino)
        if not self.esDirigido:
            self.vertices[destino].pop(origen)

    """devuelve True si destino es adyacente de origen. caso contrario devuelte False"""

    def verticesSonAdyacentes(self, origen, destino):
        if origen not in self.vertices:
            return False
        return destino in self.vertices[origen]

    """devuelve el peso de la arista origen - destino. si no existe devuelve False. si es un grafo no pesado devuelve None"""

    def pesoArista(self, origen, destino):
        if self.verticesSonAdyacentes(origen, destino):
            return self.vertices[origen][destino]
        return False

    """cambia el peso de la arista origen - destino si existe. devuelte true o false si exisitia"""
    def cambiarPeso(self, origen, destino, pesoNuevo):
        if self.verticesSonAdyacentes(origen, destino):
            self.vertices[origen][destino] = pesoNuevo
            return True
        return False
    """devuelve el dato en el vertice. si no existe ese vertice, devuelve False"""

    def datoVertice(self, vertice):
        if vertice not in self.vertices:
            return False
        return self.datos[vertice]

    """devuelve una lista con todos los vertices del grafo"""

    def listaVertices(self):
        return list(self.vertices.keys())

    """devuelve un vertice aleatorio"""

    def verticeAleatorio(self):
        return random.choice(list(self.vertices))

    def __iter__(self):
        return iter(self.vertices.keys())

    def __str__(self):
        res = ''
        for i in self.vertices:
            res += str(i) + '-->'
            if (len(self.vertices[i]) != 0):
                res += str(self.vertices[i].copy()) + '\n'
            else:
                res += '\n'
        return res

def bfs(grafo, origen):
    visitados = set()
    padres = {}
    orden = {}
    padres[origen] = None
    orden[origen] = 0
    visitados.add(origen)
    q = deque()
    q.append(origen) #encolar
    while len(q) != 0:
        v = q.popleft() #desencolar
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                q.append(w)
    return padres, orden
def reconstruirCamino(padres, destino):
    recorrido = []
    while destino is not None:
        recorrido.append(destino)
        try:
            destino = padres[destino]
        except KeyError:
            return None
    return recorrido[::-1]

def bfsHasta(grafo, origen, destino):
    padres, orden = bfs(grafo, origen)
    return reconstruirCamino(padres, destino)
def copiarGrafo(grafo):
    copia = Grafo(True, True)
    for v in grafo:
        for w in grafo.adyacentes(v):
                copia.insertarArista(v, w, grafo.pesoArista(v,w))
    return copia
def minPeso(grafo, camino):
    p = grafo.pesoArista(camino[0], camino[1])
    for i in range(1, len(camino)):
        if p > grafo.pesoArista(camino[i-1], camino[i]):
            p = grafo.pesoArista(camino[i - 1], camino[i])
    return p

def actualizarGrafoResidual(residual, u, v, valor):
    pesoAnterior = residual.pesoArista(u,v)
    if pesoAnterior == valor:
        residual.borrarArista(u,v)
    else:
        residual.cambiarPeso(u,v, pesoAnterior-valor)
    if not residual.existeArista(v, u):
        residual.insertarArista(v, u, valor)
    else:
        residual.cambiarPeso(v, u, pesoAnterior + valor)

def fordFulkersonFlujoMaximo(grafo, s, t):
    flujo = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v,w)] = 0
    grafoResidual = copiarGrafo(grafo)
    camino = bfsHasta(grafoResidual, s, t)
    while camino is not None:
        capacidadResidualCamino = minPeso(grafoResidual, camino)
        for i in range(1, len(camino)):
            if grafo.existeArista(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += capacidadResidualCamino
                actualizarGrafoResidual(grafoResidual, camino[i-1], camino[i],capacidadResidualCamino)
            else:
                flujo[(camino[i], camino[i-1])] -= capacidadResidualCamino
                actualizarGrafoResidual(grafoResidual, camino[i], camino[i-1], capacidadResidualCamino)
        camino = bfsHasta(grafoResidual, s, t)
    return flujo, grafoResidual

def eliminarCiclosParaRedDeFlujo(grafo):
    copia = copiarGrafo(grafo)
    aristasBi = set()
    diccionarioDeAristas = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            if grafo.existeArista(v, w) and grafo.existeArista(w, v):
                if (v,w) not in aristasBi and (w,v) not in aristasBi:
                    aristasBi.add((v,w))
    for i in aristasBi:
        v, w = i
        peso = grafo.pesoArista(v,w)
        copia.borrarArista(v,w)
        copia.insertarArista(v, str(v) + str(w), peso)
        diccionarioDeAristas[(v, str(v) + str(w))] = (v, w)
        diccionarioDeAristas[(str(v) + str(w), w)] = (v, w)
        copia.insertarArista(str(v) + str(w), w, peso)
    return copia, diccionarioDeAristas
def flujoMaximo(flujo, t):
    max = 0
    for i in flujo:
        u,v = i
        if v == t:
            max += flujo[(u,v)]
    return max

def construirRed(aristas):
    red = Grafo(True, True)
    aristasDeR = []
    for a in aristas:
        u,v, p = a
        if u == 'R':
            red.insertarVertice(u)
            aristasDeR.append((u, v, p))
        elif v == 'S':
            red.insertarArista(u, v, p)
        else:
            red.insertarArista(u, v, p)
            red.insertarArista(v, u, p)
    red, dicc = eliminarCiclosParaRedDeFlujo(red)
    return red, dicc, aristasDeR

def corteMinimo(grafo, residual, s):
    padres, origen = bfs(residual, s)
    subConjuntoS = set()
    aristasCorteMinimo = []
    for i in padres:
        subConjuntoS.add(i)
    for v in grafo:
        for w in grafo.adyacentes(v):
            if v in subConjuntoS and w not in subConjuntoS:
                aristasCorteMinimo.append((v,w))
    return aristasCorteMinimo

def encontrarConexionOptima(red, aristasAProbar, s, t):
    max = 0
    aristaUsada = None
    aristasCorteMinimo = None
    for i in aristasAProbar:
        o, d, p = i
        red.insertarArista(o,d,p)
        flujo, residual = fordFulkersonFlujoMaximo(red, s, t)
        maxLocal = flujoMaximo(flujo, t)
        if maxLocal >= max:
            max = maxLocal
            aristaUsada = i
            aristasCorteMinimo = corteMinimo(red, residual, s)
        red.borrarArista(o,d)
    return max, aristaUsada, aristasCorteMinimo

def traducirAristasLimitantes(aristas, diccionario):
    aux = aristas
    for i in range(len(aristas)):
        if aristas[i] in diccionario:
            aux[i] = diccionario[aristas[i]]
    return aux

# __ MAIN __
argumentos = sys.argv
if len(argumentos) != 2:
    print("ERROR")
    sys.exit()

with open(argumentos[1], 'r') as archivo:
    lineas = archivo.readlines()

aristas = []
for l in lineas:
    elementos = l.strip().split(',')
    aristas.append((str(elementos[0]), str(elementos[1]), int(elementos[2])))

r, d, a = construirRed(aristas)
max, aristaFinal, aristasLimitantes = encontrarConexionOptima(r, a, 'R', 'S')
aristasLimitantes = traducirAristasLimitantes(aristasLimitantes, d)
print("el flujo maximo de la red usando la conexion " + str(aristaFinal) + " es de " + str(max))
print("\nlas aristas que  limitan este flujo  y que deberian ser mejoradas son: ")
for i in aristasLimitantes:
    print("\t" + str(i))
