# ==============================================================================
# EJERCICIO 8: FUERZA BRUTA PARA CONTRASEÑAS
# Asignado a: Gary Añanga
# ==============================================================================

def main():
    print("--- EJERCICIO 8: FUERZA BRUTA PARA CONTRASEÑAS ---")
    # usuario ingresa contraseña correcta de 3 dígitos
    while True:
        contrasena_correcta = input("Ingrese la contraseña correcta de 3 dígitos: ")
        # validando que la contraseña sea un número de 3 dígitos
        if len(str(contrasena_correcta)) == 3 and str(contrasena_correcta).isdigit():
            break
        print("La contraseña debe ser un número de 3 dígitos. Intente nuevamente.")
    
    # iniciando ataque de fuerza bruta
    print("Iniciando ataque de fuerza bruta...")
    
    # contador de intentos
    intentos = 0
    
    # probando combinaciones por fuerza bruta desde 000 hasta 999
    for i in range(1000):
        intentos += 1
        # convirtiendo el número a una cadena de 3 dígitos
        combinacion_intento = str(i).zfill(3)
        # ver intentos en consola
        print(f"Probando... {combinacion_intento}")
        # comparando la combinación actual con la contraseña correcta
        if combinacion_intento == contrasena_correcta:
                    # si se encuentra la contraseña, se muestra un mensaje de éxito y la cantidad de intentos realizados
                    print(f"\n¡Contraseña descifrada con éxito!")
                    print(f"Contraseña encontrada: '{combinacion_intento}'")
                    print(f"Cantidad de intentos realizados: {intentos}")
                    break

if __name__ == "__main__":
    main()