// Octavos de final

function simularPartido(equipo1, equipo2) {
    // Simula un partido entre dos equipos y devuelve el ganador.
    return Math.random() < 0.5 ? equipo1 : equipo2;
}

function octavosDeFinal(equipos) {
    // Simula los octavos de final con los equipos dados.
    console.log("Octavos de Final:");
    const ganadores = [];

    // Asegurarse de que hay un número par de equipos
    if (equipos.length % 2 !== 0) {
        console.log("El número de equipos debe ser par.");
        return;
    }

    for (let i = 0; i < equipos.length; i += 2) {
        const equipo1 = equipos[i];
        const equipo2 = equipos[i + 1];
        const ganador = simularPartido(equipo1, equipo2);
        ganadores.push(ganador);
        console.log(`Partido: ${equipo1} vs ${equipo2} - Ganador: ${ganador}`);
    }

    return ganadores;
}

function main() {
    // Definimos los equipos que participan en los octavos de final
    const equipos = [
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
    const ganadores = octavosDeFinal(equipos);

    console.log("\nEquipos que avanzan a los cuartos de final:");
    for (const ganador of ganadores) {
        console.log(ganador);
    }
}
main();