#0. prompt players for their names
#1. Prompt player 1 for rps
#2. prompt player 2 for rps
#3. compare player 1 and player 2 choices and decide a winner

def RPS():
    print("Welcome to Rock Paper Scissors!")

#gather player names
    player1 = input("Player 1 please enter your name")
    player2 = input("Player 2 please enter your name")

# gather choices 
    choice1 = input(f"{player1}, Enter your choice.... rock, paper, or scissors: ").lower()
    choice2 = input(f"{player2}, Enter your choice.... rock, paper, or scissors: ").lower()

    while not IsValidMove(choice1):
        print("Invalid move! Try again")
        choice1 = input(f"{player1}, Enter your choice.... rock, paper, or scissors: ").lower()

    while not IsValidMove(choice2):
        print("Invalid move! Try again")
        choice2 = input(f"{player2}, Enter your choice.... rock, paper, or scissors: ").lower()

    
    if choice1 == choice2:
        print("It's a tie...")
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "paper" and choice2 == "rock") or \
         (choice1 == "scissors" and choice2 == "paper"):
        print(f"{player1} Wins!!")
    else:
        print(f"{player2} Wins!!")

def IsValidMove(playerMove):
    validMoves = ["rock" , "paper", "scissors"]

    if playerMove in validMoves:
        return True
    else: 
        return False


   
RPS()