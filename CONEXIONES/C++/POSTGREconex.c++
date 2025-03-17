#include <iostream>
#include <pqxx/pqxx>

int main() {
    try {
        pqxx::connection C("user=postgres password=1234 host=localhost");
        if (C.is_open()) {
            std::cout << "Conexión exitosa" << std::endl;
        } else {
            std::cout << "No se pudo abrir la base de datos" << std::endl;
            return 1;
        }
        C.disconnect();
    } catch (const std::exception &e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }
    return 0;
}