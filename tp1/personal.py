import time
tareas = ["Cocinar", "Primeros auxilios",
          "Meteorología", "astronomía", "Electricidad", "Mecanico", "Programador"]
candidatos = [["R.J. MacReady", 1, 5, 6], ["Nauls", 1, 2], ["Childs", 3, 7],
              ["Dr. Copper", 2, 4], ["George Bennings", 1, 3], ["Garry", 2, 6, 3]]

#[ childs, cooper, macready]

class PuestosCubiertos:
    def __init__(self, listaPuestos):
        self._puestos = {}
        self._tam = 0
        for i in listaPuestos:
            self._puestos[i] = 0

    def cubrirPuestos(self, puestos):
        for i in puestos:
            if i not in self._puestos:
                return False
            if self._puestos[i] == 0:
                self._tam +=1
            self._puestos[i] += 1
        return  True

    def liberarPuestos(self, puestos):
        for i in puestos:
            if i not in self._puestos:
                return False
            if self._puestos[i] == 0:
                continue
            self._puestos[i] -= 1
            if self._puestos[i] == 0:
                self._tam -=1
        return True

    def puestosCubiertos(self):
        aux = []
        for i in self._puestos:
            if self._puestos[i] > 0:
                aux.append(i)
        return aux

    def __len__(self):
        return self._tam

    def __str__(self):
        return str(self.puestosCubiertos())



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

    puestosCubiertos = set()
    mejorSolucion = []
    for i in candidatos:
        mejorSolucion.append(i[0])
    return  _bAb(0, candidatos, puestosCubiertos, [], mejorSolucion, len(puestos))

inicio = time.time()

print(branchAndBound(candidatos, tareas))

fin = time.time()
tiempo_transcurrido = (fin - inicio)*1000
print("Tiempo de ejecución: {:.6f} milisegundos".format(tiempo_transcurrido))