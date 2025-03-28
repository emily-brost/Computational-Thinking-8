while True:
    word = input("what do you think grandma likes?  ")

    if len(word) > 4:
        print(f"Grandma does not like {word}!")
    else:
        print(f"Grandma likes {word}!")

    print (" ")