#page replacement algorithm
def fifo_page_replacement(page_references, num_frames):
    """
    Implements the First-In-First-Out (FIFO) page replacement algorithm.

    Args:
        page_references: A list of integers representing the page references.
        num_frames: The number of frames available.

    Returns:
        None
    """

    num_pages = len(page_references)
    frames = [-1] * num_frames
    j = 0
    page_faults = 0

    print("\t Ref string \t page frames")
    for i in range(num_pages):
        print(f"{page_references[i]}\t", end=" ")

        found = False
        for k in range(num_frames):
            if frames[k] == page_references[i]:
                found = True
                break

        if not found:
            frames[j] = page_references[i]
            j = (j + 1) % num_frames
            page_faults += 1

        for k in range(num_frames):
            if frames[k] != -1:
                print(f"{frames[k]}\t", end=" ")
            else:
                print("-\t", end=" ")
        print()

    print(f'Page faults: {page_faults}')


if __name__ == "__main__":
    num_pages = int(input("Enter the number of pages: "))
    page_references = list(map(int, input("Enter the page numbers: ").split()))
    num_frames = int(input("Enter the number of frames: "))

    fifo_page_replacement(page_references, num_frames)
