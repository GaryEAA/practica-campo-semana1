# ==============================================================================
# EJERCICIO 10: CIFRADO CÉSAR
# Asignado a: Gary Añanga
# ==============================================================================

def main():
    print("--- EJERCICIO 10: DESCIFRADO CÉSAR POR FUERZA BRUTA ---")
    
    # ingresar el mensaje cifrado (en mayúsculas)
    mensaje_cifrado = input("Ingresa el mensaje cifrado (en MAYÚSCULAS): ")
    
    print(f"\nIniciando ataque probando las 26 claves posibles...\n")
    print("-" * 50)
    
    # abecedario en mayúsculas para el cifrado César
    ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    
    # bucle para probar cada clave posible (0 a 25)
    for clave in range(26):
        mensaje_descifrado = ""
        
        # procesar cada letra del mensaje cifrado
        for letra in mensaje_cifrado:
            if letra in ALFABETO:
                # encontrar la posición actual de la letra en el alfabeto
                posicion_actual = ALFABETO.index(letra)
                
                # calcular la nueva posición restando la clave y usando módulo para envolver el alfabeto
                nueva_posicion = (posicion_actual - clave) % 26
                
                mensaje_descifrado += ALFABETO[nueva_posicion]
            else:
                # si el carácter no es una letra (como espacios o puntuación), se mantiene igual
                mensaje_descifrado += letra
                
        print(f"Clave {clave:02d} | Resultado: {mensaje_descifrado}")
        
    print("-" * 50)
    print("\nRevisa los resultados para encontrar el mensaje descifrado correcto.")

if __name__ == "__main__":
    main()