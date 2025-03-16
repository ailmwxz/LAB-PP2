import random
def number_game():
    random.randint(1,20)
    name=input("Hello! What is your name?\n")
    guess=0
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    for i in range(1,20):
        san=int(input("\nTake a guess\n"))
        guess +=1
        if san<i:
            print("Your guess is too low.")
        elif san>i:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name} You guessed my number in {guess} guesses!")
            break
number_game()
