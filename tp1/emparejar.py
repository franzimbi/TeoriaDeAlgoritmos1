import sys
#   Se está por realizar un concurso de conocimientos en parejas para escuelas secundarias.
#   Existen “n” categorías que se evaluarán en el mismo. Una escuela evaluó a sus posibles
#   participantes. Por cada uno de ellos generaron una lista ordenada de mayor a menor de
#   las categorías según sus conocimientos. En base a una competencia interna se seleccionó
#   a uno de ellos como el capitán. Nos solicitan que los ayudemos, basándonos en el concepto
#   de inversión, a seleccionar a otro participante que mejor se complemente con el capitán.
def parejaInversiones(capitan, candidatos):
    categorias = {}
    nombreCapitan = capitan.pop(0)
    nombreComplemento = ''
    cantidadInversiones = 0
    for i in range(len(capitan)):
        categorias[capitan[i]] = i
    for c in candidatos:
        if c[0] == nombreCapitan:
            continue
        nombreActual = c[0]
        c.pop(0)
        _, aux = mergesortContador(c, categorias)
        if aux >= cantidadInversiones:
            nombreComplemento = nombreActual
            cantidadInversiones = aux
    return nombreCapitan +',' + nombreComplemento

def mergesortContador(arr, dic):
    if len(arr) <= 1:
        return (arr, 0)

    mitad = len(arr) // 2
    ladoIzq, contIzq = mergesortContador(arr[:mitad], dic)
    ladoDer, contDer = mergesortContador(arr[mitad:], dic)
    res, contRes = merge(ladoIzq, ladoDer, dic)
    return (res, contRes + contIzq + contDer)

def merge(izq, der, dic):
    res = []
    contador = 0
    i, d = 0, 0
    while i < len(izq) and d < len(der):
        if dic[izq[i]] <= dic[der[d]]:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[d])
            contador += len(izq) - i
            d += 1
    res.extend(izq[i:])
    res.extend(der[d:])
    return res, contador

#   ~~ main ~~
argumentos = sys.argv
if len(argumentos) != 3:
    print("ERROR")
    sys.exit()

with open(argumentos[1], 'r') as archivo:
    lineas = archivo.readlines()
lista = []

for l in lineas:
    elementos = l.strip().split(',')
    elementos = [elementos[0]] + [int(elemento) for elemento in elementos[1:]]
    lista.append(elementos)

if int(argumentos[2]) - 2 > len(argumentos) or int(argumentos[2]) - 1 < 0 :
    print("ERROR")
    sys.exit()
capitan = lista.pop(int(argumentos[2]) - 1 )
print(parejaInversiones(capitan, lista))