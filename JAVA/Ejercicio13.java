// OCTAVOS DE FINAL
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Ejercicio13 {
    public static String simularPartido(String equipo1, String equipo2) {
        // Simula un partido entre dos equipos y devuelve el ganador.
        Random random = new Random();
        return random.nextBoolean() ? equipo1 : equipo2;
    }

    public static List<String> octavosDeFinal(List<String> equipos) {
        // Simula los octavos de final con los equipos dados.
        System.out.println("Octavos de Final:");
        List<String> ganadores = new ArrayList<>();

        // Asegurarse de que hay un número par de equipos
        if (equipos.size() % 2 != 0) {
            System.out.println("El número de equipos debe ser par.");
            return ganadores;
        }

        for (int i = 0; i < equipos.size(); i += 2) {
            String equipo1 = equipos.get(i);
            String equipo2 = equipos.get(i + 1);
            String ganador = simularPartido(equipo1, equipo2);
            ganadores.add(ganador);
            System.out.println("Partido: " + equipo1 + " vs " + equipo2 + " - Ganador: " + ganador);
        }

        return ganadores;
    }

    public static void main(String[] args) {
        // Definimos los equipos que participan en los octavos de final
        List<String> equipos = new ArrayList<>();
        equipos.add("FC Barcelona");
        equipos.add("Real Madrid");
        equipos.add("Arsenal");
        equipos.add("Manchester City");
        equipos.add("Chelsea");
        equipos.add("Liverpool");
        equipos.add("PSG");
        equipos.add("Benfica");

        // Simular los octavos de final
        List<String> ganadores = octavosDeFinal(equipos);

        System.out.println("\nEquipos que avanzan a los cuartos de final:");
        for (String ganador : ganadores) {
            System.out.println(ganador);
        }
    }
}