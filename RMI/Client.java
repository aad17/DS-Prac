import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    public static void main(String[] args) {
        try {
            // Get the reference to the remote server object
            Registry registry = LocateRegistry.getRegistry("localhost");
            ServerInterface server = (ServerInterface) registry.lookup("Server");

            // Get data from the user
            int data = Integer.parseInt(System.console().readLine("Enter data to send to the server: "));

            // Call the remote method on the server and get the result
            int result = server.processData(data);

            // Print the result
            System.out.println("Server returned: " + result);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
