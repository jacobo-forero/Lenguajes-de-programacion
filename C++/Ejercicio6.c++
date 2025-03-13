// DICCIONARIO
#include <iostream>
#include <map>
#include <string>
#include <limits>

std::map<std::string, std::string> obtener_divisas() {
    return {
        {"Dollar", "$"},
        {"Euro", "€"},
        {"Yen", "¥"},
        {"Peso", "$"}
    };
}

void conversor() {
    std::map<std::string, std::string> divisas = obtener_divisas();
    
    while (true) {
        std::string divisa;
        std::cout << "Ingrese el tipo de divisa (o 'salir' para terminar): ";
        std::getline(std::cin, divisa);
        
        // Capitalizar la primera letra
        if (!divisa.empty()) {
            divisa[0] = toupper(divisa[0]);
        }

        if (divisa == "Salir") {
            std::cout << "Gracias por usar el conversor de divisas. ¡Hasta luego!" << std::endl;
            break;
        }
        
        if (divisas.find(divisa) != divisas.end()) {
            std::cout << "Esta es la divisa: " << divisas[divisa] << std::endl;
        } else {
            std::cout << "Divisa no encontrada. Por favor, intenta de nuevo." << std::endl;
        }
    }
}

int main() {
    conversor();
    return 0;
}