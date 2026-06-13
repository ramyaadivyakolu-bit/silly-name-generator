import random
import time
#taking players info for the game=no of players,their name in list.we also used if condition to make sure if players are less than 2 or greather than 4 to run it again until correct value is provided
def players_info():
    while(True):
        total_players=int(input("enter number of players(2/3/4): "))
        if 2<=total_players<=4:
            break
        else:
            print("you need to enter valid number of players")
    players=[]
    for i in range(total_players):
        name=input(f"enter name for player {i+1} : ")
        players.append(name)
    return players
#game starts here
while(True):
    #taking range from user with using exception handling.when user enter other than number it runs until user enter correct values
    while(True):
        try:
            lower_number=int(input("enter a lowest number of your range"))
            higher_number=int(input("enter a highest number of your range"))
            break
        except ValueError:
            print("you need to enter a proper value")
    #to make sure random.randint method works perfect
    if(lower_number>higher_number):
        lower_number,higher_number=higher_number,lower_number
    secret_number=random.randint(lower_number,higher_number)
    players=players_info()
    #asking user difficult level of the game
    level=input("enter the type of difficulty,your game needs to be : (easy/medium/hard)")
    if(level.lower()=="easy"):
        total_chances=10
        print(f"for this game u have total of {total_chances} chances")
    elif(level.lower()=="medium"):
        total_chances=7
        print(f"for this game u have total of {total_chances} chances")
    else:
        total_chances=5
        print(f"for this game u have total of {total_chances} chances")
    active_players = players.copy()
    finished_players = []
    guess_counts = {player: 0 for player in players}
    history = {player: [] for player in players}
    #starting time to find out how much time it takes to complete the game
    start=time.time()
    #guessing numbers start here
    while len(active_players) > 0:
        for player in active_players.copy():
            print(f"\n{player}'s turn!")
            try:
                guessed_number = int(input("enter a number you think is the secret number: "))
            except ValueError:
                print("you need to enter a valid number")
                continue
            guess_counts[player] += 1
            history[player].append(guessed_number)
            if guessed_number == secret_number:
                print(f"🎉 {player} found the secret number {secret_number} in {guess_counts[player]} guesses!")
                print(f"{player}'s guess history: {history[player]}")
                finished_players.append(player)
                active_players.remove(player)
            elif guessed_number < secret_number:
                print(f"oops! think larger than {guessed_number}")
            else:
                print(f"oops! think smaller than {guessed_number}")
            if guess_counts[player] == total_chances and player in active_players:
                print(f"{player} ran out of chances!")
                print(f"{player}'s guess history: {history[player]}")
                active_players.remove(player)
    #stopping time
    end = time.time()
    time_taken=end-start
    #displaying total time,final rankings
    print(f"total time taken for this game : {round(time_taken,2)} secs")
    print("\n------------***---------------")
    print("🏆 final rankings:")
    for i, player in enumerate(finished_players):
        print(f"{i+1}. {player} - found it in {guess_counts[player]} guesses")
    if active_players:
        for player in active_players:
            print(f" {player} - ran out of chances")
    print("------------***---------------")
    #asking player if he wants to play again
    play_again=input("enter do you want to play again(yes/no) : ")
    if(play_again.lower() !="yes"):
        print("thanks for playing, goodbye!")
        break
    




