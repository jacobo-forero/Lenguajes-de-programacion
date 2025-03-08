// Bucles for
function mostrarPalabra() {
    // Solicitar al usuario que ingrese una palabra
    let palabra = prompt("Ingrese la palabra que quiere que se repita:").trim();
    
    // Validar que la palabra no esté vacía
    while (!palabra) {
        alert("La entrada no puede estar vacía. Inténtalo de nuevo.");
        palabra = prompt("Ingrese la palabra que quiere que se repita:").trim();
    }
    
    // Solicitar al usuario cuántas veces quiere que se repita la palabra
    let repeticiones;
    while (true) {
        repeticiones = prompt("¿Cuántas veces quiere que se repita la palabra?");
        if (isNaN(repeticiones) || repeticiones <= 0) {
            alert("Por favor, ingrese un número positivo.");
        } else {
            repeticiones = parseInt(repeticiones);
            break;
        }
    }
    
    // Imprimir la palabra la cantidad de veces especificada
    for (let i = 0; i < repeticiones; i++) {
        console.log(palabra);
    }
}
mostrarPalabra();