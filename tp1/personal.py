import math
import sys

def funcionCosto(proxCandidato, cantidadTareas, puestosCubiertos):
    aux = cantidadTareas - len(puestosCubiertos)
    return math.ceil(aux/(len(proxCandidato)-1)) # redondea para arriba

def _bAb(indice, candidatos, puestosCubiertos, solucionParcial, mejorSolucion, cantidadPuestos):
    if len(puestosCubiertos) == cantidadPuestos:
        return solucionParcial, len(puestosCubiertos)
    if indice == len(candidatos):
        return None, 0
    contadorPuestos = 0
    costo = funcionCosto(candidatos[indice], cantidadPuestos, puestosCubiertos)
    if len(solucionParcial) + costo <= len(mejorSolucion):
    # si el costo minimo es mayor al costo de la mejor solucion, podamos
        c = candidatos[indice]
        puestoOfrecido = set(c[1:]) - puestosCubiertos
        solucionParcial.append(c[0])
        puestosCubiertos |= puestoOfrecido
        s, tam = _bAb(indice + 1, candidatos, puestosCubiertos, solucionParcial, mejorSolucion, cantidadPuestos)
        if s != None and len(s) < len(mejorSolucion):
            mejorSolucion = s.copy()
            contadorPuestos = tam
        solucionParcial.remove(c[0])
        puestosCubiertos -= puestoOfrecido
        s, tam = _bAb(indice + 1, candidatos, puestosCubiertos, solucionParcial, mejorSolucion, cantidadPuestos)
        if s != None and len(s) < len(mejorSolucion):
            mejorSolucion = s.copy()
            contadorPuestos = tam
    return mejorSolucion, contadorPuestos
def personalOptimo(candidatos, puestos):
    candidatosOrdenados = sorted(candidatos, key=len, reverse=True) #ordeno candidatos de los q mas trabajos hacen a menos
    mejorSolucion = []
    for i in candidatosOrdenados:
        mejorSolucion.append(i[0])
    solucion, t = _bAb(0, candidatosOrdenados, set(), [], mejorSolucion, len(puestos))
    if t != len(puestos):
        return None
    return solucion


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

