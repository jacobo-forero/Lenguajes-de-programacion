// Bucles for

#include <iostream>
#include <string>

void mostrar_palabra() {
    std::string palabra;
    
    // Solicitar al usuario que ingrese una palabra
    std::cout << "Ingrese la palabra que quiere que se repita: ";
    std::getline(std::cin, palabra);
    
    // Validar que la palabra no esté vacía
    while (palabra.empty()) {
        std::cout << "La entrada no puede estar vacía. Inténtalo de nuevo." << std::endl;
        std::cout << "Ingrese la palabra que quiere que se repita: ";
        std::getline(std::cin, palabra);
    }
    
    int repeticiones;
    // Solicitar al usuario cuántas veces quiere que se repita la palabra
    while (true) {
        std::cout << "¿Cuántas veces quiere que se repita la palabra? ";
        std::cin >> repeticiones;
        
        if (repeticiones <= 0) {
            std::cout << "Por favor, ingrese un número positivo." << std::endl;
        } else {
            break;
        }
    }
    
    // Imprimir la palabra la cantidad de veces especificada
    for (int i = 0; i < repeticiones; ++i) {
        std::cout << palabra << std::endl;
    }
}

int main() {
    mostrar_palabra();
    return 0;
}