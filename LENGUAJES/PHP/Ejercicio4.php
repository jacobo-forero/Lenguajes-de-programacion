<?php
//CICLO FOR

function obtenerFloat($mensaje) {
    while (true) {
        echo $mensaje;
        $input = trim(fgets(STDIN));
        
        if (is_numeric($input) && $input >= 0) {
            return floatval($input);
        } else {
            echo "Error, por favor ingrese un número válido y positivo.\n";
        }
    }
}

function obtenerInt($mensaje) {
    while (true) {
        echo $mensaje;
        $input = trim(fgets(STDIN));
        
        if (is_numeric($input) && intval($input) == $input && $input >= 0) {
            return intval($input);
        } else {
            echo "Error, por favor ingrese un número entero positivo.\n";
        }
    }
}

function inversion() {
    $cant = obtenerFloat("Ingrese la cantidad a invertir: $");
    $inter = obtenerFloat("Ingrese el interés anual (en %): ");
    $años = obtenerInt("Ingrese el número de años: ");
    
    echo "\nResumen de la inversión:\n";
    for ($i = 1; $i <= $años; $i++) {
        $cant += $cant * ($inter / 100);
        echo "Año $i: Capital obtenido será: $" . number_format($cant, 2) . "\n";
    }
}
inversion();
?>