//Condicionales IF ELSE
import java.util.Scanner;

public class Ejercicio5 {
    public static int obtenerEdad() {
        Scanner scanner = new Scanner(System.in);
        int edad;

        while (true) {
            System.out.print("Ingresa tu edad: ");
            if (scanner.hasNextInt()) {
                edad = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer
                if (edad >= 0) {
                    return edad;
                } else {
                    System.out.println("La edad no puede ser negativa. Inténtalo de nuevo.");
                }
            } else {
                System.out.println("Error, por favor ingresa un número entero válido.");
                scanner.next(); // Limpiar la entrada incorrecta
            }
        }
    }

    public static void mayoriaEdad() {
        int edad = obtenerEdad();
        
        if (edad >= 18) {
            System.out.println("Eres mayor de edad.");
        } else {
            System.out.println("Eres menor de edad.");
        }
    }

    public static void main(String[] args) {
        mayoriaEdad();
    }
}