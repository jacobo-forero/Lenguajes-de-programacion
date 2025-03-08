<?php
//CONDICIONALES

function obtenerEdad() {
    while (true) {
        echo "Ingresa tu edad: ";
        $input = trim(fgets(STDIN));
        
        if (is_numeric($input) && intval($input) == $input && $input >= 0) {
            return intval($input);
        } else {
            echo "Error, por favor ingresa un número entero válido y no negativo.\n";
        }
    }
}

function mayoriaEdad() {
    $edad = obtenerEdad();
    
    if ($edad >= 18) {
        echo "Eres mayor de edad.\n";
    } else {
        echo "Eres menor de edad.\n";
    }
}
mayoriaEdad();
?>
