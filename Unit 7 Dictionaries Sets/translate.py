'''
Rand Hasan
Period 11 HCP
Unit 7 Dictionaries
Program to translate from English to either French or German
'''
import inputHelpers

def loadData(file):
    inFile = open(file,"r")
    dictionary = {}
    for line in inFile:
        wordList = line.strip().split(",")
        dictionary[wordList[0].strip()]= wordList[1:]
    inFile.close()
    return dictionary

def translate(sentence,dictionary,choice):
    punct = "."
    #check for punctuation at end of sentece
    if sentence.strip()[-1] in ['.','!','?']:
        punct = sentence[-1]
        sentence = sentence[:-1] #slices end one before the really end
    else:
        punct = ""
    
    #turn the sentence into a list
    sentWordList = sentence.strip().split()
    
    #make a list to hold translated words
    translatedList = []
    
    #loops through sentence list converting to french or german
    for word in sentWordList:
        if word in dictionary:
            if choice == 1: #French
                translatedList.append(dictionary[word][0])
            else: #German
                translatedList.append(dictionary[word][0])
        else: #word not in dictionary
            translatedList.append(word)
            
    return " ".join(translatedList)+punct

def main():
    dictionary = loadData("Dictionary.txt")
    sentence = input("Enter a sentence to translate: ").upper()
    choice = inputHelpers.getIntBetween("Enter 1 for French or 2 for German:", 1, 2)
    print(translate(sentence,dictionary,choice).lower().capitalize())
main()