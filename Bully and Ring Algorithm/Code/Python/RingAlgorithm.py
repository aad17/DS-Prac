def main():
    # initialize the variables
    n = 0  # number of nodes
    node_ids = []  # list of node IDs
    coordinator = -1  # coordinator node ID

    # take input from user for number of nodes and node IDs
    n = int(input("Enter number of nodes: "))
    print("Enter IDs of nodes:")
    for _ in range(n):
        node_id = int(input())
        node_ids.append(node_id)

    # send messages in a ring to determine the coordinator node
    max_id = max(node_ids)

    for i in range(n):
        successor = (i + 1) % n
        print(f"Node {node_ids[i]} sends an election message to node {node_ids[successor]}")

        if node_ids[i] == max_id:
            coordinator = node_ids[i]

    # wait for the coordinator to send the coordinator message
    # while coordinator == -1:
    #     for i in range(n):
    #         predecessor = (i - 1 + n) % n
    #         successor = (i + 1) % n
    #         print(f"Node {node_ids[i]} waits for message from node {node_ids[predecessor]}")

    #         if node_ids[predecessor] == coordinator:
    #             print(f"Node {node_ids[i]} is the coordinator")
    #             coordinator = node_ids[i]
    #             break
    #         else:
    #             print(f"Node {node_ids[i]} forwards message {node_ids[predecessor]} to node {node_ids[successor]}")

    # print("Coordinator node is", coordinator)

if __name__ == '__main__':
    main()