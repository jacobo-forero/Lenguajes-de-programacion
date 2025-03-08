#OCTAVOS DE FINAL

import random

def simular_partido(equipo1, equipo2):
    #Simula un partido entre dos equipos y devuelve el ganador.
    resultado = random.choice([equipo1, equipo2])
    return resultado

def octavos_de_final(equipos):
    #Simula los octavos de final con los equipos dados.
    print("Octavos de Final:")
    ganadores = []

    # Asegurarse de que hay un número par de equipos
    if len(equipos) % 2 != 0:
        print("El número de equipos debe ser par.")
        return

    for i in range(0, len(equipos), 2):
        equipo1 = equipos[i]
        equipo2 = equipos[i + 1]
        ganador = simular_partido(equipo1, equipo2)
        ganadores.append(ganador)
        print(f"Partido: {equipo1} vs {equipo2} - Ganador: {ganador}")

    return ganadores

def main():
    # Definimos los equipos que participan en los octavos de final
    equipos = [
        "FC Barcelona",
        "Real Madrid",
        "Arsenal",
        "Manchester City",
        "Chelsea",
        "Liverpool",
        "PSG",
        "Benfica"
    ]

    # Simular los octavos de final
    ganadores = octavos_de_final(equipos)

    print("\nEquipos que avanzan a los cuartos de final:")
    for ganador in ganadores:
        print(ganador)

if __name__ == "__main__":
    main()