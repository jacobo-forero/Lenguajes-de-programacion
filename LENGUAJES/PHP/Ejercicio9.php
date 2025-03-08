<?php
// LEY OHM

function obtenerFloat($mensaje) {
    while (true) {
        echo $mensaje;
        $input = trim(fgets(STDIN));
        
        if (is_numeric($input) && floatval($input) >= 0) {
            return floatval($input);
        } else {
            echo "Error: Debes ingresar un número válido y no negativo.\n";
        }
    }
}

function calcularLeyOhm() {
    echo "Calculadora de la Ley de Ohm\n";
    
    while (true) {
        echo "\nSelecciona la variable que deseas calcular:\n";
        echo "1. Voltaje (V)\n";
        echo "2. Corriente (I)\n";
        echo "3. Resistencia (R)\n";
        echo "4. Salir\n";

        $opcion = trim(fgets(STDIN));

        if ($opcion == '1') {
            $I = obtenerFloat("Ingresa la corriente (I) en amperios: ");
            $R = obtenerFloat("Ingresa la resistencia (R) en ohmios: ");
            $V = $I * $R;
            echo "El voltaje (V) es: " . number_format($V, 2) . " voltios\n";

        } elseif ($opcion == '2') {
            $V = obtenerFloat("Ingresa el voltaje (V) en voltios: ");
            $R = obtenerFloat("Ingresa la resistencia (R) en ohmios: ");
            $I = $V / $R;
            echo "La corriente (I) es: " . number_format($I, 2) . " amperios\n";

        } elseif ($opcion == '3') {
            $V = obtenerFloat("Ingresa el voltaje (V) en voltios: ");
            $I = obtenerFloat("Ingresa la corriente (I) en amperios: ");
            $R = $V / $I;
            echo "La resistencia (R) es: " . number_format($R, 2) . " ohmios\n";

        } elseif ($opcion == '4') {
            echo "Gracias por usar la calculadora de la Ley de Ohm. ¡Hasta luego!\n";
            break;

        } else {
            echo "Opción no válida. Por favor, selecciona 1, 2, 3 o 4.\n";
        }
    }
}
calcularLeyOhm();
?>