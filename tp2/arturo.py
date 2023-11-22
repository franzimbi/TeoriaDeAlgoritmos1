import sys

def valorCaballero(caballero):
    return caballero[1]
def nombreCaballero(caballero):
    return caballero[0]
def caballerosNegativos(caballeros):
    aux = []
    for i in caballeros:
        aux.append((nombreCaballero(i), -1 * valorCaballero(i)))
    return aux
def encontrarMaximo(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] >= arr[max]:
            max = i
    return max

def construirCamino(optimos, caballeros):
    resultado = set()
    pos = encontrarMaximo(optimos)
    max = optimos[pos]
    while pos >= 0 and max != 0:
        resultado.add(caballeros[pos][0])
        max -= caballeros[pos][1]
        pos -= 1
    return resultado

def kadaneAlgoritmo(caballeros):
    optimos = []
    optimos.append(valorCaballero(caballeros[0]))
    for i in range(1, len(caballeros)):
        valor = valorCaballero(caballeros[i])
        if optimos[i-1] + valor >= valor:
            optimos.append(optimos[i-1] + valor)
        else:
            optimos.append(valor)
    return optimos[encontrarMaximo(optimos)], construirCamino(optimos,caballeros)
def caballerosMasPopulares(caballeros):
    caballerosSet = set()
    total = 0
    for i in caballeros:
        caballerosSet.add(nombreCaballero(i))
        total += valorCaballero(i)
    listaCaballerosNegativos = caballerosNegativos(caballeros)
    max, solMax =  kadaneAlgoritmo(caballeros)
    min, solMin = kadaneAlgoritmo(listaCaballerosNegativos)
    min = total + min
    if max > min:
        return solMax
    else:
        return caballerosSet - solMin


# ___ MAIN ___
argumentos = sys.argv
# if len(argumentos) != 2:
#     print("ERROR")
#     sys.exit()

with open('caballeros.txt', 'r') as archivo:
    lineas = archivo.readlines()

listaCaballeros = []
for l in lineas:
    elementos = l.strip().split(',')
    listaCaballeros.append([elementos[0], int(elementos[1])])

aux = caballerosMasPopulares(listaCaballeros)
if len(aux) == 0:
    print("No lleva a nadie")
else:
    print(aux)
