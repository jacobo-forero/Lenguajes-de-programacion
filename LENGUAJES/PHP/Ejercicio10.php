<?php
// LISTAS

function mostrar($materias) {
    if (!empty($materias)) {
        echo "Yo estudio " . count($materias) . " materias.\n";
        echo "Las materias son:\n";
        foreach ($materias as $materia) {
            echo "- $materia\n";
        }
    } else {
        echo "No hay materias para mostrar.\n";
    }
}

function agregarMateria(&$materias) {
    echo "Ingresa el nombre de la nueva materia: ";
    $nuevaMateria = trim(fgets(STDIN));
    
    if (!empty($nuevaMateria)) {
        $materias[] = $nuevaMateria;
        echo "La materia '$nuevaMateria' ha sido agregada.\n";
    } else {
        echo "El nombre de la materia no puede estar vacío.\n";
    }
}

function main() {
    $lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"];
    mostrar($lista);

    while (true) {
        echo "¿Deseas agregar una nueva materia? (s/n): ";
        $continuar = trim(fgets(STDIN));
        
        if (strtolower($continuar) === 's') {
            agregarMateria($lista);
            mostrar($lista);
        } elseif (strtolower($continuar) === 'n') {
            echo "Gracias por usar el programa. ¡Hasta luego!\n";
            break;
        } else {
            echo "Opción no válida. Por favor, ingresa 's' o 'n'.\n";
        }
    }
}
main();
?>