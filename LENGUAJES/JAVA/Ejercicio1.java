// BUCLES FOR
import java.util.Scanner;

public class Ejercicio1 {
    public static void mostrarPalabra() {
        Scanner scanner = new Scanner(System.in);
        String palabra;
        
        // Solicitar al usuario que ingrese una palabra
        System.out.print("Ingrese la palabra que quiere que se repita: ");
        palabra = scanner.nextLine().trim();
        
        // Validar que la palabra no esté vacía
        while (palabra.isEmpty()) {
            System.out.println("La entrada no puede estar vacía. Inténtalo de nuevo.");
            System.out.print("Ingrese la palabra que quiere que se repita: ");
            palabra = scanner.nextLine().trim();
        }
        
        int repeticiones;
        // Solicitar al usuario cuántas veces quiere que se repita la palabra
        while (true) {
            System.out.print("¿Cuántas veces quiere que se repita la palabra? ");
            if (scanner.hasNextInt()) {
                repeticiones = scanner.nextInt();
                if (repeticiones > 0) {
                    break;
                } else {
                    System.out.println("Por favor, ingrese un número positivo.");
                }
            } else {
                System.out.println("Entrada no válida. Por favor, ingrese un número entero.");
                scanner.next(); // Limpiar el buffer
            }
        }
        
        // Imprimir la palabra la cantidad de veces especificada
        for (int i = 0; i < repeticiones; i++) {
            System.out.println(palabra);
        }
        
        scanner.close();
    }

    public static void main(String[] args) {
        mostrarPalabra();
    }
}