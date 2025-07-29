# Python/Week5/rps_class.py

class RPSGame:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""

    def is_valid_move(self, move):
        return move in ["rock", "paper", "scissors"]

    def get_choice(self, player_name):
        choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
        while not self.is_valid_move(choice):
            print("Invalid move! Try again.")
            choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
        return choice

    def play(self):
        print("Welcome to Rock Paper Scissors!")
        self.player1 = input("Player 1, please enter your name: ")
        self.player2 = input("Player 2, please enter your name: ")

        choice1 = self.get_choice(self.player1)
        choice2 = self.get_choice(self.player2)

        if choice1 == choice2:
            print("It's a tie...")
        elif (choice1 == "rock" and choice2 == "scissors") or \
             (choice1 == "paper" and choice2 == "rock") or \
             (choice1 == "scissors" and choice2 == "paper"):
            print(f"{self.player1} Wins!!")
        else:
            print(f"{self.player2} Wins!!")
