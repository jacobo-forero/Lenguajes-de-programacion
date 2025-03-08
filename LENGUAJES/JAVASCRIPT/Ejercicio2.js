// Bucles WHILE

function obtenerNumero() {
    while (true) {
        let entrada = prompt("Ingrese un número para conocer la tabla de multiplicar:");
        let num = parseInt(entrada);
        
        if (!isNaN(num)) {
            return num;
        } else {
            alert("Error, por favor ingrese un número entero.");
        }
    }
}

function mostrarTabla(num) {
    console.log(`\nTabla de multiplicar del ${num}:`);
    for (let i = 1; i <= 10; i++) {
        console.log(`${num} x ${i} = ${num * i}`);
    }
}

function main() {
    while (true) {
        let numero = obtenerNumero();
        mostrarTabla(numero);
        
        let continuar = prompt("\n¿Desea calcular otra tabla? (s/n):").trim().toLowerCase();
        if (continuar !== 's') {
            console.log("Gracias por usar el programa. ¡Hasta luego!");
            break;
        }
    }
}
main();