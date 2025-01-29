from tabulate import tabulate
from collections import deque

class WaterJugBFS:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target

    def bfs(self):
        # Queue stores (jug1, jug2, depth, action_taken, path)
        queue = deque([(0, 0, 0, "Start", [])])
        visited = set()
        
        while queue:
            jug1, jug2, depth, action, path = queue.popleft()
            
            # Add the current state to the path
            current_path = path + [[depth, action, jug1, jug2]]

            # Check if we reached the target in either jug
            if jug1 == self.target or jug2 == self.target:
                self.display_path(current_path)
                return True
   
            # Mark the state as visited
            if (jug1, jug2) in visited:
                continue
            visited.add((jug1, jug2))

            # Define possible actions and new states
            actions = [
                ("Fill Jug1", self.jug1_capacity, jug2),
                ("Fill Jug2", jug1, self.jug2_capacity),
                ("Empty Jug1", 0, jug2),
                ("Empty Jug2", jug1, 0),
                ("Pour Jug1 -> Jug2", max(0, jug1 - (self.jug2_capacity - jug2)), jug2 + min(jug1, self.jug2_capacity - jug2)),
                ("Pour Jug2 -> Jug1", jug1 + min(jug2, self.jug1_capacity - jug1), max(0, jug2 - (self.jug1_capacity - jug1))),
            ]

            # Add each possible action to the queue if the resulting state hasn't been visited
            for action_name, new_jug1, new_jug2 in actions:
                if (new_jug1, new_jug2) not in visited:
                    queue.append((new_jug1, new_jug2, depth + 1, action_name, current_path))

        # If we exhaust the queue without finding the target
        print("Target not reachable")
        return False

    def display_path(self, path):
        # Display the BFS path taken to reach the solution
        print(tabulate(path, headers=["Depth", "Action", "Jug1 (L)", "Jug2 (L)"], tablefmt="grid"))

# Example usage
jug_bfs = WaterJugBFS(4, 3, 2)
jug_bfs.bfs()
