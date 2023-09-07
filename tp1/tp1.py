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


def _menorCantidadExpedicionarios(candidatos, tareas, puestosCubiertos, mejorSolucion, actual, cantidadTareas):
    if len(mejorSolucion) <= actual:
        return False
    if len(puestosCubiertos) == cantidadTareas:
        return actual

    for t in tareas[0]:
        if t not in puestosCubiertos:
            actual.add(candidatos[0])
            for t in tareas[0]:
                puestosCubiertos.add(t) [1, 5]
            if _menorCantidadExpedicionarios(candidatos[1:], tareas[1:], mejorSolucion, actual, cantidadTareas) == False:







def menorCantidadExpedicionarios(candidatos, tareas):
    lista = sorted(candidatos, key=len, reverse=True)
    puestosCubiertos = set()
    mejorSolucionActual = set()
    candidatosOrdenados = []
    tareasOrdenadas = []
    for l in lista:
        candidatosOrdenados.append(l[0])
        tareasOrdenadas.append(l[1:])
    for t in range(len(tareasOrdenadas)):
        for j in tareasOrdenadas[t]:
            if j not in puestosCubiertos:
                puestosCubiertos.add(j)
                mejorSolucionActual.add(candidatosOrdenados[t])
    tam = len(puestosCubiertos)
    puestosCubiertos = set()
    return _menorCantidadExpedicionarios(candidatosOrdenados, tareasOrdenadas, puestosCubiertos, mejorSolucionActual,[], tam)

menorCantidadExpedicionarios(candidatos, tareas)
