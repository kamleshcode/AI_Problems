from tabulate import tabulate

class WaterJugDFS:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited = set()  # Stores visited states as (jug1, jug2)

    def dfs(self, jug1, jug2, depth=0, path=[]):
        if (jug1, jug2) in self.visited:
            return False  # Skip already visited states
        self.visited.add((jug1, jug2))

        # Add current state to path
        path.append([depth, "", jug1, jug2])

        if jug1 == self.target or jug2 == self.target:
            path[-1][1] = f"Target {self.target}L reached!"
            self.display_path(path)
            return True

        # Define possible actions
        actions = [
            ("Fill Jug1", self.jug1_capacity, jug2),
            ("Fill Jug2", jug1, self.jug2_capacity),
            ("Empty Jug1", 0, jug2),
            ("Empty Jug2", jug1, 0),
            ("Pour Jug1 -> Jug2", max(0, jug1 - (self.jug2_capacity - jug2)), jug2 + min(jug1, self.jug2_capacity - jug2)),
            ("Pour Jug2 -> Jug1", jug1 + min(jug2, self.jug1_capacity - jug1), max(0, jug2 - (self.jug1_capacity - jug1))),
        ]

        # Try each action in sequence
        for action, new_jug1, new_jug2 in actions:
            if (new_jug1, new_jug2) not in self.visited:
                path[-1][1] = action
                if self.dfs(new_jug1, new_jug2, depth + 1, path):
                    return True

        # Backtrack
        path.pop()
        return False

    def display_path(self, path):
        print(tabulate(path, headers=["Depth", "Action", "Jug1 (L)", "Jug2 (L)"], tablefmt="grid"))

# Example usage
jug_dfs = WaterJugDFS(4, 3, 2)
jug_dfs.dfs(0, 0)
