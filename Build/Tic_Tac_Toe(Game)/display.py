def show_welcome(player1_name, player2_name):
    print(f"\n🎮 Welcome, {player1_name} and {player2_name}! Let's play Tic-Tac-Toe!\n")

def show_board(cells):
    print("\nCurrent Board:")
    for i in range(0, 9, 3):
        print(" | ".join(cells[i:i+3]))
        if i < 6:
            print("-" * 11)

def show_winner(player_name):
    print(f"\n🏆 Congratulations, {player_name}! You win!")

def show_draw():
    print("\n🤝 It's a draw!")

def ask_replay():
    return input("Would you like to play again? (yes/no): ").lower().strip()
