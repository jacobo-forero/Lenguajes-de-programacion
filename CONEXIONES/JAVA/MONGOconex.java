import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;

public class MONGOconex {
    public static void main(String[] args) {
        MongoClientURI uri = new MongoClientURI("mongodb://localhost:27017");
        MongoClient mongoClient = new MongoClient(uri);

        System.out.println("Conexión exitosa");

        mongoClient.close(); 
}