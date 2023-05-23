import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server implements ServerInterface {

    public static void main(String[] args) {
        try {
            // Create an instance of the server
            Server server = new Server();

            // Export the server object
            ServerInterface stub = (ServerInterface) UnicastRemoteObject.exportObject(server, 0);

            // Bind the server object to the registry
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.bind("Server", stub);

            System.out.println("Server started.");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }

    @Override
    public int processData(int data) throws RemoteException {
        // Process the data
        int result = data * 2;
        return result;
    }
}
