import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MYSQLconex {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/"; 
        String usuario = "root"; 
        String contraseña = ""; 

        try {
            Connection conn = DriverManager.getConnection(url, usuario, contraseña);

            System.out.println("Conexión exitosa: " + conn);

            conn.close();
        } catch (SQLException e) {
            System.out.println("Error al conectarse a MySQL: " + e.getMessage());
        }
    }
}
