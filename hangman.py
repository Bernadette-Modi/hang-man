from words import categories
import random
hangman_art =  {0:("   ",
                   "   ",
                   "   "), 
                1:(" O ",
                   "   ",
                   "   "), 
                2:(" O ",
                   " | ",
                   "   "), 
                3:(" O ",
                   "/| ",
                   "   "),
                4:(" O ",
                   "/|\\ ",
                   "   "),
                5:(" O ",
                   "/|\\ ",
                   "/   "),
                6:(" O ",
                   "/|\\ ",
                   "/ \\ "), }


def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line) 
    print("**********")
def display_hint(hint):
    print(" ".join(hint))

def display_clue(category_name, word):
    clue = categories[category_name].get(word, "No clue available.")
    return clue

def display_answer(answer):
    print(" ".join(answer)) 


def main(): 
    category_name = random.choice(list(categories.keys()))
    answer = random.choice(list(categories[category_name].keys())) 
    clue = display_clue(category_name, answer)
    print(f"category: {category_name}")
    print(f"Clue: {clue}")
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    while is_running: 
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)

        if guess in answer: 
            for i in range(len(answer)):
                if answer[i] == guess: 
                    hint[i]= guess
        else: 
            wrong_guesses += 1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU Win!") 
            is_running = False 
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")    
            is_running = False    

if __name__ == "__main__":
    main()