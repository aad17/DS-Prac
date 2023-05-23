def calculate_average_clock_time(server_clocks):
    total_clock_time = sum(server_clocks)
    return total_clock_time // len(server_clocks)

def main():
    # Simulating the clock time for each server
    server_clocks = []
    n = int(input('Enter the number of servers: \n'))
    for i in range(n):
        server_clocks.append(int(input(f'Enter the clock time for the server {i}: ')))
    average_clock_time = calculate_average_clock_time(server_clocks)

    # Adjusting clock time for each server based on the average clock time
    for i in range(len(server_clocks)):
        time_difference = average_clock_time - server_clocks[i]
        server_clocks[i] += time_difference
        print(f"Server {i} clock time adjusted by {time_difference} seconds")

    print("Final clock times for servers:", server_clocks)

if __name__ == '__main__':
    main()