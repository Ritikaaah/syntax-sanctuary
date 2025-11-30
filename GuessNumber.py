import random
def guess_number():
    print("🎲 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 20.")

    number = random.randint(1,20)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! 📉 Try again.")
            elif guess > number:
                print("Too high! 📈 Try again.")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} tries!")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    guess_number()