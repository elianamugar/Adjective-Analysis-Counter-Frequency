#requires download of nltk in python
import os
import nltk
from nltk.corpus import *
import string

def main():
    print("\nHere are the corpora built into nltk:")
    for h in os.listdir(nltk.data.find("corpora")):
        if '.zip' not in h:
            print(h)
    print()
    chosen_corpora = input("Enter corpora name (copy the name EXACTLY as listed): ")
    function_string = "nltk.corpus." + chosen_corpora + ".fileids()"
    print("\nHere are the options of corpora from", chosen_corpora + ": \n")
    for corpus in eval(function_string):
        print(str(corpus))
    print()
    text_function = chosen_corpora + ".raw(str(input('Enter text file name (with .txt): ')))"
    text = eval(text_function)
    tokens = nltk.word_tokenize(text)
    tagged_corpora = nltk.pos_tag(tokens)
    update_corpora = ""
    
    count_adj = 0

    for i in range(len(tagged_corpora)):
        if ((('JJ' in tagged_corpora[i]) or ('JJR' in tagged_corpora[i]) or ('JJS' in tagged_corpora[i])) and (('such' not in tagged_corpora[i]) and ('Such' not in tagged_corpora[i]))):
            count_adj += 1
            update_corpora += str(tagged_corpora[i][0]) + "\n"

    update_corpora += "Adjectives: " + str(count_adj)
    f = open(str(input("Enter filename for which you want the data text to be exported (with .txt): \n")), "w")
    f.write(update_corpora)

while True:
    answer = input("Run the AA Counter Frequency program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break