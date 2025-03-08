#Lista 'registros' 
registros =[
    (1, "Ana", 25),
    (2, "Luis", 30),
    (3, "Carlos", 22)
]

#Función para buscar un registro por nombre
def consultar(nombre):
    return [registro for registro in registros if registro[1].lower() == nombre.lower()]

#Funcion para ordenar los registros
def ordenarPorClave(indice):
    return sorted(registros, key=lambda x: x[indice])

#Ejemplo de uso de la función consultar (Se muestra en el terminal)
def anexarRegistro():
    idNuevo = int(input("Ingrese el ID: "))
    nombreNuevo = input("Ingrese el nombre: ")
    edadNueva = int(input("Ingrese la edad: "))
    registros.append(idNuevo, nombreNuevo, edadNueva)
    print("Registro agregado exitosamente.")

#Funcion para filtrar por la edad minima
def filtrarPorEdad(edadMinima):
    return [registro for registro in registros if registro[2] >= edadMinima]

#Funcion para mostrar los registros
def menu():
    #Bucle para mostrar el menu
    while True:
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
            clave = input("Ingrese la clave de ordenamineto (id, nombre, edad): ").lower()
            indice = {"id": 0, "nombre": 1, "edad": 2}.get(clave, -1)
            if indice != -1:
                print("Registros ordenados:", ordenarPorClave(indice))
            else:
                print("Clave no valida. Intente nuevamente.")
                
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