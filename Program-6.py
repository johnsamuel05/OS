#BANKERS ALGORITHM
def input_values():
    """
    Prompts the user to enter the necessary input values for the Banker's Algorithm.

    Returns:
        None
    """

    global maxi, alloc, need, avail, n, r

    print("********** Banker's Algorithm ************")
    n = int(input("Enter the number of Processes: "))
    r = int(input("Enter the number of resource instances: "))

    maxi = [[0] * r for _ in range(n)]
    alloc = [[0] * r for _ in range(n)]
    need = [[0] * r for _ in range(n)]
    avail = [0] * r

    print("Enter the Maxi Matrix:")
    for i in range(n):
        maxi[i] = list(map(int, input().split()))

    print("Enter the Allocation Matrix:")
    for i in range(n):
        alloc[i] = list(map(int, input().split()))

    print("Enter the available Resources: ")
    avail = list(map(int, input().split()))


def show():
    """
    Displays the current state of the system, including processes, allocations, maximum needs, and available resources.

    Returns:
        None
    """

    print("Process\tAllocation\tMaxi\tAvailable")
    for i in range(n):
        print(f"P{i + 1}\t", end='')
        print(*alloc[i], end='\t')
        print(*maxi[i], end='\t')
        if i == 0:
            print(*avail, end='')
        print()


def cal():
    """
    Implements the Banker's Algorithm to determine if the system is in a safe state.

    Returns:
        None
    """

    finish = [0] * n
    flag = 1
    safe = []

    for i in range(n):
        for j in range(r):
            need[i][j] = maxi[i][j] - alloc[i][j]

    while flag:
        flag = 0
        for i in range(n):
            c = 0
            for j in range(r):
                if finish[i] == 0 and need[i][j] <= avail[j]:
                    c += 1
            if c == r:
                for k in range(r):
                    avail[k] += alloc[i][j]
                finish[i] = 1
                flag = 1
                safe.append(i)

    if finish[i] == 1:
        i = n
        print(f"P{safe[-1]}", end="->")

    c1 = sum(finish)
    if c1 == n:
        print("\nThe system is in a safe state")
    else:
        print("\nProcesses are in deadlock")
        print("System is in an unsafe state")


input_values()
show()
cal()
