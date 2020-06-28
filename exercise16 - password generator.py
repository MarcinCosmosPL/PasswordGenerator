#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html - Where I found the challenge

import random

#defining the strings of required character types - you can define new - and then add it to allCharsList - and everything should work fine
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
specials = "@"   ####To test adding a new list
allCharsList = [ascii_lowercase, ascii_uppercase, digits, specials] #important list of required character types
allChars = "" #lists combined- generates by the loop below:
for i in allCharsList:
    allChars+=i
listOfStupidPasswords = ["dupaDupadupa", "Admin1", "password", "p", "beer"]
minimalChars = 5 ## Change if you like, but you cannot make it shorter than number of lists of characters - it would create an infinite LOOP!!!!


assert minimalChars >= len(allCharsList), "minmal number of characters in password must be bigger than number of list of required character types"

def charChecker(Password, *Charlists):  #Check if the password contains at least one element of given Charlists
    for charlist in Charlists:
        commons_list = [char for char in Password+charlist if char in Password and char in charlist]
        if len(commons_list) == 0:
            return False
            break
    else:
        return True



def PassGenerate(numberOfchars=10, easyMode=False): #generates the password, needs random and charCecker
    if easyMode:
        return random.choice(listOfStupidPasswords)
    elif numberOfchars < minimalChars:
        print("Password must be longer than {} characters".format(minimalChars))
        return False #will be usefull for further input
    else:
        newPass = ''
        while newPass == '':
            for i in range(numberOfchars):
                newChar = random.choice(allChars)
                newPass+=newChar
            if charChecker(newPass, *allCharsList):
                    return newPass
            else:
                newPass = ''

    
### TIME TO ASK THE USER
print("\n WELCOME TO PASSWORD GENERATOR \n")
while True:
    difficultySelection = input('Do you want lame password? Put "yes" or "no" and press enter to continue \n')
    if difficultySelection.lower() == 'yes':
        UserPassword = PassGenerate(4, True)
        break
    elif difficultySelection.lower() == 'no': ## THIS IS THE CRUCIAL MOMENT - Someone wants strong password
        while True:
            try: #there may be some errors
                charNumbersSelection = input("How long password do You need? Put the number higher than {} and press enter: \n".format(minimalChars))
                if PassGenerate(int(charNumbersSelection)): #Will be False if number of demanded characters are too low
                    UserPassword = PassGenerate(int(charNumbersSelection))
                    break
                else:
                    print("Password must be longer!")
            except:
                print("ERROR - Did you gave an integer?")
        break
    else:
        print("something wrong!  Repeating..")
    
#Final result:
print("Your password is: \n", UserPassword)






            



        
    

    

        
