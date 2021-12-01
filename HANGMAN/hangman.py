import random
def hangman():

    word=random.choice(["yusuf", "earth", "Adamu", "dolapo", "faisal", "idris", "babatunde","adeyemi", "deji","antidote"])
    validLetters="abcdefghijklmnopqrstuvwxyz"
    turns=10
    guessmade=""

    while len(word)>0:
        main=""
        missed=0
        for  letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+"_"+" "
        if main==word:
            print( main)
            print("You won!")
            break
        print("Guess the word:", main)
        guess=input()




        if guess in validLetters:
            guessmade=guessmade+guess
        else:
            print("Enter a valid character")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print("  ----------")
            elif turns==8:
                print("8 turns left")
                print("----------")
                print("     0     ")
            elif turns==7:
                print("7 turns left")
                print("----------")
                print("     0     ")
                print("     |     ")
            elif turns==6:
                print("6 turns left")
                print("----------")
                print("     0     ")
                print("     |     ")
                print("    /      ")
            elif turns==5:
                print("5 turns left")
                print("----------")
                print("     0     ")
                print("     |     ")
                print("    / \     ")
            elif turns==4:
                print("4 turns left")
                print("----------")
                print("   \ 0     ")
                print("     |     ")
                print("    / \     ")
            elif turns==3:
                print("3 turns left")
                print("----------")
                print("   \ 0 /    ")
                print("     |     ")
                print("    / \     ")
            elif turns==2:
                print("2 turns left")
                print("----------")
                print("   \ 0 /|    ")
                print("     |     ")
                print("    / \     ")
            elif turns==1:
                print("1 turns left")
                print("last breaths counting , Take care!")
                print("----------")
                print("   \ 0 _|/    ")
                print("     |     ")
                print("    / \     ")
            elif turns==0:
                print("you loose")
                print("You let a kind man Die")
                print("----------")
                print("     0 _|    ")
                print("    /|\     ")
                print("    / \     ")
                break

name=input("Enter your name :")
print("Welcome! %s"%name)
print("---------------------------------")
print("try to guess the word in less than 10 trials")
hangman()
print()
