// CAJERO

#include <iostream>
#include <limits>

void mostrar_menu() {
    std::cout << "\nBienvenido al cajero" << std::endl;
    std::cout << "1. Ingresar dinero" << std::endl;
    std::cout << "2. Retirar dinero" << std::endl;
    std::cout << "3. Ver saldo" << std::endl;
    std::cout << "4. Salir" << std::endl;
}

double obtener_monto(const std::string& mensaje) {
    double monto;
    while (true) {
        std::cout << mensaje;
        std::cin >> monto;

        // Validar la entrada
        if (std::cin.fail() || monto < 0) {
            std::cin.clear(); // Limpiar el estado de error
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignorar la entrada incorrecta
            std::cout << "El monto debe ser un número positivo. Inténtalo de nuevo." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer
            return monto;
        }
    }
}

void cajero() {
    double saldo = 1000.0;
    while (true) {
        mostrar_menu();
        std::string opcion;
        std::cout << "¿Qué deseas hacer? ";
        std::getline(std::cin, opcion);
        
        if (opcion == "1") {
            double monto = obtener_monto("¿Cuánto dinero deseas ingresar? $");
            saldo += monto;
            std::cout << "Se ha ingresado $" << monto << " a tu cuenta. Tu saldo actual es $" << saldo << "." << std::endl;
        
        } else if (opcion == "2") {
            double monto = obtener_monto("¿Cuánto dinero deseas retirar? $");
            if (monto <= saldo) {
                saldo -= monto;
                std::cout << "Se ha retirado $" << monto << " de tu cuenta. Tu saldo actual es $" << saldo << "." << std::endl;
            } else {
                std::cout << "Error: No tienes suficiente saldo para realizar esta operación." << std::endl;
            }
        
        } else if (opcion == "3") {
            std::cout << "Tu saldo actual es $" << saldo << "." << std::endl;
        
        } else if (opcion == "4") {
            std::cout << "Gracias por utilizar el cajero." << std::endl;
            break;
        
        } else {
            std::cout << "Opción no válida. Por favor, intenta de nuevo." << std::endl;
        }
    }
}

int main() {
    cajero();
    return 0;
}