import sys
def ordenarCandidatos(candidatos, cantidadTareas):  # O(C * T)
    ordenPorCantidad = list([] for _ in range(cantidadTareas)) # O(T) t: cantidad de tareas
    contador = [0]*cantidadTareas # O(n) n: cantidad de candidatos
    puestosUnicos = set()
    for candidato in candidatos: #O (n)
        ordenPorCantidad[len(candidato)-1].append(candidato)
        for tarea in candidato:
            if tarea!=candidato[0]:
                contador[tarea-1] += 1
    for i in range(len(contador)): # O(T)
        if contador[i] == 1:
            puestosUnicos.add(i+1)
    res = []
    for i in range(len(ordenPorCantidad)-1, 0 , -1):  # O(n)
        for candidato in ordenPorCantidad[i]: # O(T)
            agregado = False
            for c in candidato:
                if c in puestosUnicos:
                    res.insert(0, candidato)
                    agregado = True
                    break
            if not agregado:
                res.append(candidato)
    return res
def branchAndBound(candidatos, puestos):
    def _bAb(indice, candidatos, puestosCubiertos, solucionActual, mejorSolucion, cantidadPuestos):
        if len(puestosCubiertos) == cantidadPuestos:
            return solucionActual
        if indice == len(candidatos) or len(solucionActual) >= len(mejorSolucion):
            return None
        c = candidatos[indice]
        puestos = set(c[1:])
        puestoOfrecido = puestos - puestosCubiertos
        if len(puestoOfrecido) > 0:
            solucionActual.append(c[0])
            puestosCubiertos |= puestoOfrecido
            s = _bAb(indice + 1, candidatos, puestosCubiertos, solucionActual, mejorSolucion, cantidadPuestos)
            if s != None and len(s) < len(mejorSolucion):
                mejorSolucion = s.copy()
            solucionActual.remove(c[0])
            puestosCubiertos -= puestoOfrecido
            s = _bAb(indice + 1, candidatos, puestosCubiertos, solucionActual, mejorSolucion, cantidadPuestos)
            if s != None and len(s) < len(mejorSolucion):
                mejorSolucion = s.copy()
        return mejorSolucion

    candidatosOrdenados = ordenarCandidatos(candidatos, len(tareas))
    puestosCubiertos = set()
    mejorSolucion = []
    for i in candidatosOrdenados:
        mejorSolucion.append(i[0])
    return  _bAb(0, candidatosOrdenados, puestosCubiertos, [], mejorSolucion, len(puestos))


######### MAIN #############

tareas = ["Cocinar", "Primeros auxilios",
              "Meteorología", "astronomía", "Electricidad", "Mecanico", "Programador"]
candidatos = [["R.J. MacReady", 1, 5, 6], ["Nauls", 1, 2], ["Childs", 3, 7],
                  ["Dr. Copper", 2, 4], ["George Bennings", 1, 3], ["Garry", 2, 6, 3]]

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

res = branchAndBound(listaCandidatos, listaIdTareas)

for i in res:
    print(i)

