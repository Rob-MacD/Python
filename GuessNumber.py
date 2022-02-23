from math import floor
import keyboard
import random
import time
import os

maxDifficulty = 3
clear = lambda: os.system('cls')
clear()

def GuessNumber(number):
    startTime = 0
    endTime = 0
    numberOfGuesses = 0
    global maxDifficulty
    hints = 'N'
    if difficulty != 8:
        hints = input("\nWould you like hints? Yes/No (Y/N): ").upper()
    rando = random.randrange(1,number,1)
    guess = 0
    lowGuess = 1
    highGuess = number
    startTime = time.perf_counter_ns()

    while guess != rando:
        try:
            guess = int(input(f"Guess a number between {lowGuess} and {highGuess}: "))
            numberOfGuesses += 1
            if difficulty == 8:
                clear()
            if guess != rando:
                if hints == 'N':
                    print("No, try again.")
                else:
                    if guess > rando:
                        if guess < highGuess:
                            highGuess = guess
                        print(f"Your guess {guess} is too high.")
                    else:
                        if guess > lowGuess:
                            lowGuess = guess
                        print(f"Your guess {guess} is too low.")
        except ValueError:
            if difficulty == 8:
                clear()
            print("Invalid input. Try again.")
    endTime = time.perf_counter_ns()
    print("\nHEY~! YOU DID IT!")
    totalTimeNano = (endTime - startTime)
    totalTimeSeconds = totalTimeNano/1000000000
    timeSeconds = totalTimeSeconds % 60
    timeMinutes = floor((totalTimeSeconds / 60) % 60)
    timeHours = floor(totalTimeSeconds/3200)
    if timeHours > 0:
        print(f"You completed this game with {numberOfGuesses} guesses, in {timeHours} hours, {timeMinutes} minutes, and {timeSeconds:.3f} seconds.")
    elif timeMinutes > 0:
        print(f"You completed this game with {numberOfGuesses} guesses, in {timeMinutes} minutes, and {timeSeconds:.3f} seconds.")
    else:
        print(f"You completed this game with {numberOfGuesses} guesses, in {timeSeconds:.3f} seconds.")
    if difficulty == 8:
        keyboard.unblock_key('up')
    if maxDifficulty < 8 and difficulty == maxDifficulty:
        maxDifficulty = maxDifficulty + 1
        print("New difficulty unlocked!")
    with open("Leaderboard", "wb") as binary_file:
        binary_file.write(f"{name}\t{difficulty}\t{hints}\t{numberOfGuesses}\t{totalTimeNano}\n".encode('utf8'))    
    input("Press enter to return to main menu.")
    clear()
    difficulty == 10

name = input("What is your name? ")
difficulty = 10
while difficulty != 9:
    clear()
    print(f"Hello {name}! Select your difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    if maxDifficulty >= 4:
        print("4. Expert")
    if maxDifficulty >= 5:
        print("5. Champion")
    if maxDifficulty >= 6:
        print("6. Master")
    if maxDifficulty >= 7:
        print("7. Insane")
    if maxDifficulty >= 8:
        print("8. No Hope")
    try:
        difficulty = int(input(f"Select difficulty (1-{maxDifficulty}, 9 to quit): "))
    except ValueError:
        print("")
    if difficulty == 1:
        GuessNumber(10)
    if difficulty == 2:
        GuessNumber(100)
    if difficulty == 3:
        GuessNumber(1000)
    if difficulty == 4 and maxDifficulty >= 4:
        GuessNumber(10000)
    if difficulty == 5 and maxDifficulty >= 5:
        GuessNumber(100000)
    if difficulty == 6 and maxDifficulty >= 6:
        GuessNumber(1000000)
    if difficulty == 7 and maxDifficulty >= 7:
        GuessNumber(10000000)
    if difficulty == 8 and maxDifficulty >= 8:
        print("\nAre you sure? This isn't even remotely fair...")
        confirm = int(input("Press 8 again to confirm your selection: "))
        if confirm == 8:
            keyboard.block_key('up')
            clear()
            GuessNumber(1000000000)
        else:
            difficulty = 10
print("Program Complete!")