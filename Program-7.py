#Memory Allocation Algorithm
def first_fit(block_sizes, memory_blocks, process_sizes, num_processes):
    """
    Implements the First-Fit memory allocation algorithm.

    Args:
        block_sizes: A list of integers representing the sizes of the memory blocks.
        memory_blocks: The total number of memory blocks.
        process_sizes: A list of integers representing the sizes of the processes.
        num_processes: The total number of processes.

    Returns:
        None
    """

    allocation = [-1] * num_processes

    for i in range(num_processes):
        for j in range(memory_blocks):
            if block_sizes[j] >= process_sizes[i]:
                allocation[i] = j
                block_sizes[j] -= process_sizes[i]
                break

    print("Process No.\tProcess Size\tBlock no.")
    for i in range(num_processes):
        print(f"  {i + 1}\t\t{process_sizes[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


if __name__ == "__main__":
    memory_blocks = int(input("Enter the number of memory blocks: "))
    block_sizes = []
    for i in range(memory_blocks):
        size = int(input(f"Enter size of memory block {i + 1}: "))
        block_sizes.append(size)

    num_processes = int(input("Enter the number of processes: "))
    process_sizes = []
    for i in range(num_processes):
        size = int(input(f"Enter size of process {i + 1}: "))
        process_sizes.append(size)

    first_fit(block_sizes, memory_blocks, process_sizes, num_processes)
