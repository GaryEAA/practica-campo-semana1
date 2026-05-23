# ==============================================================================
# EJERCICIO 5: DICCIONARIOS
# Asignado a: Adrian Ruesta
# ==============================================================================
#Crear un diccionario con la información de un trabajador
#Registro de trabajador
nombre = input("Ingrese el nombre del trabajador: ")
edad = input("Ingrese edad del trabajador: ")
área = input("Ingrese el área del trabajador: ")
sueldo = input("Ingrese el sueldo del trabajador: ")

TRABAJADOR={"Nombre": nombre,"Edad":edad,"Área": área,"Sueldo": sueldo}

#Mostrar todos los datos ingresados
print("=== DATOS DEL TRABAJADOR ===")

for clave, valor in TRABAJADOR.items():
    print(clave, ":", valor)

#Bucle

while True:

 Respuesta1 = input("\n¿Desea editar o agregar datos? (Si/No): ")

 if Respuesta1 == "No":
        print("\nPrograma finalizado")
        break

#Modificar el sueldo

 elif Respuesta1 == "Si":

        print("\n" * 3)

        Respuesta2 = input("Digite la operación a realizar (Editar/Agregar): ")

        if Respuesta2 == "Editar":

         dato = input("¿Qué dato desea editar? ")

         if dato in TRABAJADOR:

            nuevo_valor = input("Ingrese el nuevo valor: ")

            TRABAJADOR[dato] = nuevo_valor

            print("\n=== DATOS ACTUALIZADOS ===")

            for clave, valor in TRABAJADOR.items():
                print(clave, ":", valor)

         else:
          print("Ese dato no existe")

# Agregar el campo “Correo”

        elif Respuesta2 == "Agregar":

         clave_agregada = input("Ingrese el nombre del nuevo dato: ")
         valor_agregado = input("Ingrese el valor del nuevo dato: ")

         TRABAJADOR[clave_agregada] = valor_agregado

         print("\nDato agregado correctamente")

         for clave, valor in TRABAJADOR.items():
          print(clave, ":", valor)

        else: pass
