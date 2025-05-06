def validate_move(move, available_moves):
    try:
        move = int(move)
        return move in available_moves
    except ValueError:
        return False

def clean_input(move):
    return move.strip()

def available_moves_generator(available_moves):
    for move in available_moves:
        yield move
