
# Simple code
# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n - 1, auxiliary, target, source)

# # Number of disks
# n = 3
# tower_of_hanoi(n, 'A', 'C', 'B')

# -----------------------------------------OR----------------------------------------


def move_disk(from_rod, to_rod, rods):
    """Move the top disk from one rod to another and display the current state."""
    disk = rods[from_rod].pop()  # Remove the top disk from from_rod
    rods[to_rod].append(disk)    # Place it on to_rod
    print(f"Move disk {disk} from {from_rod} to {to_rod}")
    display_rods(rods)

def display_rods(rods):
    """Print the current state of each rod in a readable format."""
    for rod, disks in rods.items():
        print(f"{rod}: {' '.join(map(str, disks)) if disks else 'Empty'}")
    print("-" * 20)  # Separator for each step

def tower_of_hanoi(n, source, destination, auxiliary, rods):
    """Recursive Tower of Hanoi function with visualization."""
    if n == 1:
        move_disk(source, destination, rods)
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination, rods)
    # Move nth disk from source to destination
    move_disk(source, destination, rods)
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source, rods)

# Example usage
num_disks = 3
# Initialize rods with all disks on 'A' in descending order (largest disk at the bottom)
rods = {'A': list(range(num_disks, 0, -1)), 'B': [], 'C': []}

print(f"Solving Tower of Hanoi with {num_disks} disks:\n")
display_rods(rods)
tower_of_hanoi(num_disks, 'A', 'C', 'B', rods)
