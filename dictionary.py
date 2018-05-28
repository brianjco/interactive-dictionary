
""" CLI based interactive dictionary script """

__author__      = "Brian Johnson"

import json
from difflib import get_close_matches

data = json.load(open("data.json")) # Imports from data.json file
matches = data.keys()

def definition(word):

    word = word.lower()


    if word in data: # If word is found, print output
        return data[word]

    elif word.title() in data: # Accepting proper nouns as valid input
        return data[word.title()]

    elif len(get_close_matches(word, matches)) > 0: # If the word is not found, this section checks for the closest matching word
        nword = get_close_matches(word, matches, n=1)
        yn = input("Did you mean %s? Enter Y if yes, or N if no: " % nword[0]).lower()
        if yn == "y":
            return data[nword[0]]
        elif yn == "n":
            return "The word doesn't exist."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist."

word = input("What is the word? ")

""" Prints out the output as a list if the type is list """
output = definition(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
