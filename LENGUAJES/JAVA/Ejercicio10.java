//LISTAS
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ejercicio10 {
    public static void mostrar(List<String> materias) {
        if (!materias.isEmpty()) {
            System.out.println("Yo estudio " + materias.size() + " materias.");
            System.out.println("Las materias son:");
            for (String materia : materias) {
                System.out.println("- " + materia);
            }
        } else {
            System.out.println("No hay materias para mostrar.");
        }
    }

    public static void agregarMateria(List<String> materias) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa el nombre de la nueva materia: ");
        String nuevaMateria = scanner.nextLine().trim();
        if (!nuevaMateria.isEmpty()) {
            materias.add(nuevaMateria);
            System.out.println("La materia '" + nuevaMateria + "' ha sido agregada.");
        } else {
            System.out.println("El nombre de la materia no puede estar vacío.");
        }
    }

    public static void main(String[] args) {
        List<String> lista = new ArrayList<>();
        lista.add("Matematicas");
        lista.add("Fisica");
        lista.add("Quimica");
        lista.add("Historia");
        lista.add("Lengua");
        
        mostrar(lista);

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("¿Deseas agregar una nueva materia? (s/n): ");
            String continuar = scanner.nextLine().trim().toLowerCase();
            if (continuar.equals("s")) {
                agregarMateria(lista);
                mostrar(lista);
            } else if (continuar.equals("n")) {
                System.out.println("Gracias por usar el programa. ¡Hasta luego!");
                break;
            } else {
                System.out.println("Opción no válida. Por favor, ingresa 's' o 'n'.");
            }
        }
        scanner.close(); // Cerrar el scanner al final
    }
}