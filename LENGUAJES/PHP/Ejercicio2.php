<?php
// BUCLES WHILE
function obtenerNumero() {
    while (true) {
        echo "Ingrese un número para conocer la tabla de multiplicar: ";
        $input = trim(fgets(STDIN));
        
        // Validar que la entrada sea un número entero
        if (is_numeric($input) && intval($input) == $input) {
            return intval($input);
        } else {
            echo "Error, por favor ingrese un número entero.\n";
        }
    }
}

function mostrarTabla($num) {
    echo "\nTabla de multiplicar del $num:\n";
    for ($i = 1; $i <= 10; $i++) {
        echo "$num x $i = " . ($num * $i) . "\n";
    }
}

function main() {
    while (true) {
        $numero = obtenerNumero();
        mostrarTabla($numero);
        
        echo "\n¿Desea calcular otra tabla? (s/n): ";
        $continuar = trim(fgets(STDIN));
        
        if (strtolower($continuar) !== 's') {
            echo "Gracias por usar el programa. ¡Hasta luego!\n";
            break;
        }
    }
}
main();
?>