#LISTAS

def mostrar(materias):
    if materias:
        print(f"Yo estudio {len(materias)} materias.")
        print("Las materias son:")
        for materia in materias:
            print(f"- {materia}")
    else:
        print("No hay materias para mostrar.")

def agregar_materia(materias):
    nueva_materia = input("Ingresa el nombre de la nueva materia: ").strip()
    if nueva_materia:
        materias.append(nueva_materia)
        print(f"La materia '{nueva_materia}' ha sido agregada.")
    else:
        print("El nombre de la materia no puede estar vacío.")

def main():
    lista = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    mostrar(lista)

    while True:
        continuar = input("¿Deseas agregar una nueva materia? (s/n): ").strip().lower()
        if continuar == 's':
            agregar_materia(lista)
            mostrar(lista)
        elif continuar == 'n':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa 's' o 'n'.")
main()