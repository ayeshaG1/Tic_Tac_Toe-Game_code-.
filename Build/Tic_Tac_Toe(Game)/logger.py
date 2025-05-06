from pathlib import Path
import datetime

class Logger:
    def __init__(self, game_number):
        self.game_number = game_number
        self.game_log_dir = Path(f"tic_tac_toe/game_log/game{game_number}")
        self.game_log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.game_log_dir / "log.txt"

    def log_move(self, move_number, player_name, move, board_state):
        with open(self.log_file, "a") as f:
            f.write(f"Move {move_number}: {player_name} -> Position {move}\n")
            f.write("Board After Move:\n")
            self._write_board(f, board_state)
            f.write("\n")

    def log_result(self, result):
        with open(self.log_file, "a") as f:
            f.write(f"Result: {result}\n")

    def _write_board(self, file, board_state):
        for i in range(0, 9, 3):
            file.write(" | ".join(board_state[i:i+3]) + "\n")
            if i < 6:
                file.write("-" * 11 + "\n")
