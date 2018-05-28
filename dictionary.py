import json
from difflib import get_close_matches

data = json.load(open("data.json"))
matches = data.keys()

def definition(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, matches)) > 0:
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
output = definition(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
