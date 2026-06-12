import random
while(True):
    while(True):
        try:
            lower_number=int(input("enter a lowest number of your range"))
            higher_number=int(input("enter a highest number of your range"))
            break
        except ValueError:
            print("you need to enter a proper value")
    if(lower_number>higher_number):
        lower_number,higher_number=higher_number,lower_number
    secret_number=random.randint(lower_number,higher_number)
    guessing_count=0
    while(True):
        if(guessing_count==7):
            print(f"oops ! you run out of chances,better luck next time")
            print(f"the secret number you trying to find is {secret_number}")
            break
        try:
            guessed_number=int(input("enter a number u thought it would be secret number"))
        except ValueError:
            print("you need to enter a valid number")
            continue
        guessing_count+=1
        if(guessed_number==secret_number):
            print(f"you find out the secret number {secret_number}")
            print(f"you found in {guessing_count} guesses")
            break
        elif(guessed_number<secret_number):
            print(f"oops ! you need to think of a larger number than {guessed_number}")
        else:
            print(f"oops ! you need to think of a smaller number than {guessed_number}")
        if(guessing_count>4):
            print(f"you still have {7-guessing_count} chances")
        if(guessing_count==5):
            choice=input("do u need hint to find secret number")
            if(choice.lower()=="yes"):
                if(secret_number%2==0):
                    print(f"secret number is even")
                else:
                    print(f"secret number is odd")
            else:
                print("going without a hint,bravo! ")
        if(guessing_count==6):
            choice=input("do u need hint to find secret number")
            if(choice.lower()=="yes"):
                if(secret_number<=((lower_number+higher_number)/2)):
                    print(f"secret number is in first half of the range")
                else:
                    print(f"secret number is in second half of the range")
            else:
                print("u can crack even without a hint,bravo")
    play_again=input("enter do you want to play again(yes/no) : ")
    if(play_again.lower() !="yes"):
        print("thanks for playing, goodbye!")
        break
    




