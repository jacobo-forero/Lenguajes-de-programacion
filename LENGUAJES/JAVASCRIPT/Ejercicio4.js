//Ciclo for

function obtenerFloat(mensaje) {
    while (true) {
        let entrada = prompt(mensaje);
        let valor = parseFloat(entrada);
        
        if (!isNaN(valor) && valor >= 0) {
            return valor;
        } else {
            alert("El valor debe ser un número positivo. Inténtalo de nuevo.");
        }
    }
}

function obtenerInt(mensaje) {
    while (true) {
        let entrada = prompt(mensaje);
        let valor = parseInt(entrada);
        
        if (!isNaN(valor) && valor >= 0) {
            return valor;
        } else {
            alert("El valor debe ser un número entero positivo. Inténtalo de nuevo.");
        }
    }
}

function inversion() {
    let cant = obtenerFloat("Ingrese la cantidad a invertir: $");
    let inter = obtenerFloat("Ingrese el interés anual (en %): ");
    let años = obtenerInt("Ingrese el número de años: ");
    
    console.log("\nResumen de la inversión:");
    for (let i = 1; i <= años; i++) {
        cant += cant * (inter / 100);
        console.log(`Año ${i}: Capital obtenido será: $${cant.toFixed(2)}`);
    }
}
inversion();