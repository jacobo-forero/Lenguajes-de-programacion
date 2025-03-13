// BUCLES WHILE

import java.util.Scanner;

public class Ejercicio2 {
    public static int obtenerNumero() {
        Scanner scanner = new Scanner(System.in);
        int num;

        while (true) {
            System.out.print("Ingrese un número para conocer la tabla de multiplicar: ");
            if (scanner.hasNextInt()) {
                num = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer
                return num;
            } else {
                System.out.println("Error, por favor ingrese un número entero.");
                scanner.next(); // Limpiar la entrada incorrecta
            }
        }
    }

    public static void mostrarTabla(int num) {
        System.out.println("\nTabla de multiplicar del " + num + ":");
        for (int i = 1; i <= 10; i++) {
            System.out.println(num + " x " + i + " = " + (num * i));
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            int numero = obtenerNumero();
            mostrarTabla(numero);
            
            System.out.print("\n¿Desea calcular otra tabla? (s/n): ");
            String continuar = scanner.nextLine().trim().toLowerCase();

            if (!continuar.equals("s")) {
                System.out.println("Gracias por usar el programa. ¡Hasta luego!");
                break;
            }
        }
        scanner.close();
    }
}