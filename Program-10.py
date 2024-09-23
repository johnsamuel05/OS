# Implement the concept of File allocation mechanism in windows and linux
def contiguous_memory_allocation():
    """
    Implements contiguous memory allocation.

    Returns:
        None
    """

    num_files = int(input("Enter the number of files: "))
    block_sizes = [0] * 20
    starting_blocks = [0] * 20
    file_tables = [[0] * 20 for _ in range(20)]

    for i in range(num_files):
        print(f"Enter no. of blocks occupied by file {i + 1}:", end=" ")
        block_sizes[i] = int(input())

        print(f"Enter the starting block of file {i + 1}:", end=" ")
        starting_blocks[i] = int(input())

        for j in range(block_sizes[i]):
            file_tables[i][j] = starting_blocks[i] + j

    print("Filename \t Start block \t Length")
    for i in range(num_files):
        print(f"{i + 1}\t {starting_blocks[i]}\t {block_sizes[i]}")

    file_name = int(input("Enter file name: "))
    print(f"File name is: {file_name}")
    print(f"Length is: {block_sizes[file_name - 1]}")
    print("Blocks occupied: ", end=" ")
    for i in range(block_sizes[file_name - 1]):
        print(f"{file_tables[file_name - 1][i]:4}", end=" ")


if __name__ == "__main__":
    contiguous_memory_allocation()
