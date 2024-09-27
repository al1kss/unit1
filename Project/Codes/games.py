import random
from colors import *

with open("games.csv", mode='r') as f:
    data = f.readlines()
dikt = {}
for item in data:
    data_cleaned = item.strip()
    data_separated = data_cleaned.split(',')
    dikt[data_separated[0]] = int(data_separated[1])

def validate(value):
    for i in value:
        if i not in "-1234567890":
            return False
    return True

def guess_game():
    def guess_game_operation(number, hardness):
        for i in range(hardness):
            attempt = i + 1
            guess = input("Enter your guess: ")
            if validate(guess):
                guess = int(guess)
                if guess == number:
                    print(f"{green}You guessed it!{end_code}")
                    print(
                        f"{blue}You took {yellow}{attempt}{blue} attempts. You get {green}{dikt['Guess a number'] * 5 if attempt < hardness - 2 else dikt['Guess a number'] * 2}$")
                    return dikt['Guess a number'] * 5 if attempt < hardness - 2 else dikt[
                                                                                         'Guess a number'] * 2  # Return the points gained
                elif guess > number:
                    print(f"{LIGHT_PURPLE}It is lower than {guess}{end_code}")
                elif guess < number:
                    print(f"{LIGHT_PURPLE}It is higher than {guess}{end_code}")
            else:
                print(f"{red}Invalid input{end_code}")
                continue

        print(f"{red}Nope, it was {number}{end_code}")
        print(f"{red}Better luck next time!{end_code}")
        return 0  # Return 0 points if all attempts are used


    level = input("Enter the level of difficulty [easy, medium, hard]: ").lower()
    if level == "easy":
        number = random.randint(1, 10)
        print("I'm thinking of a number between 1 and 10.")
        return guess_game_operation(number,3)

    elif level == "medium":
        number = random.randint(1, 20)
        print("I'm thinking of a number between 1 and 20.")
        return guess_game_operation(number, 5)

    elif level == "hard":
        number = random.randint(1, 50)
        print("I'm thinking of a number between 1 and 50.")
        return guess_game_operation(number,7)
    else:
        print(f"{red}Invalid level{end_code}")
        return 0

def tic_tac_toe():
    tic = """
                  ___         __     ___        __     _____    
                 <  /        / /    |__ \      / /    |__  /    
                 / /        / /     __/ /     / /      /_ <     
                / /        / /     / __/     / /     ___/ /     
               /_/        / /     /____/    / /     /____/      
    _____________________/_/_______________/_/__________________
   /_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/
           / // /      / /    / ____/    / /    / ___/          
          / // /_     / /    /___ \     / /    / __ \           
         /__  __/    / /    ____/ /    / /    / /_/ /           
           /_/      / /    /_____/    / /     \____/            
    _______________/_/_______________/_/__________________      
   /_____/_____/_____/_____/_____/_____/_____/_____/_____/      
        /__  /   / /    ( __ )     / /    / __ \                
          / /   / /    / __  |    / /    / /_/ /                
         / /   / /    / /_/ /    / /     \__, /                 
        /_/   / /     \____/    / /     /____/                  
             /_/               /_/                              
    """
    print(blue + tic + end_code)
    board = [" " for i in range(9)]
    def print_board():
        print(f"{green}-------------")
        for i in range(3):
            print(f"{green}| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
            print(f"-------------{end_code}")
    def check_winner():
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != " ":
                return True
            if board[i*3] == board[i*3+1] == board[i*3+2] != " ":
                return True
        if board[0] == board[4] == board[8] != " ":
            return True
        if board[2] == board[4] == board[6] != " ":
            return True
        return False
    def check_draw():
        return " " not in board
    def play_game():
        player = f"{red}X{green}" # Player X always starts
        while True:
            print_board()
            move = input(f"{LIGHT_PURPLE}Enter your move (1-9): ")
            if validate(move):
                move = int(move)
                move -= 1
                if board[move] == " ":
                    board[move] = player
                    if check_winner():
                        print_board()
                        print(f"{green}{player} wins!{end_code}")
                        return 1
                    if check_draw():
                        print_board()
                        print(f"{yellow}It's a draw!{end_code}")
                        return 0
                    player = f"{blue}O{green}" if player == f"{red}X{green}" else f"{red}X{green}"
                else:
                    print(f"{red}Invalid move{end_code}")
            else:
                print(f"{red}Invalid input{end_code}")
                print(f"{blue}Input like of 1 2 3 / 4 5 6 / 7 8 9{end_code}")
    if play_game() == 1:
        return dikt['Tic-Tac-Toe']
    else:
        return 0 # Return 0 points

def word_scramble():
    with open("word_scramble.txt", "r") as file:
        words = file.readlines()

    catalogue = []
    for word in words:
        catalogue.append(word.strip())
    word = random.choice(catalogue)

    def play():
        attempt = 0
        word_list = list(word)
        random.shuffle(word_list)
        scrambled_word = ""
        for char in word_list:
            scrambled_word += char

        while True:
            attempt += 1
            print(f"{cyan}Unscramble the word: {scrambled_word}{end_code}")
            guess = input(f"{LIGHT_PURPLE}Enter your guess: {end_code}").lower()

            if guess == word.lower():
                print(f"{green}You guessed it!{end_code}")
                print(f"{yellow}It took you {attempt} attempts{end_code}")
                print(f"{yellow}You earned: {green}${dikt['Word Scramble'] * 2 if attempt <= 3 else dikt['Word Scramble']}{end_code}")
                return (dikt['Word Scramble'] * 2) if attempt <= 3 else dikt['Word Scramble']
            else:
                print(f"{red}Nope, try again{end_code}")

    return play()

def rock_paper_scissors():
    def play():
        total = 0
        k = True
        while k:
            player = input(f"\n{blue}Enter your choice [rock (r), paper (p), scissors (s), X - to {red}leave{blue}]: {end_code}").lower()
            var = ["rock", "paper", "scissors"]
            var_short = ["r", "p", "s"]
            y = random.randint(0, 2)
            computer = var[y]
            comp_short = var_short[y]
            if player == "x":
                k = False
                print(f"{red}You left the game{end_code}")
                break

            print(f"{yellow}Computer chose: {LIGHT_PURPLE}{computer}{end_code}")

            if player == computer or player == comp_short:
                print(f"{yellow}It's a draw!{end_code}")

            elif player == "rock" or player == "r":
                if computer == "paper" or computer == "p":
                    print(f"{red}You lose!{end_code}")
                else:
                    print(f"{green}You win!{end_code}")
                    total += dikt['Rock Paper Scissors']
            elif player == "paper" or player == "p":
                if computer == "rock" or computer == "r":
                    print(f"{green}You win!{end_code}")
                    total += dikt['Rock Paper Scissors']
                else:
                    print(f"{red}You lose!{end_code}")
            elif player == "scissors" or player == "s":
                if computer == "rock" or computer == "r":
                    print(f"{red}You lose!{end_code}")
                else:
                    print(f"{green}You win!{end_code}")
                    total += dikt['Rock Paper Scissors']
            else:
                print(f"{red}Invalid choice{end_code}")
            print(f"{yellow}You earned: {green}${total}{end_code}")
        return total
    return play()