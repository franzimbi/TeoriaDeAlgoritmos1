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

#[ childs, cooper, macready]

class PuestosCubiertos:
    def __init__(self, listaPuestos):
        self._puestos = {}
        for i in listaPuestos:
            self._puestos[i] = 0

    def cubrirPuestos(self, puestos):
        for i in puestos:
            if i not in self._puestos:
                return False
            self._puestos[i] += 1
        return  True

    def liberarPuestos(self, puestos):
        for i in puestos:
            if i not in self._puestos:
                return False
            if self._puestos[i] == 0:
                continue
            self._puestos[i] -= 1
        return True

    def puestosCubiertos(self):
        aux = []
        for i in self._puestos:
            if self._puestos[i] > 0:
                aux.append(i)
        return aux

    def __len__(self):
        tam = 0
        for i in self._puestos:
            if self._puestos[i] > 0:
                tam+= 1
        return tam

    def __str__(self):
        return str(self.puestosCubiertos())


    #https://docs.google.com/document/d/1wXAO5pavAgGTnVFEGN96WoUL4Mt--S38csLr9-YKiqg/edit
def _menorCantidadExpedicionarios(solucionActual, candidatos, puestosCubiertos, cantidadTareas):
    if len(puestosCubiertos) == cantidadTareas:
        return solucionActual
    if len(candidatos) == 0:
        return None

def ordenarPorAportes(candidatos):
    """devuelve una lista nueva con los candidatos de mayor a menor cantidad de trabajos q hacen.
    no toca la lista de candidatos original"""
    return sorted(candidatos, key=len, reverse=True)

def agregarCandidato(candidatos, puestosCubiertos, solucion):
    solucion.append(candidatos[0][0])
    for i in candidatos[0]:
        if i == candidatos[0][0]:
            continue
        puestosCubiertos.add(i)

def menorCantidadExpedicionarios(candidatos, tareas):
    copiaCandidatos = candidatos.copy()
    puestos = []
    mejorSolucionActual = []
    for i in range(1, len(tareas)+1):
        puestos.append(i)
    puestosCubiertos = PuestosCubiertos(puestos)
    for i in candidatos:
        mejorSolucionActual.append(i[0])
    return _menorCantidadExpedicionarios(mejorSolucionActual, copiaCandidatos, puestosCubiertos, len(tareas))

menorCantidadExpedicionarios(candidatos,tareas)