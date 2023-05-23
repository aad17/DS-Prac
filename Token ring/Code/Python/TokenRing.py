class TokenRing:

    def main(self):
        print("Enter the number of nodes:")
        n = int(input())  # Get the number of nodes from the user
        m = n - 1  # Calculate the maximum value for the token
        token = 0  # Initialize the token to 0
        ch = 0  # Initialize the choice variable to 0
        flag = 0  # Initialize the flag variable to 0

        for i in range(n):
            print(" " + str(i), end="")
        print(" 0")  # Print the nodes' IDs, including 0, as a reference

        while True:
            print("Enter sender:")
            s = int(input())  # Get the sender's ID from the user
            print("Enter receiver:")
            r = int(input())  # Get the receiver's ID from the user
            print("Enter Data:")
            a = input()  # Get the data to be sent from the user
            print("Token passing:", end="")
            i = token
            j = token

            # Print the path of the token until it reaches the sender's ID
            while (i % n) != s:
                print(" " + str(j) + "->", end="")
                i += 1
                j = (j + 1) % n

            print(" " + str(s))  # Print the sender's ID
            print(f'Sender {s} sending data {a}')  # Print the sender and the data being sent

            i = (s + 1) % n
            while i != r:
                print("data " + str(a) + " forwarded by " + str(i))  # Print the intermediate nodes forwarding the data
                i = (i + 1) % n

            print("Receiver " + str(r) + " received data: " + str(a) + "\n")  # Print the receiver's ID and the received data
            token = s  # Update the token to the sender's ID

            while True:
                try:
                    if flag == 1:
                        print("Invalid Input!!...")
                    print("Do you want to send again? Enter 1 for Yes and 0 for No: ", end="")
                    ch = int(input())  # Get the user's choice to send again or not
                    if ch != 1 and ch != 0:
                        flag = 1
                    else:
                        flag = 0
                    break
                except ValueError:
                    print("Invalid Input")

            if ch != 1:
                break

if __name__ == "__main__":
    token_ring = TokenRing()
    token_ring.main()
