# ==============================================================================
# EJERCICIO 9: NÚMERO MAYOR SIN UTILIZAR MAX()
# Asignado a: Alvaro Oré
# ==============================================================================

def main():
    print("--- EJERCICIO 9: NÚMERO MAYOR SIN UTILIZAR MAX() ---")
  # Crear una lista de números. Puedes pedirla al usuario o ponerla fija
lista = [15, 3, 27, 8, 19, 4, 31, 12, 9, 22]
print(f"Lista: {lista}")
print("-" * 30)

# Asumimos que el primer número es el mayor inicialmente
numero_mayor = lista[0]
print(f"Paso 0: Empezamos asumiendo que el mayor es {numero_mayor}")

# Recorremos la lista desde el segundo elemento usando fuerza bruta
for i in range(1, len(lista)):
    numero_actual = lista[i]
    print(f"Paso {i}: Comparando {numero_mayor} con {numero_actual}...")
    
    # Comparación manual
    if numero_actual > numero_mayor:
        print(f" -> {numero_actual} es mayor. Actualizamos el mayor.")
        numero_mayor = numero_actual
    else:
        print(f" -> {numero_mayor} sigue siendo el mayor.")

print("-" * 30)
print(f"El número mayor de la lista es: {numero_mayor}")
    
if __name__ == "__main__":
    main()
