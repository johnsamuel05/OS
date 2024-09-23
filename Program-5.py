def fcfs(processes):
    """
    Implements the First-Come-First-Served (FCFS) scheduling algorithm.

    Args:
        processes: A list of tuples, where each tuple represents a process.
                   Each tuple contains two elements: the arrival time and the burst time.

    Returns:
        None
    """

    num_processes = len(processes)
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes

    for i in range(1, num_processes):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1] - processes[i][0]
        if waiting_time[i] < 0:
            waiting_time[i] = 0

    for i in range(num_processes):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    average_waiting_time = sum(waiting_time) / num_processes
    average_turnaround_time = sum(turnaround_time) / num_processes

    print("Process\t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time")
    for i in range(num_processes):
        print(f"P{i}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\n Average Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


if __name__ == "__main__":
    processes = [(0, 5), (1, 3), (2, 8), (4, 6)]
    fcfs(processes)
