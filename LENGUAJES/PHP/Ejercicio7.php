<?php
// FUNCIONES

function obtenerNombre() {
    while (true) {
        echo "Ingrese su nombre: ";
        $nombre = trim(fgets(STDIN));
        
        if (!empty($nombre)) {
            return $nombre;
        } else {
            echo "El nombre no puede estar vacío. Inténtalo de nuevo.\n";
        }
    }
}

function saludo($nombre) {
    echo "Hola $nombre, bienvenido/a!\n";
}

function main() {
    while (true) {
        $nombre = obtenerNombre();
        saludo($nombre);
        
        echo "¿Deseas saludar a otra persona? (s/n): ";
        $continuar = trim(fgets(STDIN));
        
        if (strtolower($continuar) !== 's') {
            echo "Gracias por usar el programa. ¡Hasta luego!\n";
            break;
        }
    }
}
main();
?>