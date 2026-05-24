# ==============================================================================
# EJERCICIO 7: BÚSQUEDA LINEAL
# Asignado a: Alvaro Oré
# ==============================================================================

def main():
    print("--- EJERCICIO 7: BÚSQUEDA LINEAL ---")
    import random

# 1. Generar una lista de 10 números aleatorios del 1 al 20
lista = random.sample(range(1, 21), 10)
print(f"Lista generada: {lista}")

# 2. Solicitar un número a buscar
numero_buscado = int(input("Ingresa el número que quieres buscar: "))

# 3. Búsqueda lineal: recorrer elemento por elemento
encontrado = False
posicion = -1

for i in range(len(lista)):
    if lista[i] == numero_buscado:
        encontrado = True
        posicion = i # Guardamos la posición
        break # Salimos del bucle apenas lo encontramos


# 4. Mostrar resultados según los requisitos
if encontrado:
    print(f"¡Número encontrado!")
    print(f"El número {numero_buscado} está en la posición {posicion}")
else:
    print(f"El número {numero_buscado} no existe en la lista.")
    
    
if __name__ == "__main__":
    main()
    