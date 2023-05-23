import Pyro4

def main():
    try:
        # Create a proxy for the Calculator object
        calculator = Pyro4.Proxy("PYRONAME:Calculator")
        # Get user input for the operation
        scanner = input("Enter operation (add/subtract/multiply/divide): ")
        while True:
            operation = scanner.lower()
            # Break the loop if the user enters "exit"
            if operation == "exit":
                break
            # Get user input for the numbers
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = None

            # Perform the corresponding operation based on user input
            if operation == "add":
                result = calculator.add(a, b)
            elif operation == "subtract":
                result = calculator.subtract(a, b)
            elif operation == "multiply":
                result = calculator.multiply(a, b)
            elif operation == "divide":
                try:
                    result = calculator.divide(a, b)
                except Exception as e:
                    print("Error:", str(e))
            else:
                print("Invalid operation")

            # Print the result if it is not None
            if result is not None:
                print("Result:", result)
            scanner = input()  # consume newline character
    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    main()