from pathlib import Path
from game.board import Board
from game.players import Player
from game.utils import validate_move, clean_input, available_moves_generator
from tools.display import show_welcome, show_board, show_winner, show_draw, ask_replay
from tools.logger import Logger

def start_game():
    game_number = len(list(Path("tic_tac_toe/game_log").glob("game*"))) + 1
    logger = Logger(game_number)

    # Get player names
    player1_name = input("Please enter Player 1 name: ")
    player2_name = input("Please enter Player 2 name: ")

    # Create player objects
    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")
    players = [player1, player2]

    show_welcome(player1_name, player2_name)

    # Initialize the board
    board = Board()
    move_number = 1
    current_player_index = 0

    # Game loop
    while True:
        show_board(board.cells)

        current_player = players[current_player_index]
        available_moves = board.available_positions()

        # Get and validate move
        move = None
        while move not in available_moves:
            move = current_player.get_move(available_moves)

        # Place marker and log move
        board.place_marker(move, current_player.marker)
        logger.log_move(move_number, current_player.name, move, board.cells)
        move_number += 1

        # Check for win or draw
        if board.check_winner(current_player.marker):
            show_board(board.cells)
            show_winner(current_player.name)
            logger.log_result(f"{current_player.name} wins!")
            break
        elif board.is_full():
            show_board(board.cells)
            show_draw()
            logger.log_result("Draw")
            break

        # Alternate turns
        current_player_index = 1 - current_player_index

    # Ask if players want to play again
    if ask_replay() == "yes":
        start_game()

if __name__ == "__main__":
    start_game()

