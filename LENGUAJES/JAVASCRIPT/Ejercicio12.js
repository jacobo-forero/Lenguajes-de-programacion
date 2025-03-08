//Tabla de la verdad

function generarCombinaciones(variables) {
    // Genera todas las combinaciones de valores booleanos para las variables dadas.
    const combinaciones = [];
    const totalCombinaciones = Math.pow(2, variables.length);

    for (let i = 0; i < totalCombinaciones; i++) {
        const combinacion = [];
        for (let j = 0; j < variables.length; j++) {
            combinacion.push(Boolean((i >> (variables.length - 1 - j)) & 1));
        }
        combinaciones.push(combinacion);
    }

    return combinaciones;
}

function imprimirTablaVerdad(variables) {
    // Imprime la tabla de verdad para la operación A y B.
    const combinaciones = generarCombinaciones(variables);
    
    // Imprimimos la cabecera de la tabla
    console.log(`${variables.join(' | ')} | ${variables.join(' y ')}`);
    console.log('-'.repeat(variables.length * 4 + 10));  // Ajusta el ancho de la línea

    // Evaluamos la expresión para cada combinación
    for (const combinacion of combinaciones) {
        const resultado = combinacion.every(Boolean);  // A y B
        console.log(combinacion.map(String).join(' | ') + ` | ${resultado}`);
    }
}

function main() {
    // Definimos las variables
    const variables = ['A', 'B'];
    imprimirTablaVerdad(variables);
}
main();