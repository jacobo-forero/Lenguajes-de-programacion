//INTERACCION CON EL USUARIO
import java.util.Random;
import java.util.Scanner;

public class Ejercicio8 {
    public static int obtenerAdivinanza() {
        Scanner scanner = new Scanner(System.in);
        int adivinar;

        while (true) {
            System.out.print("Adivina el número del 1 al 10: ");
            if (scanner.hasNextInt()) {
                adivinar = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer
                if (adivinar >= 1 && adivinar <= 10) {
                    return adivinar;
                } else {
                    System.out.println("Por favor, ingresa un número entre 1 y 10.");
                }
            } else {
                System.out.println("Error: Debes ingresar un número entero.");
                scanner.next(); // Limpiar la entrada incorrecta
            }
        }
    }

    public static void jugar() {
        Random random = new Random();
        int num = random.nextInt(10) + 1; // Generar un número aleatorio entre 1 y 10
        int intentos = 3; // Número de intentos permitidos

        System.out.println("Tienes 3 intentos para adivinar el número.");
        
        for (int i = 0; i < intentos; i++) {
            int adivinar = obtenerAdivinanza();
            
            if (num == adivinar) {
                System.out.println("¡Has ganado!");
                return;
            } else {
                System.out.println("Intento " + (i + 1) + " fallido.");
            }
        }
        
        System.out.println("Has perdido, el número era: " + num);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            jugar();
            System.out.print("¿Quieres jugar de nuevo? (s/n): ");
            String continuar = scanner.nextLine().trim().toLowerCase();
            
            if (!continuar.equals("s")) {
                System.out.println("Gracias por jugar. ¡Hasta luego!");
                break;
            }
        }
       