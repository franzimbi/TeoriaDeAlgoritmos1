import sys
import heapq
import math
import time


def funcionCosto(proxCandidato, puestosCubiertos, cantidadTareas,):
    aux = cantidadTareas - len(puestosCubiertos)
    return math.ceil(aux/(len(proxCandidato)-1)) # redondea para arriba

def _bAb(candidatos, cantidadPuestos):
    candidatos = sorted(candidatos, key=len, reverse=True)
    heap = []
    heapq.heappush(heap, (0, 0, set(), []))  # (costoAcumulado, indice, puestosCubiertos, solucionActual)
    mejorSolucion = None
    cantidadCandidatos = len(candidatos)
    while len(heap) != 0:
        costoAcumulado, indice, puestosCubiertos, solucionActual = heapq.heappop(heap)
        if mejorSolucion is not None and len(solucionActual) >= len(mejorSolucion):
            continue
        if len(puestosCubiertos) == cantidadPuestos:
            mejorSolucion = solucionActual
            continue
        if indice < cantidadCandidatos:
            c = candidatos[indice]
            puestoOfrecido = set(c[1:]) - puestosCubiertos
            costo = funcionCosto(c, puestosCubiertos, cantidadPuestos)
            if mejorSolucion is not None and costo + len(solucionActual) >= len(mejorSolucion):
                continue
            # sin agregar el candidato
            heapq.heappush(heap, (costoAcumulado, indice + 1, puestosCubiertos.copy(), solucionActual.copy()))
            # agregando el candidato
            heapq.heappush(heap, (costoAcumulado + costo, indice + 1, puestosCubiertos | puestoOfrecido, solucionActual + [c[0]]))

    return mejorSolucion

def chequeoSolucion(candidatos, solucion, puestos):
    cubiertos = set()
    for candidato in solucion:
        for c in candidatos:
            if c[0] == candidato:
                cubiertos |= set(c[1:])
                break
    return cubiertos == set(puestos)

def personalOptimo(candidatos, puestos):
    solucion = _bAb(candidatos, len(puestos))
    if solucion is not None and chequeoSolucion(candidatos, solucion, puestos):
        return solucion
    else:
        return None

######### MAIN #############
argumentos = sys.argv
if len(argumentos) != 3:
    print("ERROR")
    sys.exit()

with open(argumentos[1], 'r') as archivo:
    lineas = archivo.readlines()
listaTareas = []
listaIdTareas = []

for l in lineas:
    elementos = l.strip().split(',')
    listaTareas.append(elementos[1])
    listaIdTareas.append(int(elementos[0]))

with open(argumentos[2], 'r') as archivo:
    lineas = archivo.readlines()
listaCandidatos = []
for l in lineas:
    elementos = l.strip().split(',')
    aux = []
    aux.append(elementos.pop(0))
    for i in elementos:
        aux.append(int(i))
    listaCandidatos.append(aux)

res = personalOptimo(listaCandidatos, listaIdTareas)
if res == None:
    print("No tiene solucion")
else:
    for i in res:
        print(i)

