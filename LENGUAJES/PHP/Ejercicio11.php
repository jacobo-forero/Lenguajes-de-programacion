<?php
// OPERACIONES

function suma($num1, $num2) {
    return $num1 + $num2;
}

function resta($num1, $num2) {
    return $num1 - $num2;
}

function multiplicacion($num1, $num2) {
    return $num1 * $num2;
}

function division($num1, $num2) {
    if ($num2 != 0) {
        return $num1 / $num2;
    } else {
        return "No se puede dividir entre cero";
    }
}

function potencia($num1, $num2) {
    return pow($num1, $num2);
}

function main() {
    while (true) {
        echo "\nCalculadora\n";
        echo "1. Suma\n";
        echo "2. Resta\n";
        echo "3. Multiplicación\n";
        echo "4. División\n";
        echo "5. Potencia\n";
        echo "6. Salir\n";

        $opcion = trim(fgets(STDIN));

        if ($opcion == '6') {
            echo "Gracias por usar la calculadora. ¡Hasta luego!\n";
            break;
        }

        echo "Ingresa el primer número: ";
        $num1 = floatval(trim(fgets(STDIN)));
        echo "Ingresa el segundo número: ";
        $num2 = floatval(trim(fgets(STDIN)));

        switch ($opcion) {
            case '1':
                echo "Resultado de la suma: " . suma($num1, $num2) . "\n";
                break;
            case '2':
                echo "Resultado de la resta: " . resta($num1, $num2) . "\n";
                break;
            case '3':
                echo "Resultado de la multiplicación: " . multiplicacion($num1, $num2) . "\n";
                break;
            case '4':
                echo "Resultado de la división: " . division($num1, $num2) . "\n";
                break;
            case '5':
                echo "Resultado de la potencia: " . potencia($num1, $num2) . "\n";
                break;
            default:
                echo "Opción no válida. Por favor, selecciona una opción del 1 al 6.\n";
                break;
        }
    }
}
main();
?>