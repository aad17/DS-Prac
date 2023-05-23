def initiate_election(processes, initiating_process):
    coordinator = initiating_process

    # Iterate over the processes with higher IDs
    for i in range(initiating_process + 1, len(processes)):
        if processes[i] > coordinator:
            print(f"Process {initiating_process} sends message to process {i}")
            if send_message(i):
                print(f"Process {i} responded to process {initiating_process}")
                coordinator = i

    # Iterate over the processes with lower IDs
    for i in range(initiating_process):
        print(f"Process {initiating_process} sends message to process {i}")
        if send_message(i):
            print(f"Process {i} responded to process {initiating_process}")
            coordinator = i

    return coordinator

def send_message(process):
    # Simulating message sending and receiving
    return True

def main():
    n = int(input("Enter the number of processes: "))
    processes = []

    print("Enter the process IDs:")
    for _ in range(n):
        process_id = int(input())
        processes.append(process_id)

    initiating_process = int(input("Enter the process ID initiating the election: "))
    print("Election initiated by process", initiating_process)
    coordinator = initiate_election(processes, initiating_process)
    print("Coordinator process is", coordinator)

if __name__ == '__main__':
    main()