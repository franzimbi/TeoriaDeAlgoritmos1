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
        _, aux = mergesortContador(c,0, len(c)-1, categorias)
        if aux >= cantidadInversiones:
            nombreComplemento = nombreActual
            cantidadInversiones = aux
    return nombreCapitan +',' + nombreComplemento

def mergesortContador(arr, ini, fin, dic):
    if ini >= fin:
        return (arr[ini], 0)

    mitad = (ini+fin) // 2
    ladoIzq, contIzq = mergesortContador(arr, ini, mitad, dic)
    ladoDer, contDer = mergesortContador(arr, mitad+1, fin, dic)
    res, contRes = merge(arr, ini, mitad, fin, dic)
    return (res, contRes + contIzq + contDer)

def merge(arr, ini, mitad, fin, dic):
    res = []
    contador = 0
    i, d = 0, mitad + 1
    while i <= mitad and d <= fin:
        if dic[arr[i]] <= dic[arr[d]]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[d])
            contador += mitad - i + 1
            d += 1
    while i <= mitad:
        res.append(arr[i])
        i += 1
    while d <= fin:
        res.append(arr[d])
        d += 1
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
capitan = lista.pop(int(argumentos[2]) - 1)
print(parejaInversiones(capitan, lista))