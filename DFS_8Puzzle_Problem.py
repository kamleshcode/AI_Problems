class PuzzleState:
    def __init__(self, board, zero_pos, moves, path=None):
        self.board = board
        self.zero_pos = zero_pos
        self.moves = moves
        self.path = path if path else [board]  # Track the path of board states

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def display_board(self):
        """Display the board in a readable 3x3 format."""
        for i in range(0, 9, 3):
            print(self.board[i:i + 3])
        print()

    def get_neighbors(self):
        neighbors = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = self.board[:]
                # Swap zero with the target position
                new_board[x * 3 + y], new_board[new_x * 3 + new_y] = new_board[new_x * 3 + new_y], new_board[x * 3 + y]
                neighbors.append(PuzzleState(new_board, (new_x, new_y), self.moves + 1, self.path + [new_board]))
        
        return neighbors

def dfs(initial_state):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()

        # Display the board at each state
        print(f"Move {current_state.moves}:")
        current_state.display_board()

        if current_state.is_goal():
            print("Goal state reached in", current_state.moves, "moves!")
            print("\nSolution Path:")
            for i, board in enumerate(current_state.path):
                print(f"Step {i + 1}:")
                for j in range(0, 9, 3):
                    print(board[j:j + 3])
                print()
            return current_state.moves
        
        visited.add(tuple(current_state.board))
        
        # Add neighbors to stack
        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in visited:
                stack.append(neighbor)

    print("No solution found.")
    return -1

# Example usage
if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    zero_position = (2, 0)
    initial_state = PuzzleState(initial_board, zero_position, 0)
    
    print("Starting DFS to solve 8-puzzle problem:\n")
    result = dfs(initial_state)
    print("\nNumber of moves to solve the puzzle:", result)
