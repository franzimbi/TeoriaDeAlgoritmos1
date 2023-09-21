import time
tareas = ["Cocinar", "Primeros auxilios",
          "Meteorología", "astronomía", "Electricidad", "Mecanico", "Programador"]
candidatos = [["R.J. MacReady", 1, 5, 6], ["Nauls", 1, 2], ["Childs", 3, 7],
              ["Dr. Copper", 2, 4], ["George Bennings", 1, 3], ["Garry", 2, 6, 3]]

#[ childs, cooper, macready]
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

inicio = time.time()

print(branchAndBound(candidatos, tareas))

fin = time.time()
tiempo_transcurrido = (fin - inicio)*1000
print("Tiempo de ejecución: {:.6f} milisegundos".format(tiempo_transcurrido))