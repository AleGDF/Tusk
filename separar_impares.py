from es_par import es_par

def separar_impares(pila):
    """Función que separa los números impares de la pila."""
    impares = []
    while pila:
        numero = pila.pop()
        if not es_par(numero):
            impares.append(numero)
    return impares