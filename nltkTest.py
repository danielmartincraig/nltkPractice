###################################################################################################
# This is code that I wrote while working through the book Natural Language Processing with Python,
# by Steven Bird, Ewan Klein, and Edward Loper
#
# Book Citation:
# Bird, Steven, Ewan Klein, and Edward Loper (2009), Natural Language Processing with Python, O'Reilly Media.
#
# @author Daniel Craig
###################################################################################################

import nltk

from nltk.book import *


def lexical_diversity(text):
    """ This function counts the lexical diversity of the text, aka how many times each word is used on average """
    print("The lexical diversity of " + str(text) + " is : ", end="")
    print(len(text) / len(set(text)))


def percentage(text, word=""):
    """ This function calculates the percent of a text taken up by a particular word """
    if not word == "":
        # If the user forgets to input the word, it just prompts them for it again
        print("The percentage of the word " + word + " in text " + str(text) + " is : ", end="")
        print(100 * text4.count(word) / len(text))
    else:
        print("Percentage: Please specify the word")


def main():
    """ Driver program for the two functions above """
    print("")
    lexical_diversity(text4)

    print("")
    percentage(text4, "America")

# this trick lets this file be included as a library without causing problems
if __name__ == '__main__':
    main()
