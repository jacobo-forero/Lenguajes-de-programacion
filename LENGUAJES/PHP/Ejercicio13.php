<?php
// OCTAVOS DE FINAL

function simularPartido($equipo1, $equipo2) {
    /** Simula un partido entre dos equipos y devuelve el ganador. */
    return rand(0, 1) ? $equipo1 : $equipo2;
}

function octavosDeFinal($equipos) {
    /** Simula los octavos de final con los equipos dados. */
    echo "Octavos de Final:\n";
    $ganadores = [];

    // Asegurarse de que hay un número par de equipos
    if (count($equipos) % 2 != 0) {
        echo "El número de equipos debe ser par.\n";
        return;
    }

    for ($i = 0; $i < count($equipos); $i += 2) {
        $equipo1 = $equipos[$i];
        $equipo2 = $equipos[$i + 1];
        $ganador = simularPartido($equipo1, $equipo2);
        $ganadores[] = $ganador;
        echo "Partido: $equipo1 vs $equipo2 - Ganador: $ganador\n";
    }

    return $ganadores;
}

function main() {
    // Definimos los equipos que participan en los octavos de final
    $equipos = [
        "FC Barcelona",
        "Real Madrid",
        "Arsenal",
        "Manchester City",
        "Chelsea",
        "Liverpool",
        "PSG",
        "Benfica"
    ];

    // Simular los octavos de final
    $ganadores = octavosDeFinal($equipos);

    echo "\nEquipos que avanzan a los cuartos de final:\n";
    foreach ($ganadores as $ganador) {
        echo "$ganador\n";
    }
}
main();
?>