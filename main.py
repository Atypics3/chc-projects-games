import random
import time

print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

def main():
  global count, display, word, already_guessed, length, play_game, word
  word_to_guess = ["january", "border", "image", "film", "promise", "Kids", "lungs", "doll", "rhyme", "damage", "plants"]
  word = random.choice(word_to_guess)
  length = len(word)
  count = 0
  display = '_' * length
  already_guessed = []
  play_game = ""

# function loops the game when the first game ends
def play_loop():
  global play_game
  play_game = input("Play again? (Y/N): ")
  # while user inputs wrong key, loops prompt again
  while play_game not in ["Y", "N", "y", "n"]:
    print("Error! Please enter either 'Y' or 'N'.")
    play_game = input("Play again? (Y/N): ")
  
  # if the input is 'Y', then plays game again. If not, exits the program
  if (play_game == "Y"):
    main()
  elif (play_game == "N"):
    print("Thanks for playing!")
    time.sleep(5)
    exit()

# function has the entire game in it
def hangman_game():
  global count, display, word, already_guessed, play_game
  num_guesses = 5
  guess = input("This is the word: " + display + "\nEnter your guess: ")
  guess = guess.strip() # removes a letter from the given word
  # if the guess is nothing or greater than or equal to 2 or if a number is inputted,
  # then restart input prompt
  if (len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9"):
    print("Invalid input. Please try again.\n")
    hangman_game()
  # if the guess is a match, search for that letter in the word
  elif guess in word:
      already_guessed.extend([guess])
      index = word.find(guess)
      word = word[:index] + "_" + word[index + 1:]
      display = display[:index] + guess + display[index + 1:]
      print(display + "\n")

  #if already guessed, prompt another letter
  elif guess in already_guessed:
      print("Try another letter.\n")

  # otherwise, the guess is wrong and the user will see how many guesses they have left
  # the visual status of the hangman is also shown, depending on the progress that the user has made
  else:
      count += 1

      if count == 1:
          time.sleep(1)
          print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
          print("Wrong guess. " + str(num_guesses - count) + " guesses remaining\n")

      elif count == 2:
          time.sleep(1)
          print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
          print("Wrong guess. " + str(num_guesses - count) + " guesses remaining\n")

      elif count == 3:
          time.sleep(1)
          print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
          print("Wrong guess. " + str(num_guesses - count) + " guesses remaining\n")

      elif count == 4:
          time.sleep(1)
          print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
          print("Wrong guess. " + str(num_guesses - count) + " last guess remaining\n")

      elif count == 5:
          time.sleep(1)
          print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")
          # game is over at this point, tells the user that they lost, what the word was, and to loop back to restart the game
          print("Wrong guess. You are hanged!!!\n")
          print("The word was: ", already_guessed, word)
          play_loop()

  # if the word was guessed correctly, the user wins
  if word == '_' * length:
      print("Congrats! You have guessed the word correctly!")
      play_loop()


  elif count != num_guesses:
      hangman_game()


main()
hangman_game()
  
  
  
  