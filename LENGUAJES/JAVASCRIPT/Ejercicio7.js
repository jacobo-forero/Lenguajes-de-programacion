//Funciones

function obtenerNombre() {
    while (true) {
        let nombre = prompt("Ingrese su nombre:").trim();
        if (nombre) {
            return nombre;
        } else {
            alert("El nombre no puede estar vacío. Inténtalo de nuevo.");
        }
    }
}

function saludo(nombre) {
    console.log(`Hola ${nombre}, bienvenido/a!`);
}

function main() {
    while (true) {
        let nombre = obtenerNombre();
        saludo(nombre);
        
        let continuar = prompt("¿Deseas saludar a otra persona? (s/n):").trim().toLowerCase();
        if (continuar !== 's') {
            console.log("Gracias por usar el programa. ¡Hasta luego!");
            break;
        }
    }
}
main();