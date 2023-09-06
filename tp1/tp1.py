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


def _menorCantidadExpedicionarios(l, cubiertos, solucionActual):


def menorCantidadExpedicionarios(c, t):
    lista = sorted(c, key=len, reverse=True)
    puestosCubiertos = set()
    for i in range(len(tareas)):
        puestosCubiertos.add(i)
    mejorSolucionActual = []
    for i in lista:
        mejorSolucionActual.append(i[0])

    return _menorCantidadExpedicionarios(lista, puestosCubiertos, mejorSolucionActual):


menorCantidadExpedicionarios(candidatos, tareas)
