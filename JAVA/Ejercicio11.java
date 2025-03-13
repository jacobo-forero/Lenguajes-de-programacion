//OPERACIONES
import java.util.Scanner;

public class Ejercicio11 {
    public static double suma(double num1, double num2) {
        return num1 + num2;
    }

    public static double resta(double num1, double num2) {
        return num1 - num2;
    }

    public static double multiplicacion(double num1, double num2) {
        return num1 * num2;
    }

    public static String division(double num1, double num2) {
        if (num2 != 0) {
            return String.valueOf(num1 / num2);
        } else {
            return "No se puede dividir entre cero";
        }
    }

    public static double potencia(double num1, double num2) {
        return Math.pow(num1, num2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nCalculadora");
            System.out.println("1. Suma");
            System.out.println("2. Resta");
            System.out.println("3. Multiplicación");
            System.out.println("4. División");
            System.out.println("5. Potencia");
            System.out.println("6. Salir");

            System.out.print("Selecciona una opción (1-6): ");
            int opcion = scanner.nextInt();

            if (opcion == 6) {
                System.out.println("Gracias por usar la calculadora. ¡Hasta luego!");
                break;
            }

            System.out.print("Ingresa el primer número: ");
            double num1 = scanner.nextDouble();
            System.out.print("Ingresa el segundo número: ");
            double num2 = scanner.nextDouble();

            switch (opcion) {
                case 1:
                    System.out.println("Resultado de la suma: " + suma(num1, num2));
                    break;
                case 2:
                    System.out.println("Resultado de la resta: " + resta(num1, num2));
                    break;
                case 3:
                    System.out.println("Resultado de la multiplicación: " + multiplicacion(num1, num2));
                    break;
                case 4:
                    System.out.println("Resultado de la división: " + division(num1, num2));
                    break;
                case 5:
                    System.out.println("Resultado de la potencia: " + potencia(num1, num2));
                    break;
                default:
                    System.out.println("Opción no válida. Por favor, selecciona una opción del 1 al 6.");
                    break;
            }
        }
        scanner.close(); // Cerrar el scanner al final
    }
}