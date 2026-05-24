# ==============================================================================
# EJERCICIO 3: LISTAS
# Asignado a: Jadhe Sotelo
# ==============================================================================

def main():
    print("--- EJERCICIO 1: OPERACIONES BÁSICAS ---")
    # TODO: Desarrolla tu código aquí
    
# Programa que permite ingresar 8 números en una lista
# y muestra el mayor, menor y la suma total

# Crear lista vacía
numeros = []

# Ingreso de datos
for i in range(8):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Mostrar todos los elementos
print("\nLista de números ingresados:")
print(numeros)

# Mostrar número mayor
print("Número mayor:", max(numeros))

# Mostrar número menor
print("Número menor:", min(numeros))

# Calcular suma total
print("Suma total:", sum(numeros))

if __name__ == "__main__":
    main()