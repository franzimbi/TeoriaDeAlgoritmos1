import sys

def valorCaballero(caballero):
    return caballero[1]
def nombreCaballero(caballero):
    return caballero[0]
def encontrarElUltimoNegativo(caballeros):
    ultimo = -1
    for i in range(len(caballeros)):
        if valorCaballero(caballeros[i]) < 0:
            ultimo = i
    return ultimo

def encontrarMaximo(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] >= arr[max]:
            max = i
    return max

def construirCamino(optimos, caballeros):
    resultado = []
    pos = encontrarMaximo(optimos)
    while pos > 0 and optimos[pos-1] >= 0:
        resultado.append(caballeros[pos-1][0])
        pos -= 1
    return resultado

def caballerosMasPopulares(caballeros):
    ultimoNegativo = encontrarElUltimoNegativo(caballeros)
    caballerosReordenados = []
    if ultimoNegativo != -1:
        caballerosReordenados.extend(caballeros[ultimoNegativo+1:])
        caballerosReordenados.extend(caballeros[:ultimoNegativo])
    else:
        caballerosReordenados = caballeros
    optimos = []
    optimos.append(0)
    for i in range(len(caballerosReordenados)):
        valor = valorCaballero(caballerosReordenados[i])
        if optimos[i] + valor >= valor:
            optimos.append(optimos[i] + valor)
        else:
            optimos.append(valor)
    return construirCamino(optimos, caballerosReordenados)[::-1]

# ___ MAIN ___
argumentos = sys.argv
if len(argumentos) != 2:
    print("ERROR")
    sys.exit()

with open(argumentos[1], 'r') as archivo:
    lineas = archivo.readlines()

listaCaballeros = []
for l in lineas:
    elementos = l.strip().split(',')
    listaCaballeros.append([elementos[0], int(elementos[1])])

print(caballerosMasPopulares(listaCaballeros))
