//Operaciones

function suma(num1, num2) {
    return num1 + num2;
}

function resta(num1, num2) {
    return num1 - num2;
}

function multiplicacion(num1, num2) {
    return num1 * num2;
}

function division(num1, num2) {
    if (num2 !== 0) {
        return num1 / num2;
    } else {
        return "No se puede dividir entre cero";
    }
}

function potencia(num1, num2) {
    return Math.pow(num1, num2);
}

function main() {
    while (true) {
        console.log("\nCalculadora");
        console.log("1. Suma");
        console.log("2. Resta");
        console.log("3. Multiplicación");
        console.log("4. División");
        console.log("5. Potencia");
        console.log("6. Salir");

        let opcion = prompt("Selecciona una opción (1-6):");

        if (opcion === '6') {
            console.log("Gracias por usar la calculadora. ¡Hasta luego!");
            break;
        }

        let num1 = parseFloat(prompt("Ingresa el primer número:"));
        let num2 = parseFloat(prompt("Ingresa el segundo número:"));

        if (opcion === '1') {
            console.log("Resultado de la suma:", suma(num1, num2));
        } else if (opcion === '2') {
            console.log("Resultado de la resta:", resta(num1, num2));
        } else if (opcion === '3') {
            console.log("Resultado de la multiplicación:", multiplicacion(num1, num2));
        } else if (opcion === '4') {
            let resultado = division(num1, num2);
            console.log("Resultado de la división:", resultado);
        } else if (opcion === '5') {
            console.log("Resultado de la potencia:", potencia(num1, num2));
        } else {
            console.log("Opción no válida. Por favor, selecciona una opción del 1 al 6.");
        }
    }
}
main();