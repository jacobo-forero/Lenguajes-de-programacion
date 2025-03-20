//TABLA DE LA VERDAD
import java.util.ArrayList;
import java.util.List;

public class Ejercicio12 {
    public static List<List<Boolean>> generarCombinaciones(int n) {
        List<List<Boolean>> combinaciones = new ArrayList<>();
        int total = 1 << n; // 2^n combinaciones

        for (int i = 0; i < total; i++) {
            List<Boolean> combinacion = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                combinacion.add((i & (1 << (n - j - 1))) != 0);
            }
            combinaciones.add(combinacion);
        }
        return combinaciones;
    }

    public static void imprimirTablaVerdad(String[] variables) {
        List<List<Boolean>> combinaciones = generarCombinaciones(variables.length);

        // Imprimimos la cabecera de la tabla
        for (String var : variables) {
            System.out.print(var + " | ");
        }
        System.out.println("A y B");
        System.out.println("-".repeat(variables.length * 4 + 10)); // Ajusta el ancho de la línea

        // Evaluamos la expresión para cada combinación
        for (List<Boolean> combinacion : combinaciones) {
            boolean resultado = true; // A y B
            for (boolean valor : combinacion) {
                System.out.print((valor ? "1" : "0") + " | "); // Imprimir 1 para true y 0 para false
                resultado = resultado && valor; // A y B
            }
            System.out.println((resultado ? "1" : "0")); // Imprimir resultado
        }
    }

    public static void main(String[] args) {
        // Definimos las variables
        String[] variables = {"A", "B"};
        imprimirTablaVerdad(variables);
    }
}