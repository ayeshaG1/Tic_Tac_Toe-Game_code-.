class Board:
    def __init__(self):
        self.cells = [str(i) for i in range(1, 10)]

    def display(self):
        print("\nCurrent Board:")
        for i in range(0, 9, 3):
            print(" | ".join(self.cells[i:i+3]))
            if i < 6:
                print("-" * 11)

    def place_marker(self, position, marker):
        self.cells[position - 1] = marker

    def is_position_free(self, position):
        return self.cells[position - 1] not in ['X', 'O']

    def check_winner(self, marker):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.cells[i] == marker for i in combo) for combo in wins)

    def is_full(self):
        return all(cell in ['X', 'O'] for cell in self.cells)

    def available_positions(self):
        return [i + 1 for i, cell in enumerate(self.cells) if cell not in ['X', 'O']]
