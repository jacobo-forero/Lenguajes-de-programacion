// CAJERO 
import java.util.Scanner;

public class Ejercicio3 {
    public static void mostrarMenu() {
        System.out.println("\nBienvenido al cajero");
        System.out.println("1. Ingresar dinero");
        System.out.println("2. Retirar dinero");
        System.out.println("3. Ver saldo");
        System.out.println("4. Salir");
    }

    public static double obtenerMonto(String mensaje) {
        Scanner scanner = new Scanner(System.in);
        double monto;

        while (true) {
            System.out.print(mensaje);
            if (scanner.hasNextDouble()) {
                monto = scanner.nextDouble();
                scanner.nextLine(); // Limpiar el buffer
                if (monto >= 0) {
                    return monto;
                } else {
                    System.out.println("El monto debe ser un número positivo. Inténtalo de nuevo.");
                }
            } else {
                System.out.println("Error, por favor ingrese un número válido.");
                scanner.next(); // Limpiar la entrada incorrecta
            }
        }
    }

    public static void cajero() {
        double saldo = 1000.0;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            mostrarMenu();
            System.out.print("¿Qué deseas hacer? ");
            String opcion = scanner.nextLine();
            
            if (opcion.equals("1")) {
                double monto = obtenerMonto("¿Cuánto dinero deseas ingresar? $");
                saldo += monto;
                System.out.printf("Se ha ingresado $%.2f a tu cuenta. Tu saldo actual es $%.2f.%n", monto, saldo);
            
            } else if (opcion.equals("2")) {
                double monto = obtenerMonto("¿Cuánto dinero deseas retirar? $");
                if (monto <= saldo) {
                    saldo -= monto;
                    System.out.printf("Se ha retirado $%.2f de tu cuenta. Tu saldo actual es $%.2f.%n", monto, saldo);
                } else {
                    System.out.println("Error: No tienes suficiente saldo para realizar esta operación.");
                }
            
            } else if (opcion.equals("3")) {
                System.out.printf("Tu saldo actual es $%.2f.%n", saldo);
            
            } else if (opcion.equals("4")) {
                System.out.println("Gracias por utilizar el cajero.");
                break;
            
            } else {
                System.out.println("Opción no válida. Por favor, intenta de nuevo.");
            }
        }
        scanner.close(); // Cerrar el scanner al final
    }

    public static void main(String[] args) {
        cajero();
    }
}