<?php
// BUCLES FOR

function mostrarPalabra() {
    // Solicitar al usuario que ingrese una palabra
    echo "Ingrese la palabra que quiere que se repita: ";
    $palabra = trim(fgets(STDIN));
    
    // Validar que la palabra no esté vacía
    while (empty($palabra)) {
        echo "La entrada no puede estar vacía. Inténtalo de nuevo.\n";
        echo "Ingrese la palabra que quiere que se repita: ";
        $palabra = trim(fgets(STDIN));
    }
    
    // Solicitar al usuario cuántas veces quiere que se repita la palabra
    do {
        echo "¿Cuántas veces quiere que se repita la palabra? ";
        $input = trim(fgets(STDIN));
        $repeticiones = intval($input);
        
        if ($repeticiones <= 0) {
            echo "Por favor, ingrese un número positivo.\n";
        }
    } while ($repeticiones <= 0);
    
    // Imprimir la palabra la cantidad de veces especificada
    for ($i = 0; $i < $repeticiones; $i++) {
        echo $palabra . "\n";
    }
}
mostrarPalabra();
?>