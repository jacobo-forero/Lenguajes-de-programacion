//Ley ohm

function obtenerFloat(mensaje) {
    while (true) {
        let entrada = prompt(mensaje);
        let valor = parseFloat(entrada);
        
        if (!isNaN(valor) && valor >= 0) {
            return valor;
        } else {
            alert("Error: Debes ingresar un número válido.");
        }
    }
}

function calcularLeyOhm() {
    console.log("Calculadora de la Ley de Ohm");
    
    while (true) {
        console.log("\nSelecciona la variable que deseas calcular:");
        console.log("1. Voltaje (V)");
        console.log("2. Corriente (I)");
        console.log("3. Resistencia (R)");
        console.log("4. Salir");

        let opcion = prompt("Ingresa el número de la opción (1, 2, 3 o 4):");

        if (opcion === '1') {
            let I = obtenerFloat("Ingresa la corriente (I) en amperios:");
            let R = obtenerFloat("Ingresa la resistencia (R) en ohmios:");
            let V = I * R;
            console.log(`El voltaje (V) es: ${V.toFixed(2)} voltios`);

        } else if (opcion === '2') {
            let V = obtenerFloat("Ingresa el voltaje (V) en voltios:");
            let R = obtenerFloat("Ingresa la resistencia (R) en ohmios:");
            let I = V / R;
            console.log(`La corriente (I) es: ${I.toFixed(2)} amperios`);

        } else if (opcion === '3') {
            let V = obtenerFloat("Ingresa el voltaje (V) en voltios:");
            let I = obtenerFloat("Ingresa la corriente (I) en amperios:");
            let R = V / I;
            console.log(`La resistencia (R) es: ${R.toFixed(2)} ohmios`);

        } else if (opcion === '4') {
            console.log("Gracias por usar la calculadora de la Ley de Ohm. ¡Hasta luego!");
            break;

        } else {
            console.log("Opción no válida. Por favor, selecciona 1, 2, 3 o 4.");
        }
    }
}
calcularLeyOhm();