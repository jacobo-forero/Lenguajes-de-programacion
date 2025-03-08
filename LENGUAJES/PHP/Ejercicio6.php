<?php
//DICCIONARIO

function obtenerDivisas() {
    return [
        'Euro' => '€',
        'Dollar' => '$',
        'Yen' => '¥',
        'Peso' => '$'
    ];
}

function conversor() {
    $divisas = obtenerDivisas();
    
    while (true) {
        echo "Ingrese el tipo de divisa (o 'salir' para terminar): ";
        $divisa = trim(fgets(STDIN));
        
        if (strtolower($divisa) === 'salir') {
            echo "Gracias por usar el conversor de divisas. ¡Hasta luego!\n";
            break;
        }
        
        $divisaCapitalizada = ucfirst(strtolower($divisa));
        
        if (array_key_exists($divisaCapitalizada, $divisas)) {
            echo "Esta es la divisa: " . $divisas[$divisaCapitalizada] . "\n";
        } else {
            echo "Divisa no encontrada. Por favor, intenta de nuevo.\n";
        }
    }
}
conversor();
?>