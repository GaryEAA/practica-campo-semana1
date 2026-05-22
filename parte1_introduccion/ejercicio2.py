# ==============================================================================
# EJERCICIO 2: PROMEDIO DE NOTAS
# Asignado a: Jadhe Sotelo
# ==============================================================================

def main():
    print("--- EJERCICIO 1: OPERACIONES BÁSICAS ---")
    # TODO: Desarrolla tu código aquí

# Programa para calcular el promedio de 4 notas de un estudiante

# Entrada de datos
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))

# Cálculo del promedio
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Mostrar resultado
print("\nPromedio final:", promedio)

# Condición para determinar si aprueba o desaprueba
if promedio >= 11:
    print("Condición: Aprobado")
else:
    print("Condición: Desaprobado")

if __name__ == "__main__":
    main()