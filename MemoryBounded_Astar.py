from collections import deque

class PuzzleState:
    def __init__(self, board, zero_pos, moves=0, cost=0, path=[]):
        self.board = board
        self.zero_pos = zero_pos  # Position of the empty tile (0)
        self.moves = moves  # Number of moves taken so far (g-value)
        self.cost = cost  # f = g + h (total cost)
        self.path = path  # Solution path including moves
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def get_manhattan_distance(self, goal):
        # Flatten the goal board for easier index lookup
        flat_goal = [item for row in goal for item in row]
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    target_index = flat_goal.index(self.board[i][j])
                    target_x, target_y = divmod(target_index, 3)
                    distance += abs(i - target_x) + abs(j - target_y)
        return distance

    def get_neighbors(self):
        """Generate neighboring states by moving the blank tile (0) up, down, left, or right."""
        neighbors = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Copy current board and swap 0 with target position
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, (new_x, new_y), self.moves + 1))
        
        return neighbors

    def print_board(self):
        """Helper to print the board in a readable format."""
        for row in self.board:
            print(" ".join(str(num) if num != 0 else " " for num in row))
        print()

def ida_star(initial_state, goal):
    def search(state, threshold):
        """Recursive depth-first search with a cost threshold."""
        f_cost = state.moves + state.get_manhattan_distance(goal)
        
        if f_cost > threshold:
            return f_cost
        
        if state.board == goal:
            print("\nSolution found in", state.moves, "moves!")
            for step, board in enumerate(state.path + [state.board]):
                print(f"\nStep {step}:")
                for row in board:
                    print(" ".join(str(cell) if cell != 0 else " " for cell in row))
            return None

        min_cost = float('inf')
        
        for neighbor in state.get_neighbors():
            # Convert each board in the path to a tuple for cycle checking
            path_boards = {tuple(map(tuple, b)) for b in state.path}
            if tuple(map(tuple, neighbor.board)) not in path_boards:  # Avoid cycles
                neighbor.path = state.path + [state.board]  # Update path
                neighbor_cost = search(neighbor, threshold)
                if neighbor_cost is None:
                    return None
                min_cost = min(min_cost, neighbor_cost)
        
        return min_cost

    threshold = initial_state.get_manhattan_distance(goal)
    while True:
        result = search(initial_state, threshold)
        if result is None:
            break  # Solution found
        if result == float('inf'):
            print("No solution found.")
            break
        threshold = result  # Update threshold

# Example usage
initial_board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]
goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
initial_zero_position = (1, 1)
initial_state = PuzzleState(initial_board, initial_zero_position)

ida_star(initial_state, goal_board)
