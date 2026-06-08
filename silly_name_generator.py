import random
print(f"welcome to the silly name generator ")
first_name=('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
 "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
 'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
 'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
 'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
 'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
 "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
 'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
 "Winston 'Jazz Hands'", 'Worms')
last_name=('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck',)
while(True):
    select_first_name=random.choice(first_name)
    select_last_name=random.choice(last_name)
    print(f"your name will be {select_first_name} {select_last_name}")
    choice= input("do u wanna continue to play(yes/no) : ")
    if(choice!="yes"):
        break


