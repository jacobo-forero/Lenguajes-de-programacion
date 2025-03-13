//TABLA DE LA VERDAD
#include <iostream>
#include <vector>
#include <iomanip>

void generar_combinaciones(std::vector<std::vector<bool>>& combinaciones, int n) {
    int total = 1 << n; // 2^n combinaciones
    for (int i = 0; i < total; ++i) {
        std::vector<bool> combinacion;
        for (int j = 0; j < n; ++j) {
            combinacion.push_back((i & (1 << (n - j - 1))) != 0);
        }
        combinaciones.push_back(combinacion);
    }
}

void imprimir_tabla_verdad(const std::vector<std::string>& variables) {
    std::vector<std::vector<bool>> combinaciones;
    generar_combinaciones(combinaciones, variables.size());

    // Imprimimos la cabecera de la tabla
    for (const auto& var : variables) {
        std::cout << var << " | ";
    }
    std::cout << "A y B" << std::endl;
    std::cout << std::string(variables.size() * 4 + 10, '-') << std::endl; // Ajusta el ancho de la línea

    // Evaluamos la expresión para cada combinación
    for (const auto& combinacion : combinaciones) {
        bool resultado = true; // A y B
        for (bool valor : combinacion) {
            std::cout << (valor ? "1" : "0") << " | "; // Imprimir 1 para true y 0 para false
            resultado = resultado && valor; // A y B
        }
        std::cout << (resultado ? "1" : "0") << std::endl; // Imprimir resultado
    }
}

int main() {
    // Definimos las variables
    std::vector<std::string> variables = {"A", "B"};
    imprimir_tabla_verdad(variables);
    return 0;
}