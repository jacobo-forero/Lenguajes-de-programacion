//LEY OHM
import java.util.Scanner;

public class Ejercicio9 {
    public static double obtenerFloat(String mensaje) {
        Scanner scanner = new Scanner(System.in);
        double valor;

        while (true) {
            System.out.print(mensaje);
            if (scanner.hasNextDouble()) {
                valor = scanner.nextDouble();
                scanner.nextLine(); 
                if (valor >= 0) {
                    return valor;
                } else {
                    System.out.println("El valor no puede ser negativo. Inténtalo de nuevo.");
                }
            } else {
                System.out.println("Error: Debes ingresar un número válido.");
                scanner.next();
            }
        }
    }

    public static void calcularLeyOhm() {
        System.out.println("Calculadora de la Ley de Ohm");
        
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nSelecciona la variable que deseas calcular:");
            System.out.println("1. Voltaje (V)");
            System.out.println("2. Corriente (I)");
            System.out.println("3. Resistencia (R)");
            System.out.println("4. Salir");

            System.out.print("Ingresa el número de la opción (1, 2, 3 o 4): ");
            String opcion = scanner.nextLine();

            if (opcion.equals("1")) {
                double I = obtenerFloat("Ingresa la corriente (I) en amperios: ");
                double R = obtenerFloat("Ingresa la resistencia (R) en ohmios: ");
                double V = I * R;
                System.out.printf("El voltaje (V) es: %.2f voltios%n", V);

            } else if (opcion.equals("2")) {
                double V = obtenerFloat("Ingresa el voltaje (V) en voltios: ");
                double R = obtenerFloat("Ingresa la resistencia (R) en ohmios: ");
                double I = V / R;
                System.out.printf("La corriente (I) es: %.2f amperios%n", I);

            } else if (opcion.equals("3")) {
                double V = obtenerFloat("Ingresa el voltaje (V) en voltios: ");
                double I = obtenerFloat("Ingresa la corriente (I) en amperios: ");
                double R = V / I;
                System.out.printf("La resistencia (R) es: %.2f ohmios%n", R);

            } else if (opcion.equals("4")) {
                System.out.println("Gracias por usar la calculadora de la Ley de Ohm. ¡Hasta luego!");
                break;

            } else {
                System.out.println("Opción no válida. Por favor, selecciona 1, 2, 3 o 4.");
            }
        }
        scanner.close(); 
    }

    public static void main(String[] args) {
        calcularLeyOhm();
    }
}