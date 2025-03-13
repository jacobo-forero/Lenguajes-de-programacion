//LISTAS
#include <iostream>
#include <vector>
#include <string>
#include <limits>

void mostrar(const std::vector<std::string>& materias) {
    if (!materias.empty()) {
        std::cout << "Yo estudio " << materias.size() << " materias." << std::endl;
        std::cout << "Las materias son:" << std::endl;
        for (const auto& materia : materias) {
            std::cout << "- " << materia << std::endl;
        }
    } else {
        std::cout << "No hay materias para mostrar." << std::endl;
    }
}

void agregar_materia(std::vector<std::string>& materias) {
    std::string nueva_materia;
    std::cout << "Ingresa el nombre de la nueva materia: ";
    std::getline(std::cin, nueva_materia);
    if (!nueva_materia.empty()) {
        materias.push_back(nueva_materia);
        std::cout << "La materia '" << nueva_materia << "' ha sido agregada." << std::endl;
    } else {
        std::cout << "El nombre de la materia no puede estar vacío." << std::endl;
    }
}

int main() {
    std::vector<std::string> lista = {"Matematicas", "Fisica", "Quimica", "Historia", "Lengua"};
    mostrar(lista);

    while (true) {
        std::string continuar;
        std::cout << "¿Deseas agregar una nueva materia? (s/n): ";
        std::getline(std::cin, continuar);
        if (continuar == "s") {
            agregar_materia(lista);
            mostrar(lista);
        } else if (continuar == "n") {
            std::cout << "Gracias por usar el programa. ¡Hasta luego!" << std::endl;
            break;
        } else {
            std::cout << "Opción no válida. Por favor, ingresa 's' o 'n'." << std::endl;
        }
    }
    return 0;
}