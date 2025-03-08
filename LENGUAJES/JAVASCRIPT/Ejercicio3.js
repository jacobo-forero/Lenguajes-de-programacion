//Cajero

function mostrarMenu() {
    console.log("\nBienvenido al cajero");
    console.log("1. Ingresar dinero");
    console.log("2. Retirar dinero");
    console.log("3. Ver saldo");
    console.log("4. Salir");
}

function obtenerMonto(mensaje) {
    while (true) {
        let entrada = prompt(mensaje);
        let monto = parseFloat(entrada);
        
        if (!isNaN(monto) && monto >= 0) {
            return monto;
        } else {
            alert("El monto debe ser un número positivo. Inténtalo de nuevo.");
        }
    }
}

function cajero() {
    let saldo = 1000;
    while (true) {
        mostrarMenu();
        let opcion = prompt("¿Qué deseas hacer?");
        
        if (opcion === "1") {
            let monto = obtenerMonto("¿Cuánto dinero deseas ingresar? $");
            saldo += monto;
            console.log(`Se ha ingresado $${monto.toFixed(2)} a tu cuenta. Tu saldo actual es $${saldo.toFixed(2)}.`);
        
        } else if (opcion === "2") {
            let monto = obtenerMonto("¿Cuánto dinero deseas retirar? $");
            if (monto <= saldo) {
                saldo -= monto;
                console.log(`Se ha retirado $${monto.toFixed(2)} de tu cuenta. Tu saldo actual es $${saldo.toFixed(2)}.`);
            } else {
                console.log("Error: No tienes suficiente saldo para realizar esta operación.");
            }
        
        } else if (opcion === "3") {
            console.log(`Tu saldo actual es $${saldo.toFixed(2)}.`);
        
        } else if (opcion === "4") {
            console.log("Gracias por utilizar el cajero.");
            break;
        
        } else {
            console.log("Opción no válida. Por favor, intenta de nuevo.");
        }
    }
}
cajero();