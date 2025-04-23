import random

# Pick a word at random
word_list = ["heart", "audio", "fairy", "nymph", "lover", "oinks", "water", "bread", "igloo"]
hidden_word = random.choice(word_list)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    if len(guess_word) > 5 or len(guess_word) < 5:
         print("that is not 5 letters")
    else:
         # first letter
        if guess_word[0] == hidden_word[0]:
            output += "🟩"
        elif guess_word[0] in hidden_word:
            output += "🟨"
        else:
             output += "⬛"
    
        # Second letter
        if guess_word[1] == hidden_word[1]:
            output += "🟩"
        elif guess_word[1] in hidden_word:
            output += "🟨"
        else:
             output += "⬛"

        # third letter
        if guess_word[2] == hidden_word[2]:
            output += "🟩"
        elif guess_word[2] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # fourth letter
        if guess_word[3] == hidden_word[3]:
            output += "🟩"
        elif guess_word[3] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

         # fifth letter
        if guess_word[4] == hidden_word[4]:
            output += "🟩"
        elif guess_word[4] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")
