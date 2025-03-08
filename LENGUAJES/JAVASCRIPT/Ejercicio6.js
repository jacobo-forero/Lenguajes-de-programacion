//Diccionario

function obtenerDivisas() {
    return {
        'Dollar': '$',
        'Euro': '€',
        'Yen': '¥',
        'Peso': '$'
    };
}

function conversor() {
    const divisas = obtenerDivisas();
    
    while (true) {
        let divisa = prompt("Ingrese el tipo de divisa (o 'salir' para terminar):").capitalize();
        
        if (divisa.toLowerCase() === 'salir') {
            console.log("Gracias por usar el conversor de divisas. ¡Hasta luego!");
            break;
        }
        
        if (divisa in divisas) {
            console.log("Esta es la divisa:", divisas[divisa]);
        } else {
            console.log("Divisa no encontrada. Por favor, intenta de nuevo.");
        }
    }
}

// Método para capitalizar la primera letra de la cadena
String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1).toLowerCase();
}
conversor();