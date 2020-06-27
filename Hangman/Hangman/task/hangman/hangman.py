# Write your code here
import random
import string



def guess_word():
    target_words = ['python', 'java', 'kotlin', 'javascript']
    target_word = target_words[random.randint(0, 3)]
    tried_letters = set()
    tried_times = 0
    found = False
    while tried_times < 8:

        word = ''
        for letter in target_word:
            if letter in tried_letters:
                word += letter
            else:
                word += '-'
        print(f"\n{word}")
        if word == target_word:
            found = True

        try:
            guess = input("Input a letter:")
        except:
            pass

        if len(guess) != 1:
            print("You should input a single letter")
        elif guess not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif guess in tried_letters:
            print("You already typed this letter")
        else:
            tried_letters.add(guess)
            if guess not in target_word:
                tried_times += 1
                print("No such letter in the word")

    if found:
        print(f"You guessed the word {target_word}!")
        print("You survived!")
    else:
        print("You are hanged!")

print("""H A N G M A N""")
action = input('Type "play" to play the game, "exit" to quit:')
while action != "exit" and action == "play":
    guess_word()
    action = input('\nType "play" to play the game, "exit" to quit:')
