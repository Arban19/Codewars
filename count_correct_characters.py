""" Consider a game, wherein the player has to guess a target word. All the player knows is the length of the target word.

To help them in their goal, the game will accept guesses, and return the number of letters that are in the correct position.

Write a method that, given the correct word and the player's guess, returns this number.

For example, here's a possible thought process for someone trying to guess the word "dog":

count_correct_characters("dog", "car"); #0 (No letters are in the correct position)
count_correct_characters("dog", "god"); #1 ("o")
count_correct_characters("dog", "cog"); #2 ("o" and "g")
count_correct_characters("dog", "cod"); #1 ("o")
count_correct_characters("dog", "bog"); #2 ("o" and "g")
count_correct_characters("dog", "dog"); #3 (Correct!)
The caller should ensure that the guessed word is always the same length as the correct word, but since it could cause problems
if this were not the case, you need to check for this eventuality:

Raise an exception if the two parameters are of different lengths.

"""

def count_correct_characters(correct,guess):
    sum = 0
    if len(correct) != len(guess):
        raise ValueError
    else:
        for ind, ele in enumerate(correct):
            for dex, ment in enumerate(guess):
                if ment == ele and dex == ind:
                    sum += 1
        return sum

def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise ValueError("Strings must be of equal length")

    return sum(1 for c, g in zip(correct, guess) if c == g)
