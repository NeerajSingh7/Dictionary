
import json
from difflib import get_close_matches

# loading the data

data = json.load(open("original.json"))
print("Welcome to English->English Dictionary")


# function to find meaning

def findmeaning():
        word = input("Enter a word to search:")
        smallword = word.lower()
        if word in data:
            print(data[word])
        elif smallword in data:
            print(data[smallword])
        elif smallword.title() in data:
            print(data[smallword.title()])
        elif smallword.upper() in data:
            print(data[smallword.upper()])
        elif len(get_close_matches(word , data.keys())) > 0 :
            print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
            decide = input("press 'y' for yes or 'n' for no:")
            if decide == "y":
                 print(data[get_close_matches(word , data.keys())[0]])
            elif decide == "n":
                 print("word not exist in dictionary")
            else:
                 print("You have entered wrong input")
        else:
            print("word not exist in dictionary")
        return


# function to ask again for input

def askagain():
    print("wanna search for another word.  press 'Y' to search, 'N'to exit")
    choice = input()
    return choice



# function to work everthing in Loop

def logic(choice):
    global want_search
    if choice == 'Y':
        findmeaning()
        choice = askagain()
        logic(choice)

    elif choice =='N':
         want_search = False

    else:
        print("Wrong Input!")
        choice  = askagain()
        logic(choice)  
    return want_search




# Program starts from here:

want_search = True 

while want_search:
    findmeaning()
    choice=askagain()
    want_search = logic(choice)