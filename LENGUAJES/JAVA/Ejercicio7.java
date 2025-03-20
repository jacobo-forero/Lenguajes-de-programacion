//FUNCIONES
import java.util.Scanner;

public class Ejercicio7 {
    public static String obtenerNombre() {
        Scanner scanner = new Scanner(System.in);
        String nombre;

        while (true) {
            System.out.print("Ingrese su nombre: ");
            nombre = scanner.nextLine().trim();
            if (!nombre.isEmpty()) {
                return nombre;
            } else {
                System.out.println("El nombre no puede estar vacío. Inténtalo de nuevo.");
            }
        }
    }

    public static void saludo(String nombre) {
        System.out.println("Hola " + nombre + ", bienvenido/a!");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String nombre = obtenerNombre();
            saludo(nombre);
            
            System.out.print("¿Deseas saludar a otra persona? (s/n): ");
            String continuar = scanner.nextLine().trim().toLowerCase();
            
            if (!continuar.equals("s")) {
                System.out.println("Gracias por usar el programa. ¡Hasta luego!");
                break;
            }
        }
        scanner.close(); 
    }
}