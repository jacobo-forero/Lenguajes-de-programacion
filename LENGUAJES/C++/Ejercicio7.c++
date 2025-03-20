//FUNCIONES
#include <iostream>
#include <string>
#include <limits>

std::string obtener_nombre() {
    std::string nombre;
    while (true) {
        std::cout << "Ingrese su nombre: ";
        std::getline(std::cin, nombre);
        if (!nombre.empty()) {
            return nombre;
        } else {
            std::cout << "El nombre no puede estar vacío. Inténtalo de nuevo." << std::endl;
        }
    }
}

void saludo(const std::string& nombre) {
    std::cout << "Hola " << nombre << ", bienvenido/a!" << std::endl;
}

int main() {
    while (true) {
        std::string nombre = obtener_nombre();
        saludo(nombre);
        
        std::string continuar;
        std::cout << "¿Deseas saludar a otra persona? (s/n): ";
        std::getline(std::cin, continuar);
        
        if (continuar != "s" && continuar != "S") {
            std::cout << "Gracias por usar el programa. ¡Hasta luego!" << std::endl;
            break;
        }
    }
    return 0;
}