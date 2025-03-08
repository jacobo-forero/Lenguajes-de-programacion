<?php
// INTERACCION USUARIO

function obtenerAdivinanza() {
    while (true) {
        echo "Adivina el número del 1 al 10: ";
        $input = trim(fgets(STDIN));
        
        if (is_numeric($input) && intval($input) >= 1 && intval($input) <= 10) {
            return intval($input);
        } else {
            echo "Por favor, ingresa un número entre 1 y 10.\n";
        }
    }
}

function jugar() {
    $num = rand(1, 10);
    $intentos = 3; // Número de intentos permitidos

    echo "Tienes $intentos intentos para adivinar el número.\n";
    
    for ($i = 0; $i < $intentos; $i++) {
        $adivinar = obtenerAdivinanza();
        
        if ($num === $adivinar) {
            echo "¡Has ganado!\n";
            return;
        } else {
            echo "Intento " . ($i + 1) . " fallido.\n";
        }
    }
    
    echo "Has perdido, el número era: $num\n";
}

function main() {
    while (true) {
        jugar();
        echo "¿Quieres jugar de nuevo? (s/n): ";
        $continuar = trim(fgets(STDIN));
        
        if (strtolower($continuar) !== 's') {
            echo "Gracias por jugar. ¡Hasta luego!\n";
            break;
        }
    }
}
main();
?>