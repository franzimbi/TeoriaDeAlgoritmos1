# https://jamboard.google.com/d/1NkHMri_u8HTwly7UPNdU_GuMhs3_AFTz474NmIDRI9w/viewer?f=0

# Nos informan de la apertura de una nueva base de
# investigación antártica. En la misma se espera realizar una
# serie de experimentos. Por lo tanto, han comenzado una búsqueda
# de personal calificado. Se cuenta con un listado de “n” habilidades
# a cubrir por el personal
# (Ejemplo: “Cocinar”, “Primeros auxilios”, “Meteorología”, “astronomía”, “Electricidad”, etc).
# Además se ha reunido una cantidad de “m” candidatos. Cada candidato cubre un
# subconjunto de las habilidades.
# Nos solicitan que los ayudemos a resolver el problema intentando seleccionar
# a la menor cantidad de expedicionarios, sin dejar de cubrir los requerimientos. (Branch and Bound)


tareas = ["Cocinar", "Primeros auxilios",
          "Meteorología", "astronomía", "Electricidad", "Mecanico", "Programador"]
candidatos = [["R.J. MacReady", 1, 5, 6], ["Nauls", 1, 2], ["Childs", 3, 7],
              ["Dr. Copper", 2, 4], ["George Bennings", 1, 3], ["Garry", 2, 6, 3]]

[ childs, cooper, macready]

    #https://docs.google.com/document/d/1wXAO5pavAgGTnVFEGN96WoUL4Mt--S38csLr9-YKiqg/edit
def _menorCantidadExpedicionarios(solucionActual, candidatos, puestosCubiertos, cantidadTareas):
    if len(puestosCubiertos) == cantidadTareas:
        return solucionActual
    if len(candidatos) == 0:
        return None

    candidatos = ordenarPorAportes(candidatos, puestosCubiertos)
    agregarCandidato(candidatos, puestosCubiertos, solucionActual)
    return _menorCantidadExpedicionarios(solucionActual, candidatos[1:], puestosCubiertos, cantidadTareas)

def ordenarPorAportes(candidatos, puestosCubiertos):
    """devuelve una lista nueva con los candidatos reordenados segun los puestos que faltan cubrir.
    no toca la lista de candidatos ni los puestos cubiertos"""
    nuevosCandidatos = []
    for c in candidatos: #O(n) n: cantidad de candidatos
        aux = []
        for t in c:
            if t not in puestosCubiertos:
                aux.append(t)
        if len(aux) > 1:
            nuevosCandidatos.append(aux)
    return sorted(nuevosCandidatos, key=len, reverse=True)

def agregarCandidato(candidatos, puestosCubiertos, solucion):
    solucion.append(candidatos[0][0])
    for i in candidatos[0]:
        if i == candidatos[0][0]:
            continue
        puestosCubiertos.add(i)

def menorCantidadExpedicionarios(candidatos, tareas):
    copiaCandidatos = candidatos.copy()
    puestosCubiertos = set()
    mejorSolucionActual = []
    return _menorCantidadExpedicionarios(mejorSolucionActual, copiaCandidatos, puestosCubiertos, len(tareas))


print(menorCantidadExpedicionarios(candidatos, tareas))