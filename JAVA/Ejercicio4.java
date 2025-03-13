// CICLO FOR
import java.util.Scanner;

public class Ejercicio4 {
    public static double obtenerFloat(String mensaje) {
        Scanner scanner = new Scanner(System.in);
        double valor;

        while (true) {
            System.out.print(mensaje);
            if (scanner.hasNextDouble()) {
                valor = scanner.nextDouble();
                scanner.nextLine(); // Limpiar el buffer
                if (valor >= 0) {
                    return valor;
                } else {
                    System.out.println("El valor debe ser un número positivo. Inténtalo de nuevo.");
                }
            } else {
                System.out.println("Error, por favor ingrese un número válido.");
                scanner.next(); // Limpiar la entrada incorrecta
            }
        }
    }

    public static int obtenerInt(String mensaje) {
        Scanner scanner = new Scanner(System.in);
        int valor;

        while (true) {
            System.out.print(mensaje);
            if (scanner.hasNextInt()) {
                valor = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer
                if (valor >= 0) {
                    return valor;
                } else {
                    System.out.println("El valor debe ser un número entero positivo. Inténtalo de nuevo.");
                }
            } else {
                System.out.println("Error, por favor ingrese un número válido.");
                scanner.next(); // Limpiar la entrada incorrecta
            }
        }
    }

    public static void inversion() {
        double cant = obtenerFloat("Ingrese la cantidad a invertir: $");
        double inter = obtenerFloat("Ingrese el interés anual (en %): ");
        int años = obtenerInt("Ingrese el número de años: ");
        
        System.out.println("\nResumen de la inversión:");
        for (int i = 1; i <= años; i++) {
            cant += cant * (inter / 100);
            System.out.printf("Año %d: Capital obtenido será: $%.2f%n", i, cant);
        }
    }

    public static void main(String[] args) {
        inversion();
    }
}

