import random
import time

# game statistics
games_played = 0
wins = 0
high_score = None
best_player = " "

#aSCII art for the game
def show_banner():
    print("=" * 50)
    print("WELCOME TO CIPHER QUEST!")
    print("=" * 50)

#player name
def get_player_name():
    name = input("Enter your name, adventurer: ")
    return name.strip() or "Anonymous"

#difficulty selection
def choose_level():
    print("\nChoose your difficulty level:")
    print("1. Easy (3 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (7 attempts)")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 3
        elif choice == "2":
            return 5
        elif choice == "3":
            return 7
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

#secret hints
def give_secret_hint(secret):
    print("\n Secret Hint:")
    if secret % 2 == 0:
        print("The secret number is even.")
    else:
        print("The secret number is odd.")
    if secret % 5 == 0:
        print("The secret number is a multiple of 5.")
    if secret > 50:
        print("The secret number is greater than 50.")
    else:
        print("The secret number is 50 or less.")

# input validation:
def get_valid_guess(max_number):
    while True:
        try:
            guess = int(input(f"Enter your guess: "))
            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}")
            else:
                return guess
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

#Range hints
def range_hint(secret, guess):
    difference = abs(secret - guess)
    if difference <= 3:
        print("You're extremely close!")
    elif difference <= 10:
        print("You're close!")
    elif difference <= 20:
        print("You're somewhat close.")
    else:
        print("You're far away.")

#Timer challenge
def timer_left(start_time, limit):
    elapsed = int(time.time() - start_time)
    remaining = limit - elapsed
    return remaining

#Game function
def play_game(player_name):
    global wins
    global high_score
    global best_player

    level, max_number, attempt_limit, points = choose_level()
    print(f"\n Hello {player_name}! Good luck!")
    print(f"I have guessed a number between 1 and {max_number}. Can you guess it?")
    print(f"You have {attempt_limit} attempts")
    print("You have 30 seconds to win!")
    secret_number = random.randint(1, max_number)
    give_secret_hint(secret_number)
    attempts = 0
    start_time = time.time()
    while True:
        remaining_time = timer_left(start_time, 30)
        if remaining_time <= 0:
            print("\n Time over")
            print(f"The secret number was: {secret_number}")
            return False
        print(f"\n Time remaining: {remaining_time} seconds")
        print(f"Attempts left: {attempt_limit - attempts}")
        guess = get_valid_guess(max_number)
        attempts += 1
    if guess == secret:
        print("YAY! You have guessed the number!")
        print("You have guessed the number in", attempts, "attempts!")
        print("Your score is:", points)
        wins += 1
        if high_score is None or attempts < high_score:
            high_score = attempts
            best_player = player_name
        return True
    elif guess > secret:
        print("Too high! Try again.")
        range_hint(secret, guess)
    else:
        print("Too low! Try again.")
        range_hint(secret, guess)
    if attempts == attempt_limit:
        print("\n You've used all your attempts!")
        print(f"The secret number was: {secret_number}")
        return False
    
#Multiplayer mode
def multiplayer_mode():
    print("\nMultiplayer Mode")
    setter = input("Player 1 name: ")
    guesser = input("Player 2 name: ")
    print(f"\n{setter} vs {guesser} - Let the battle begin!")
    max_number = 100
    while True:
        try:
            secret = int(input(f"{setter}, enter a secret number between 1 and 100: "))
            if 1 <= secret <= 100:
                break
            else:
                print(f"Please enter a number between 1 and 100")
        except:
            print("Numbers only")

    print("\n" * 50)  # Clear the screen
    attempts = 0
    while True:
        guess = get_valid_guess(max_number)
        attempts += 1
        if guess == secret:
            print(f"Congratulations {guesser}! You've guessed the number in {attempts} attempts!")
            break
        elif guess > secret:
            print("Too high! Try again.")
            
        else:
            print("Too low! Try again.")

#Statistics screen
def show_statistics():
    print("\nGame Statistics:")
    print("-" * 40)
    print("Games played:", games_played)
    print("Wins:", wins)

    if games_played > 0:
        accuray = (wins / games_played) * 100
        print(f"Accuracy: {accuray:.2f}%")
    if high_score is not None:
        print("Best score:", high_score, "attempts")
        print("Best player:", best_player)

#Main game loop
def main():
    global games_played
    show_banner()
    player_name = get_player_name()
    while True:
        print("\nMain Menu:")
        print("1. Play Game")
        print("2. Multiplayer Mode")
        print("3. View Statistics")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            games_played += 1
            play_game(player_name)
        elif choice == "2":
            multiplayer_mode()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            print("Thanks for playing Cipher Quest!")
            break
        else:
            print("Invalid choice.")
            
#Start game
main()