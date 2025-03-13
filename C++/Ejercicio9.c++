//LEY OHM
#include <iostream>
#include <limits>
#include <iomanip>

double obtener_float(const std::string& mensaje) {
    double valor;
    while (true) {
        std::cout << mensaje;
        std::cin >> valor;

        // Validar la entrada
        if (std::cin.fail() || valor < 0) {
            std::cin.clear(); // Limpiar el estado de error
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignorar la entrada incorrecta
            std::cout << "El valor no puede ser negativo. Inténtalo de nuevo." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer
            return valor;
        }
    }
}

void calcularLeyOhm() {
    std::cout << "Calculadora de la Ley de Ohm" << std::endl;
    
    while (true) {
        std::cout << "\nSelecciona la variable que deseas calcular:" << std::endl;
        std::cout << "1. Voltaje (V)" << std::endl;
        std::cout << "2. Corriente (I)" << std::endl;
        std::cout << "3. Resistencia (R)" << std::endl;
        std::cout << "4. Salir" << std::endl;

        std::string opcion;
        std::cout << "Ingresa el número de la opción (1, 2, 3 o 4): ";
        std::getline(std::cin, opcion);

        if (opcion == "1") {
            double I = obtener_float("Ingresa la corriente (I) en amperios: ");
            double R = obtener_float("Ingresa la resistencia (R) en ohmios: ");
            double V = I * R;
            std::cout << "El voltaje (V) es: " << std::fixed << std::setprecision(2) << V << " voltios" << std::endl;

        } else if (opcion == "2") {
            double V = obtener_float("Ingresa el voltaje (V) en voltios: ");
            double R = obtener_float("Ingresa la resistencia (R) en ohmios: ");
            double I = V / R;
            std::cout << "La corriente (I) es: " << std::fixed << std::setprecision(2) << I << " amperios" << std::endl;

        } else if (opcion == "3") {
            double V = obtener_float("Ingresa el voltaje (V) en voltios: ");
            double I = obtener_float("Ingresa la corriente (I) en amperios: ");
            double R = V / I;
            std::cout << "La resistencia (R) es: " << std::fixed << std::setprecision(2) << R << " ohmios" << std::endl;

        } else if (opcion == "4") {
            std::cout << "Gracias por usar la calculadora de la Ley de Ohm. ¡Hasta luego!" << std::endl;
            break;

        } else {
            std::cout << "Opción no válida. Por favor, selecciona 1, 2, 3 o 4." << std::endl;
        }
    }
}

int main() {
    calcularLeyOhm();
    return 0;
}