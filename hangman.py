import random
def database():
    data=['hangman','python','codealpha','programming','software','internship','gaming']
    return  random.choice(data)

def current_word_state(word,letters):
     
     return ' '.join(alpa if alpa in letters else '_' for alpa in word)

def game():
     word=database()
     letters_guessed =set()
     wrong_guesses=0
     max_wrong_guesses=5


     print("Welcome to Hangman:)!")
     print()
     print("The Word to be Guessed is:" )
     print(current_word_state(word,letters_guessed))

     while wrong_guesses < max_wrong_guesses:
        guess=input("\n Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in letters_guessed :
            print("You have already guessed that letter...!\n")
            continue
        letters_guessed.add(guess)
        if guess in word:
            print("Correct Guess..:)\n ")
            
        else:
            wrong_guesses+=1
            print(f"\nopps...! Wrong guess. You have {max_wrong_guesses-wrong_guesses} guesses left... \n") 
        current_word=current_word_state(word,letters_guessed)
        print(current_word)


        if '_' not in current_word:
          print("\nYahoo..@ Congratulations! You've guessed the word!\n") 
          break
        
     else:
         print(f"\nGame Over!The word is {word}")

     print("\nGood Bye !\n")



game()
            

     