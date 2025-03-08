// Condicionales IF, ELSE

function obtenerEdad() {
    while (true) {
        let entrada = prompt("Ingresa tu edad:");
        let edad = parseInt(entrada);
        
        if (!isNaN(edad) && edad >= 0) {
            return edad;
        } else {
            alert("La edad no puede ser negativa. Inténtalo de nuevo.");
        }
    }
}

function mayoriaEdad() {
    let edad = obtenerEdad();
    
    if (edad >= 18) {
        console.log("Eres mayor de edad.");
    } else {
        console.log("Eres menor de edad.");
    }
}
mayoriaEdad();