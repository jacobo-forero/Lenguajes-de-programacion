// CICLO FOR

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
            std::cout << "El valor debe ser un número positivo. Inténtalo de nuevo." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer
            return valor;
        }
    }
}

int obtener_int(const std::string& mensaje) {
    int valor;
    while (true) {
        std::cout << mensaje;
        std::cin >> valor;

        // Validar la entrada
        if (std::cin.fail() || valor < 0) {
            std::cin.clear(); // Limpiar el estado de error
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignorar la entrada incorrecta
            std::cout << "El valor debe ser un número entero positivo. Inténtalo de nuevo." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer
            return valor;
        }
    }
}

void inversion() {
    double cant = obtener_float("Ingrese la cantidad a invertir: $");
    double inter = obtener_float("Ingrese el interés anual (en %): ");
    int años = obtener_int("Ingrese el número de años: ");
    
    std::cout << "\nResumen de la inversión:" << std::endl;
    for (int i = 1; i <= años; ++i) {
        cant += cant * (inter / 100);
        std::cout << "Año " << i << ": Capital obtenido será: $" << std::fixed << std::setprecision(2) << cant << std::endl;
    }
}

int main() {
    inversion();
    return 0;
}