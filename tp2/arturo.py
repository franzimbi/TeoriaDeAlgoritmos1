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
    for i in range(pos, -1, -1):



def caballerosMasPopulares(caballeros):
    ultimoNegativo = encontrarElUltimoNegativo(caballeros)
    caballerosReordenados = []
    if ultimoNegativo != -1:
        caballerosReordenados.extend(caballeros[ultimoNegativo:])
        caballerosReordenados.extend(caballeros[:ultimoNegativo])
    else:
        caballerosReordenados = caballeros
    optimos = []
    optimos.append(0)
    for i in range(len(caballerosReordenados)-1):
        valor = valorCaballero(caballerosReordenados[i])
        if optimos[i] + valor >= valor:
            optimos.append(optimos[i] + valor)
        else:
            optimos.append(valor)
    return construirCamino(optimos, caballerosReordenados)



