<?php
// TABLA DE LA VERDAD

function generarCombinaciones($variables) {

    // Genera todas las combinaciones de valores booleanos para las variables dadas
    $combinaciones = [];
    $numVariables = count($variables);
    $totalCombinaciones = pow(2, $numVariables); // 2^n combinaciones

    for ($i = 0; $i < $totalCombinaciones; $i++) {
        $combinacion = [];
        for ($j = 0; $j < $numVariables; $j++) {
            $combinacion[] = (bool) (($i >> $j) & 1); // Genera True o False
        }
        $combinaciones[] = $combinacion;
    }
    return $combinaciones;
}

function imprimirTablaVerdad($variables) {
    //Imprime la tabla de verdad para la operación A AND B.
    $combinaciones = generarCombinaciones($variables);
    
    // Imprimimos la cabecera de la tabla
    echo implode(" | ", $variables) . " | " . implode(" AND ", $variables) . "\n";
    echo str_repeat("-", (count($variables) * 4 + 10)) . "\n"; // Ajusta el ancho de la línea

    // Evaluamos la expresión para cada combinación
    foreach ($combinaciones as $combinacion) {
        $resultado = $combinacion[0] && $combinacion[1]; // A AND B
        echo implode(" | ", array_map('var_export', $combinacion, array_fill(0, count($combinacion), true))) . " | " . ($resultado ? 'true' : 'false') . "\n";
    }
}

function main() {
    // Definimos las variables
    $variables = ['A', 'B'];
    imprimirTablaVerdad($variables);
}
main();
?>