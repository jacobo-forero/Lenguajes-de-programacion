#Lista 'registros' 
registros = {
    1: {"nombre": "Ana", "edad": 25},
    2: {"nombre": "Luis", "edad": 30},
    3: {"nombre": "Carlos", "edad": 22},
}

#Función para buscar un registro por nombre
def consultar(nombre):
    return {id_: datos for id_, datos in registros.items() if datos["nombre"].lower() == nombre.lower()}

#Funcion para ordenar los registros
def ordenarPorClave(clave):
    return sorted(registros.items(), key=lambda x: x[1][clave])

#Ejemplo de uso de la función consultar (Se muestra en el terminal)
def anexarRegistro():
    idNuevo = int(input("Ingrese el ID: "))
    nombreNuevo = input("Ingrese el nombre: ")
    edadNueva = int(input("Ingrese la edad: "))
    registros[idNuevo] = {"nombre": nombreNuevo, "edad":  edadNueva}
    print("Registro agregado exitosamente.")

#Funcion para filtrar por la edad 
def filtrarPorEdad(edadMinima):
    return {id_: datos for id_, datos in registros.items() if datos["edad"] >= edadMinima}

#Funcion con bucle while para realizar las diferentes opciones
def menu():
    while True:
        #Bucle para mostrar el menu
        print("\n--- MENÚ ---")
        print("1. Consultar por nombre")
        print("2. Ordenar registros")
        print("3. Agregar nuevo regitro")
        print("4. Filtrar por edad")
        print("5. Mostrar registros")
        print("6. Salir")

        #Input para seleccionar la opción
        opcion = input("Seleccione una opción: ")

        #Opcion 1: Consultar por nombre
        if opcion == "1":
            nombre = input("Ingrese el nombre a consultar: ")
            print("Resultados", consultar(nombre))
            
        #Opcion  2: Ordenar registros y mostrarlos
        elif opcion == "2":
            clave = input("Ingrese la clave de ordenamineto (nombre, edad): ")
            print("Registros Ordenados:", filtrarPorEdad(edad))
            
        #Opcion 3: Agregar un nuevo registro
        elif opcion == "3":
            anexarRegistro()
            
        #Opcion 4: Filtrar por edad
        elif opcion == "4":
            edad = int(input("Ingrese la edad minima para filtrar: "))
            print("Registros filtrados:", filtrarPorEdad(edad))
            
        #Opcion 5: Mostrar registros
        elif opcion == "5":
         print("Lista completa de registros: ", registros)
         
        #Opcion 6: Salir del programa
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")    
menu()