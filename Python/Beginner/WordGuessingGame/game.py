# Users Input their name 
# Asked to guess any alphabet
# If the word has that letter it will show on in the correct placement
# Else asked to input another letter
# Have maximum of 12 turns

import random

# Functions
def word():
    words = ["Abjure","Future","Picnic","Agonistic","Garland","Protect","Airline","Gigantic","Publish","Bandit","Goofy","Quadrangle","Banquet","Government","Recount","Binoculars","Grandnieces","Redoubtable","Biologist","Handbook","Reflection","Blackboard","Himself","Reporter","Board","Indulge","Ring","Bookworm","Inflatable","Salesclerk","Butterscotch","Inimical","Snapshot","Camera","Interim","Shellfish","Campus","Invest","Ship","Catfish","Jackpot","Significance","Carsick","Kitchenette","Sometimes","Celebrate","Law","Sublime","Celery","Life","Tabletop","Citizen","Lifeline","Teamwork","Coloring","Love","Tennis","Compact","Magnificent","Timesaving","Dark","Malevolence","Tree","Damage","Man","Termination","Dangerous","Mascot","Underestimate","Decorum","Marshmallow","Vineyard","Endorse","Mine","War","Engender","Moonwalk","Way","Erratic","Near","Wealth","Envelope","Nephogram","Wednesday","Etymology","Newborn","World","Eyewitness","Noisome","Xerox","Eulogy","Owl","You","Fish","Parenthesis","Zestful","Food","Perpetrator", "Foreclose", "Phone"]
    return random.choice(words)


def printWord(word):
    



# Main Function
def main():
    name = input("What is your name? ")
    print("Good Luck! " + name)
    wordToGuss = word()
    print("Word has selected, Start guessing.")
    printWord()



if __name__ == "__main__":
    main()