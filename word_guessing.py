import random
name=input("enter your name : ")
def asking_choice():
    choice=input(f"hello {name},which level do u want to play(easy/medium/hard): ")
    if(choice=="easy"):
        total_guesses=5
        print("you need guess a fruit or a vegetable of 5 letters")
        words=['apple','berry','mango','melon','guava','lemon','peach','olive','cress','chard','beets','leeks','onion','radic','yucca']
        word=random.choice(words)
    elif(choice=="medium"):
        total_guesses=6
        print("you need to think of  a country(hint: the country name has five letters only)")
        words=['chile','china','egypt','ghana','haiti','india','italy','japan','kenya','libya','malta','nepal','samoa','spain','syria','yemen']
        word=random.choice(words)
    else:
        total_guesses=10
        print("you need think of a coutry(hint:no need to limit to 5 letters")
        words=['mangolia','angola','bolivia','nigeria','tanzania','namibia','turkey','zambia','sudan','france','ukraine','poland','uganda','loas','syria']
        word=random.choice(words)
    return total_guesses,word

def valid_input(guessing_word,total_guesses,word):
    char=input(f"enter the character you would think it is in word")
    if(len(char)==1 and char.isalpha()):
            if(char in word):
                 guessing_word=guessing_word+char
            else:
                 guessing_word=guessing_word+char
                 total_guesses-=1
    else:
            print("you need to enter single character only")
    return guessing_word,total_guesses,word


total_guesses,word=asking_choice()
print("guess characters of word")
guessing_word=""
while(total_guesses>0):
     guessing_word,total_guesses,word=valid_input(guessing_word,total_guesses,word)
     print(f"letters used this far : {','.join(guessing_word)}")
     for char in word:
        if char in guessing_word:
             print(char,end=" ")
        else:
            print("_",end=" ")
            
     if all(char in guessing_word for char in word):
        print("you won !")
        break
     print(f"  you still left with {total_guesses} guesses")
else:
    print(f"you lost! the word was {word}")
    
