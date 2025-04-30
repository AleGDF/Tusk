from es_par import es_par

def separar_pares(pila):
    """Función que separa los números pares de la pila."""
    pares = []
    while pila:
        numero = pila.pop()
        if es_par(numero):
            pares.append(numero)
    return pares