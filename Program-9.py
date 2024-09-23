#disk scheduling algorithm
def scan_disk_scheduling(disk_size, queue_size, queue, initial_head_position):
    """
    Implements the SCAN disk scheduling algorithm.

    Args:
        disk_size: The maximum range of the disk.
        queue_size: The size of the queue of disk requests.
        queue: A list of integers representing the disk positions to be read.
        initial_head_position: The initial position of the disk head.

    Returns:
        None
    """

    queue.insert(0, initial_head_position)
    queue.sort()

    seek_time = 0
    direction = 1  # 1 for moving towards the right, -1 for moving towards the left

    for i in range(queue_size):
        seek_time += abs(queue[i + 1] - queue[i])
        print(f"Disk head moves from {queue[i]} to {queue[i + 1]} with seek {abs(queue[i + 1] - queue[i])}")

    print(f"Total seek time is {seek_time}")
    average_seek_time = seek_time / float(queue_size)
    print(f"Average seek time is {average_seek_time}")


if __name__ == "__main__":
    disk_size = int(input("Enter the max range of the disk: "))
    queue_size = int(input("Enter the size of queue requests: "))
    queue = []
    print("Enter the queue of disk positions to be read: ")
    for i in range(queue_size):
        queue.append(int(input()))

    initial_head_position = int(input("Enter the initial head position: "))

    scan_disk_scheduling(disk_size, queue_size, queue, initial_head_position)
