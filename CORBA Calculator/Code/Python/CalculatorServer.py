import Pyro4
from CalculatorImpl import CalculatorImpl

def main():
    try:
        # Create an instance of the CalculatorImpl class
        calculator = CalculatorImpl()
        # Create a Pyro daemon
        daemon = Pyro4.Daemon()
        # Locate the Pyro Name Server
        ns = Pyro4.locateNS()
        # Register the Calculator object with the daemon
        uri = daemon.register(calculator)
        # Register the object URI with the Pyro Name Server
        ns.register("Calculator", uri)
        # Start the Pyro event loop
        print("Calculator server is running...")
        daemon.requestLoop()
    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    main()


# If error on NameServer
# Step 1: Open a new terminal
# Step 2: python -m Pyro4.naming (keep it running)
# Step 3: Open a new terminal
# Step 4: python CalculatorServer.py