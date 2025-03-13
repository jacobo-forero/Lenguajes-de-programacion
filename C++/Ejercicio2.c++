// BUCLES WHILE

#include <iostream>
#include <limits>

int obtener_numero() {
    int num;
    while (true) {
        std::cout << "Ingrese un número para conocer la tabla de multiplicar: ";
        std::cin >> num;

        // Validar la entrada
        if (std::cin.fail()) {
            std::cin.clear(); // Limpiar el estado de error
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignorar la entrada incorrecta
            std::cout << "Error, por favor ingrese un número entero." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer
            return num;
        }
    }
}

void mostrar_tabla(int num) {
    std::cout << "\nTabla de multiplicar del " << num << ":" << std::endl;
    for (int i = 1; i <= 10; ++i) {
        std::cout << num << " x " << i << " = " << num * i << std::endl;
    }
}

int main() {
    while (true) {
        int numero = obtener_numero();
        mostrar_tabla(numero);
        
        char continuar;
        std::cout << "\n¿Desea calcular otra tabla? (s/n): ";
        std::cin >> continuar;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer

        if (continuar != 's' && continuar != 'S') {
            std::cout << "Gracias por usar el programa. ¡Hasta luego!" << std::endl;
            break;
        }
    }
    return 0;
}