//OPERACIONES
#include <iostream>
#include <limits>
#include <cmath>

double suma(double num1, double num2) {
    return num1 + num2;
}

double resta(double num1, double num2) {
    return num1 - num2;
}

double multiplicacion(double num1, double num2) {
    return num1 * num2;
}

std::string division(double num1, double num2) {
    if (num2 != 0) {
        return std::to_string(num1 / num2);
    } else {
        return "No se puede dividir entre cero";
    }
}

double potencia(double num1, double num2) {
    return std::pow(num1, num2);
}

int main() {
    while (true) {
        std::cout << "\nCalculadora" << std::endl;
        std::cout << "1. Suma" << std::endl;
        std::cout << "2. Resta" << std::endl;
        std::cout << "3. Multiplicación" << std::endl;
        std::cout << "4. División" << std::endl;
        std::cout << "5. Potencia" << std::endl;
        std::cout << "6. Salir" << std::endl;

        int opcion;
        std::cout << "Selecciona una opción (1-6): ";
        std::cin >> opcion;

        if (opcion == 6) {
            std::cout << "Gracias por usar la calculadora. ¡Hasta luego!" << std::endl;
            break;
        }

        double num1, num2;
        std::cout << "Ingresa el primer número: ";
        std::cin >> num1;
        std::cout << "Ingresa el segundo número: ";
        std::cin >> num2;

        switch (opcion) {
            case 1:
                std::cout << "Resultado de la suma: " << suma(num1, num2) << std::endl;
                break;
            case 2:
                std::cout << "Resultado de la resta: " << resta(num1, num2) << std::endl;
                break;
            case 3:
                std::cout << "Resultado de la multiplicación: " << multiplicacion(num1, num2) << std::endl;
                break;
            case 4:
                std::cout << "Resultado de la división: " << division(num1, num2) << std::endl;
                break;
            case 5:
                std::cout << "Resultado de la potencia: " << potencia(num1, num2) << std::endl;
                break;
            default:
                std::cout << "Opción no válida. Por favor, selecciona una opción del 1 al 6." << std::endl;
                break;
        }
    }
    return 0;
}