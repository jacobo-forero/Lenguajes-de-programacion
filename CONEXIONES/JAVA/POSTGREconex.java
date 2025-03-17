import java.sql.Connection;
import java.sql.DriverManager;

public class POSTGREconex {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/";
        String user = "postgres";
        String password = "1234";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            if (conn != null) {
                System.out.println("Conexión exitosa");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
