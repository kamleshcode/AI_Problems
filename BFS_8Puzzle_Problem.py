from collections import deque

class PuzzleState:
    def __init__(self, board, zero_pos, moves, path=None, move_description=None):
        self.board = board
        self.zero_pos = zero_pos
        self.moves = moves
        self.path = path if path else [(self.board, move_description)]  # Track path with descriptions

    def get_possible_moves(self):
        x, y = self.zero_pos
        possible_moves = []
        directions = {
            (-1, 0): "Move blank up",
            (1, 0): "Move blank down",
            (0, -1): "Move blank left",
            (0, 1): "Move blank right"
        }
        
        for (dx, dy), action in directions.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                # Swap zero with the target position
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                possible_moves.append((new_board, (new_x, new_y), action))
        return possible_moves

def print_board(board):
    """Helper function to print a 3x3 board in a readable format."""
    for row in board:
        print(" ".join(str(num) if num != 0 else " " for num in row))
    print("\n")

def bfs_8_puzzle(start, goal):
    start_state = PuzzleState(start, (0, 0), 0)
    queue = deque([start_state])
    visited = set()
    visited.add(tuple(map(tuple, start)))

    while queue:
        current_state = queue.popleft()

        # Check if goal is reached
        if current_state.board == goal:
            print("\nSolution Steps:")
            for i, (step_board, action) in enumerate(current_state.path):
                print(f"Step {i + 1}: {action if action else 'Start'}")
                print_board(step_board)
            print("Goal state reached!")
            return current_state.moves
        
        # Explore moves from current state
        for new_board, new_zero_pos, action in current_state.get_possible_moves():
            board_tuple = tuple(map(tuple, new_board))
            if board_tuple not in visited:
                visited.add(board_tuple)
                queue.append(PuzzleState(
                    new_board, new_zero_pos, current_state.moves + 1,
                    current_state.path + [(new_board, action)]
                ))
    
    print("No solution found.")
    return -1

# Example usage
start = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
bfs_8_puzzle(start, goal)
