// OCTAVOS DE FINAL
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

std::string simular_partido(const std::string& equipo1, const std::string& equipo2) {
    // Simula un partido entre dos equipos y devuelve el ganador.
    return (rand() % 2 == 0) ? equipo1 : equipo2;
}

std::vector<std::string> octavos_de_final(const std::vector<std::string>& equipos) {
    // Simula los octavos de final con los equipos dados.
    std::cout << "Octavos de Final:" << std::endl;
    std::vector<std::string> ganadores;

    // Asegurarse de que hay un número par de equipos
    if (equipos.size() % 2 != 0) {
        std::cout << "El número de equipos debe ser par." << std::endl;
        return ganadores;
    }

    for (size_t i = 0; i < equipos.size(); i += 2) {
        std::string equipo1 = equipos[i];
        std::string equipo2 = equipos[i + 1];
        std::string ganador = simular_partido(equipo1, equipo2);
        ganadores.push_back(ganador);
        std::cout << "Partido: " << equipo1 << " vs " << equipo2 << " - Ganador: " << ganador << std::endl;
    }

    return ganadores;
}

int main() {
    std::srand(static_cast<unsigned int>(std::time(0))); // Inicializar la semilla para rand

    // Definimos los equipos que participan en los octavos de final
    std::vector<std::string> equipos = {
        "FC Barcelona",
        "Real Madrid",
        "Arsenal",
        "Manchester City",
        "Chelsea",
        "Liverpool",
        "PSG",
        "Benfica"
    };

    // Simular los octavos de final
    std::vector<std::string> ganadores = octavos_de_final(equipos);

    std::cout << "\nEquipos que avanzan a los cuartos de final:" << std::endl;
    for (const auto& ganador : ganadores) {
        std::cout << ganador << std::endl;
    }

    return 0;
}