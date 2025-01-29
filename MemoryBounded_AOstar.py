from collections import defaultdict
import heapq

class AONode:
    def __init__(self, name, is_goal=False):
        self.name = name
        self.is_goal = is_goal
        self.children = []  # List of tuples (child_node, cost, is_and_node)

    def add_child(self, child, cost, is_and_node=False):
        """Add a child node with specified cost and type (AND or OR)."""
        self.children.append((child, cost, is_and_node))

class MemoryBoundedAOStar:
    def __init__(self, start_node):
        self.start_node = start_node
        self.path_costs = {start_node: 0}  # Initial path costs
        self.best_path = {}  # Stores the best path found
        self.memory_limit = 5  # Limiting the memory for demonstration

    def visualize_state(self, frontier, nodes_in_memory):
        """Helper function to print the current state of the frontier and memory."""
        print("\n--- Current State ---")
        print("Frontier:")
        for cost, _, node in frontier:
            print(f"  Node {node.name} with cumulative cost {cost}")
        print("Nodes in Memory:")
        print("  ", ", ".join(node for node in nodes_in_memory))
        print("---------------------\n")

    def ao_star(self, node):
        """Performs the memory-bounded AO* search with visualization."""
        frontier = [(0, node.name, node)]  # Include node name in tuple to avoid direct comparison
        visited = set()
        nodes_in_memory = {node.name}

        while frontier:
            # Visualize state at each iteration
            self.visualize_state(frontier, nodes_in_memory)

            cost, _, current_node = heapq.heappop(frontier)
            print(f"Processing Node: {current_node.name} (Cost: {cost})")
            visited.add(current_node.name)

            # Goal check
            if current_node.is_goal:
                print(f"Reached goal {current_node.name}\n")
                return self.extract_path(current_node)

            for child, child_cost, is_and_node in current_node.children:
                # Check if memory limit exceeded
                if len(nodes_in_memory) >= self.memory_limit:
                    removed_node = nodes_in_memory.pop()
                    print(f"Removing node {removed_node} from memory to manage memory limit")

                if is_and_node:
                    # For AND nodes, all child nodes are needed to satisfy this branch
                    sub_cost = 0
                    for sub_child, sub_child_cost, _ in child.children:
                        sub_cost += sub_child_cost
                        if sub_child.name not in visited:
                            heapq.heappush(frontier, (cost + sub_cost, sub_child.name, sub_child))
                            nodes_in_memory.add(sub_child.name)
                            visited.add(sub_child.name)
                            print(f"Adding AND-node child {sub_child.name} with cost {cost + sub_cost}")
                else:
                    # For OR nodes, only one child is needed
                    total_cost = cost + child_cost
                    if child.name not in visited:
                        heapq.heappush(frontier, (total_cost, child.name, child))
                        nodes_in_memory.add(child.name)
                        visited.add(child.name)
                        print(f"Adding OR-node child {child.name} with cost {total_cost}")

        print("No solution found within memory bounds")
        return None

    def extract_path(self, goal_node):
        """Helper to extract the path from the start node to the goal node."""
        path = []
        current = goal_node
        while current:
            path.append(current.name)
            current = self.best_path.get(current, None)
        print("Solution Path:", " -> ".join(path[::-1]))  # Reverse to get correct order
        return path[::-1]

# Define the graph
start = AONode("Start")
a = AONode("A")
b = AONode("B")
c = AONode("C")
d = AONode("D", is_goal=True)

# Construct the AND-OR graph
start.add_child(a, cost=1, is_and_node=False)
start.add_child(b, cost=2, is_and_node=True)
a.add_child(d, cost=3, is_and_node=False)
b.add_child(c, cost=1, is_and_node=True)
c.add_child(d, cost=1, is_and_node=False)

# Initialize and run the Memory-Bounded AO* algorithm
solver = MemoryBoundedAOStar(start)
solver.ao_star(start)
