//Interaccion con el usuario

function obtenerAdivinanza() {
    while (true) {
        let entrada = prompt("Adivina el número del 1 al 10:");
        let adivinar = parseInt(entrada);
        
        if (!isNaN(adivinar) && adivinar >= 1 && adivinar <= 10) {
            return adivinar;
        } else {
            alert("Por favor, ingresa un número entre 1 y 10.");
        }
    }
}

function jugar() {
    let num = Math.floor(Math.random() * 10) + 1; // Genera un número aleatorio entre 1 y 10
    let intentos = 3; // Número de intentos permitidos

    console.log("Tienes 3 intentos para adivinar el número.");
    
    for (let i = 0; i < intentos; i++) {
        let adivinar = obtenerAdivinanza();
        
        if (num === adivinar) {
            console.log("¡Has ganado!");
            return;
        } else {
            console.log(`Intento ${i + 1} fallido.`);
        }
    }

    console.log(`Has perdido, el número era: ${num}`);
}

function main() {
    while (true) {
        jugar();
        let continuar = prompt("¿Quieres jugar de nuevo? (s/n):").trim().toLowerCase();
        if (continuar !== 's') {
            console.log("Gracias por jugar. ¡Hasta luego!");
            break;
        }
    }
}
main();