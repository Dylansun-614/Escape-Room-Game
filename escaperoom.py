import random

def play_lock(level, max_attempts=5):
    secret = random.randint(1, 20)
    print(f"\nLock {level}: Guess the number between 1 and 20. You have {max_attempts} attempts.")

    attempts = 0
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}: ")
        if not guess.strip().isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! Lock {level} is now open.")
            return True

    print(f"You failed to unlock Lock {level} in time.")
    return False

def main():
    print("Welcome to the Number Lock Escape Room!")
    print("You need to unlock 3 number locks to escape.\n")

    for i in range(1, 4):
        success = play_lock(i)
        if not success:
            print("\nGame Over! You're trapped in the room...")
            return

    print("\nCongratulations! You unlocked all the locks and escaped the room!")

if __name__ == "__main__":
    main()
