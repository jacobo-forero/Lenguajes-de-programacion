#include <mysql_driver.h>
#include <mysql_connection.h>
#include <iostream>

int main() {
    try {
        sql::mysql::MySQL_Driver *driver;
        sql::Connection *conn;

        driver = sql::mysql::get_mysql_driver_instance();
        conn = driver->connect("tcp://localhost:3306", "root", "");

        std::cout << "Conexión exitosa" << std::endl;

        delete conn; // Cerrar la conexión
    } catch (sql::SQLException &e) {
        std::cerr << "Error de conexión: " << e.what() << std::endl;
    }
    return 0;
}