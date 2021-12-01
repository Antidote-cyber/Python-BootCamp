# DONT EDIT ANYTHING YOU DONT KNOW
# DONT EDIT ANYTHING YOU DONT KNOW
# DONT EDIT ANYTHING YOU DONT KNOW
# DONT EDIT ANYTHING YOU DONT KNOW
import json #json library
from difflib import get_close_matches #imports only the get_get_close_matches library

data=json.load(open("data.json"))
print("<<DevAntidote>>")
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
            return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0: #This checks if the misspelled words exists with at least one close match from the dictionary
        print("did you mean %s instead "%get_close_matches(word,data.keys())[0] ) #This chooses the first out of all the close match words
        decide=input("press y for yes or n for no: ")
        if decide=="y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide=="n":
            return("You have entered a wrong word please check it again")
        else:
            return("you have entered a wrong input please just y or n")
    else:
        print("You have entered a wrong word please check it again")


word=input("Enter The word to search: ")
output=translate(word)

if type(output)==list: #Having multiple meqning
    for item in output:
        print(item)
else:
    print(output)
