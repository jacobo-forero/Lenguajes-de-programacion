//Listas

function mostrar(materias) {
    if (materias.length > 0) {
        console.log(`Yo estudio ${materias.length} materias.`);
        console.log("Las materias son:");
        for (let materia of materias) {
            console.log(`- ${materia}`);
        }
    } else {
        console.log("No hay materias para mostrar.");
    }
}

function agregarMateria(materias) {
    let nuevaMateria = prompt("Ingresa el nombre de la nueva materia:").trim();
    if (nuevaMateria) {
        materias.push(nuevaMateria);
        console.log(`La materia '${nuevaMateria}' ha sido agregada.`);
    } else {
        console.log("El nombre de la materia no puede estar vacío.");
    }
}

function main() {
    let lista = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"];
    mostrar(lista);

    while (true) {
        let continuar = prompt("¿Deseas agregar una nueva materia? (s/n):").trim().toLowerCase();
        if (continuar === 's') {
            agregarMateria(lista);
            mostrar(lista);
        } else if (continuar === 'n') {
            console.log("Gracias por usar el programa. ¡Hasta luego!");
            break;
        } else {
            console.log("Opción no válida. Por favor, ingresa 's' o 'n'.");
        }
    }
}
main();