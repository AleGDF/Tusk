from separar_pares import separar_pares
from separar_impares import separar_impares

def separarParImpar(pila):
    """Función principal que separa pares e impares en la pila."""
    # Usamos una copia de la pila para no modificar la original
    pila_original = pila.copy()
    
    pares = separar_pares(pila_original)  # Separar pares
    pila_original = pila.copy()  # Volver a copiar la pila original
    impares = separar_impares(pila_original)  # Separar impares
    
    # Limpiar la pila original
    pila.clear()
    
    # Combinar pares e impares
    # Primero agregamos los pares
    for par in pares:
        pila.append(par)
    # Luego agregamos los impares
    for impar in impares:
        pila.append(impar)
    
    return pila