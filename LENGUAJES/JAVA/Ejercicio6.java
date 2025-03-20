//DICCIONARIO
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Ejercicio6 {
    public static Map<String, String> obtenerDivisas() {
        Map<String, String> divisas = new HashMap<>();
        divisas.put("Dollar", "$");
        divisas.put("Euro", "€");
        divisas.put("Yen", "¥");
        divisas.put("Peso", "$");
        return divisas;
    }

    public static void conversor() {
        Map<String, String> divisas = obtenerDivisas();
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.print("Ingrese el tipo de divisa (o 'salir' para terminar): ");
            String divisa = scanner.nextLine().trim();
            
            // Capitalizar la primera letra
            if (!divisa.isEmpty()) {
                divisa = Character.toUpperCase(divisa.charAt(0)) + divisa.substring(1).toLowerCase();
            }

            if (divisa.equalsIgnoreCase("salir")) {
                System.out.println("Gracias por usar el conversor de divisas. ¡Hasta luego!");
                break;
            }
            
            if (divisas.containsKey(divisa)) {
                System.out.println("Esta es la divisa: " + divisas.get(divisa));
            } else {
                System.out.println("Divisa no encontrada. Por favor, intenta de nuevo.");
            }
        }
        scanner.close(); // Cerrar el scanner al final
    }

    public static void main(String[] args) {
        conversor();
    }
}