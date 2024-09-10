class MinMaxGame:
    def __init__(self, red_marbles, blue_marbles):
        self.red_marbles = red_marbles
        self.blue_marbles = blue_marbles

    def is_terminal(self):
        return self.red_marbles <= 0 or self.blue_marbles <= 0

    def evaluate(self):
        # Customize evaluation function if needed
        return self.red_marbles * 2 + self.blue_marbles * 3

    def get_possible_moves(self, version):
        if version == "standard":
            return [
                (2, 2),  # Pick 2 red marbles and 2 blue marbles
                (1, 1),  # Pick 1 red marble and 1 blue marble
                (2, 0),  # Pick 2 red marbles
                (0, 2),  # Pick 2 blue marbles
            ]
        elif version == "misere":
            return [
                (0, 2),  # Pick 2 blue marbles
                (0, 1),  # Pick 1 blue marble
                (2, 0),  # Pick 2 red marbles
                (1, 0),  # Pick 1 red marble
            ]
        else:
            return []  # Handle unexpected versions

    def apply_move(self, move):
        r, b = move
        if r > self.red_marbles or b > self.blue_marbles:
            return None  # Invalid move
        return MinMaxGame(self.red_marbles - r, self.blue_marbles - b)

    def minmax(self, depth, alpha, beta, is_maximizing_player, version):
        if self.is_terminal():
            if is_maximizing_player:
                return -self.evaluate()  # Minimizer's perspective
            else:
                return self.evaluate()  # Maximizer's perspective

        if depth == 0:
            return self.evaluate()  # Base case for depth limit

        best_value = float('-inf') if is_maximizing_player else float('inf')
        for move in self.get_possible_moves(version):
            next_state = self.apply_move(move)
            if next_state is None:
                continue  # Skip invalid moves
            value = next_state.minmax(depth - 1, alpha, beta, not is_maximizing_player, version)

            if is_maximizing_player:
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)
            else:
                best_value = min(best_value, value)
                beta = min(beta, best_value)

            if beta <= alpha:
                break  # Beta cutoff

        return best_value

    def best_move(self, depth, version):
        best_value = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        for move in self.get_possible_moves(version):
            next_state = self.apply_move(move)
            if next_state is None:
                continue  # Skip invalid moves
            move_value = next_state.minmax(depth - 1, alpha, beta, False, version)

            if move_value > best_value:
                best_value = move_value
                best_move = move

            alpha = max(alpha, best_value)
            if beta <= alpha:
                break

        return best_move

def play_game(version):
    game = MinMaxGame(10, 10)  # Starting with 10 red and 10 blue marbles
    depth = 3  # Depth of search for MinMax algorithm

    player_turn = True  # Start with the player's turn

    while not game.is_terminal():
        print(f"Current game state: Red marbles: {game.red_marbles}, Blue marbles: {game.blue_marbles}")
        if player_turn:
            possible_moves = game.get_possible_moves(version)
            print("Possible moves (red, blue):", possible_moves)
            move = input("Enter your move (format: red blue): ").strip().split()
            if len(move) != 2:
                print("Invalid input format. Use 'red blue' format.")
                continue
            
            try:
                move = (int(move[0]), int(move[1]))
                if move not in possible_moves:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Enter integers for red and blue marbles.")
                continue

            next_game = game.apply_move(move)
            if next_game is None:
                print("Invalid move applied. Exiting.")
                break
            game = next_game
        else:
            move = game.best_move(depth, version)
            print(f"AI plays: {move}")
            next_game = game.apply_move(move)
            if next_game is None:
                print("AI made an invalid move. Exiting.")
                break
            game = next_game

        player_turn = not player_turn  # Switch turns

    print("Game Over!")
    
    # Determine and print the result
    if game.red_marbles <= 0:
        if game.blue_marbles <= 0:
            print("It's a draw!")
        else:
            if not player_turn:
                print("AI wins!")
            else:
                print("Player wins!")
    elif game.blue_marbles <= 0:
        if not player_turn:
            print("AI wins!")
        else:
            print("Player wins!")
    else:
        print("Unexpected end state.")

    print("Final Score:", game.evaluate())

def main():
    version = input("Enter game version (standard/misere): ").strip().lower()
    if version not in ["standard", "misere"]:
        print("Invalid version selected. Please enter 'standard' or 'misere'.")
        return

    print(f"Playing {version.capitalize()} Version:")
    play_game(version)

if __name__ == "__main__":
    main()
