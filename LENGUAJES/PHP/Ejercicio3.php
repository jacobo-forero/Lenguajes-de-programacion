<?php
// CAJERO

function mostrarMenu() {
    echo "\nBienvenido al cajero\n";
    echo "1. Ingresar dinero\n";
    echo "2. Retirar dinero\n";
    echo "3. Ver saldo\n";
    echo "4. Salir\n";
}

function obtenerMonto($mensaje) {
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

function cajero() {
    $saldo = 1000;
    
    while (true) {
        mostrarMenu();
        echo "¿Qué deseas hacer? ";
        $opcion = trim(fgets(STDIN));
        
        if ($opcion == "1") {
            $monto = obtenerMonto("¿Cuánto dinero deseas ingresar? $");
            $saldo += $monto;
            echo "Se ha ingresado $" . number_format($monto, 2) . " a tu cuenta. Tu saldo actual es $" . number_format($saldo, 2) . ".\n";
        
        } elseif ($opcion == "2") {
            $monto = obtenerMonto("¿Cuánto dinero deseas retirar? $");
            if ($monto <= $saldo) {
                $saldo -= $monto;
                echo "Se ha retirado $" . number_format($monto, 2) . " de tu cuenta. Tu saldo actual es $" . number_format($saldo, 2) . ".\n";
            } else {
                echo "Error: No tienes suficiente saldo para realizar esta operación.\n";
            }
        
        } elseif ($opcion == "3") {
            echo "Tu saldo actual es $" . number_format($saldo, 2) . ".\n";
        
        } elseif ($opcion == "4") {
            echo "Gracias por utilizar el cajero.\n";
            break;
        
        } else {
            echo "Opción no válida. Por favor, intenta de nuevo.\n";
        }
    }
}
cajero();
?>