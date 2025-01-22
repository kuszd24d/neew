import random
import time

def delete_system32_simulation():
    print("\nYou failed to guess the number. Initiating System32 deletion...\n")
    time.sleep(2)
    fake_files = [
        "C:\\Windows\\System32\\kernel32.dll",
        "C:\\Windows\\System32\\user32.dll",
        "C:\\Windows\\System32\\ntdll.dll",
        "C:\\Windows\\System32\\cmd.exe",
    ]
    for file in fake_files:
        print(f"Deleting {file}...")
        time.sleep(1)
    print("\nERROR: Access Denied\nSystem32 is protected.")
    print("Just kidding! Play again if you dare. 😈")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100. You have 10 attempts.\n")
    
    number_to_guess = random.randint(1, 100)
    attempts_left = 10
    
    while attempts_left > 0:
        try:
            guess = int(input(f"You have {attempts_left} attempts left. Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            if guess == number_to_guess:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly!")
                break
            elif guess < number_to_guess:
                print("Too low! The number is higher. Try again.")
            else:
                print("Too high! The number is lower. Try again.")
            
            attempts_left -= 1
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if attempts_left == 0:
        print(f"\nThe correct number was {number_to_guess}.")
        delete_system32_simulation()

if __name__ == "__main__":
    number_guessing_game()
