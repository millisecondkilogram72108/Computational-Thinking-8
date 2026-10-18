money = 500
health_points = 100
morale = 80
speed = 30




print("Welcome to the")
#oregon trail
print("\033[0;37m                             \033[0;97m▄\033[0;37m             \033[0;97m▄\033[0;37m \033[0m")
print("\033[0;97;47m▄\033[0;97m▀▄\033[0;37m \033[0;97m▄▀\033[0;97;47m▄\033[0;37m \033[0;97m▄▀\033[0;97;47m▀\033[0;37m \033[0;97m▄▀▀\033[0;37m \033[0;97;47m▄\033[0;97m▀▄\033[0;37m \033[0;97;47m▄\033[0;97m▀▄\033[0;37m      \033[0;97m█\033[0;37m▄  \033[0;97m▄▀\033[0;97;47m▄\033[0;37m \033[0;97m▄▀█\033[0;37m \033[0;97m█\033[0;37m \033[0;97m█\033[0;37m \033[0m")
print("\033[0;97;47m▐\033[0;37m \033[0;97;47m▓\033[0;37m \033[0;97;47m▌\033[0;37m▀\033[0;97m▄\033[0;37m \033[0;97;47m▌\033[0;97m▀\033[0;37m▄ \033[0;97;47m▌\033[0;37m \033[0;97;47m▌\033[0;37m \033[0;97;47m▐\033[0;37m \033[0;97;47m▓\033[0;37m \033[0;97;47m▓\033[0;37m \033[0;97;47m▌\033[0;37m      \033[0;97;47m▐\033[0;37m \033[0;97m▄\033[0;37m \033[0;97;47m▌\033[0;37m▀\033[0;97m▄\033[0;37m \033[0;97;47m▓\033[0;37m▄\033[0;97;47m▌\033[0;37m \033[0;97;47m▓\033[0;37m \033[0;97;47m▓\033[0;37m \033[0m")
print("\033[0;37m \033[0;97m▀\033[0;37m▀ \033[0;97m▀\033[0;37m \033[0;97;47m▀\033[0;37m  \033[0;97m▀\033[0;37m▀  \033[0;97m▀\033[0;37m▀  \033[0;97m▀\033[0;37m▀ \033[0;97;47m▌\033[0;37m ▀       \033[0;97m▀\033[0;37m▀ \033[0;97m▀\033[0;37m \033[0;97;47m▀\033[0;37m \033[0;97;47m▌\033[0;37m ▀ ▀ ▀▀\033[0m")

horse_or_ox = input("First off, would you prefer a horse or an ox to carry your wagon? ")
if horse_or_ox == "horse":
    speed += 20
elif horse_or_ox == "ox":
    speed += 0
print("Alright!")
print("                                                                                                     ")
print("Now, to start off our journey, your going to need to gather your materials. You start off with $500.")
print("                                                                                                     ")
print(" Material List 1 - $300 (basic): flour x175, dried fruit x2, medicine bottle x3, coffee x4, toolbox x3, wheel x2")
print(" Material List 2 - $400 (forager's): meat x4, dried fruit x2, medicine bottle x3, forager's encyclopedia x1, coffee x4, toolbox x3, wheel x2")
print(" Material List 3 - $400 (fisher's): meat x2, dried fruit x2, medicine bottle x3, bait x50, coffee x4, toolbox x3, wheel x2")
print(" Material List 4 - $450 (mechanic's): flour x175, dried fruit x2, medicine bottle x3, coffee x4, toolbox x6, wheel x4")

materiallist = input("Choose one and put the list number here: ")

if materiallist == "1":
    money -= 300
elif materiallist == "2" or materiallist == "3":
    money -= 400
elif materiallist == "4":
    money -= 450


print("  ________________")
print(" /_____           |")
print(" |    |  ~~~~~~~    ")
print(" |    |  ~~~~~~~   |")
print(" |____|___________")
print("/____/______________|")
print("/    /          /   |")



q1 = input(f"You set out from independece on your {horse_or_ox} with your wagon bumping along behind you. A mile or two after you leave you see a dog laying alone on the side of the road. Do you examine the dog or leave it? ")
if q1 == "examine":
    morale += 10
    dogq = input(f"You see that the dogs paw has a thorn in it, not uncommon in the high grasses around you. Would you like to lay the dog onto your {horse_or_ox} or leave it? ")
    if dogq == "bring" or dogq == "lay it" or dogq == "lay":
        morale += 15
    elif dogq == "leave" or dogq == "leave it":
        morale -= 10
elif q1 == "leave it" or q1 == "leave":
    morale -= 10
print("You manage to get to the Kansas River crossing by nightfall, you set up camp right next to the water.")
#dinner sequence
if materiallist == "3":
    fish_ = input("Would you like to fish in the river? ")
    if fish_ == "yes":
        morale += 10
        print("You catch a fish to eat for dinner, and you decide to skewer it with some of your meat.")
        health_points += 2
    elif fish_ == "no":
        print("You use the meat you bought to make yourself a skewer.")
        health_points +=1
if materiallist == "2":
    forager = input("Would you like to forage for your dinner?")
    if forager == "yes":
        print("You look around your camp and find plenty of berries an mushrooms you know to be safe from your book and cook those on your fire for dinner.")
        health_points +=2
    elif forager == "no":
        print("You have some of your dried fruit instead.")
        health_points +=0
if materiallist == "1" or materiallist == "4":
    print("You have your last piece of meat and some of your dried fruit.")
    health_points +=5
sleep = input("Press enter to go to sleep ")
print("                                                                                                     ")
print(" ____  ____  ____  ____  ____")
print("(_   )(_   )(_   )(_   )(_   )")
print(" / /_  / /_  / /_  / /_  / /_")
print("(____)(____)(____)(____)(____)")
print("                                                                                                     ")
space = input(" ")

print("You wake up to the sound of a robin calling far off in the distance. A group of geese fly overhead as the sun rises.")
coffee = input("Would you like to make some coffee? ")
if coffee == "yes":
    morale += 15
    speed += 5

print("You smother out your fire and get ready to cross the river.")
print("                                                                                                     ")
print("Now you must cross the river.")
crossriver = input("Would you like to pay the ferryman $20 or try and ford the river? ")
if crossriver == "pay the ferryman" or crossriver == "pay ferryman":
    #ferry
    money -= 20
    morale += 5
elif crossriver == "ford" or crossriver == "ford the river":
    if horse_or_ox == "horse":
        horseford = input("Fording the river may be too hard on you horse's legs, you should probably take the ferry. ")
        if horseford == "okay" or horseford == "ok":
            money -= 20
            morale += 5
    else:
        #river - ford
        print("You seal your wagon and walk into the river.")
        print("As you across the rocks and sand at the bottom of the river a large fish's fin cuts across your leg and leaves a mild scratch.")
        health_points -= 10
        med = input("Would you like to put some medicine on? ")
        if med == "yes":
            ("Good choice!")
            health_points += 5
        elif med == "no":
            ("Okay.")
            health_points -= 30
        print("You lose 1 bag of coffee.")
space4 = input("You keep moving.")
print("                                                                                                     ")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("                                                                                                     ")
#coyote sequence
coyote = input("You decide to take a break to eat lunch. As your eating, something rustles behind you. The seomthing peeks it head out of the grass to reveal itself as a coyote. Would you like to give it some of you food? ")
if coyote == "yes":
    print("You hold your hand out wiht some meat for it to eat, it takes a while but it eventually takes he food, but not without biting your finger.")
    health_points -= 10
    med2 = input("Would you like to use some of your medicine? ")
    if med2 == "yes":
        health_points +=5
    elif med2 == "no":
        print("Okay.")
        health_points -= 30
elif coyote == "no":
    print("The coyote slips away back into the grass.")

    health_points -=5
space3 = input("You keep moving.")
print("                                                                                                     ")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("                                                                                                     ")
print("You are about halfway to Fort Kearny, the first stop on your journey. You decide to stop here for the night.")


print("You make a fire and get ready to make dinner.")

#dinner sequence
if materiallist == "3":
    fish_ = input("Would you like to fish in the river? ")
    if fish_ == "yes":
        morale += 10
        print("You catch a fish to eat for dinner, and you decide to skewer it with some of your meat.")
    elif fish_ == "no":
        print("You use the meat you bought to make yourself a skewer.")
        health_points +=1
if materiallist == "2":
    forager = input("Would you like to forage for your dinner?")
    if forager == "yes":
        print("You look around your camp and find plenty of berries an mushrooms you know to be safe from your book and cook those on your fire for dinner.")
        health_points +=2
    elif forager == "no":
        print("You have some of your dried fruit instead.")
        health_points +=0
if materiallist == "1" or materiallist == "4":
    print("You have your last piece of meat and some of your dried fruit.")
    health_points +=1

sleep = input("Press enter to go to sleep ")
print("                                                                                                     ")
print(" ____  ____  ____  ____  ____")
print("(_   )(_   )(_   )(_   )(_   )")
print(" / /_  / /_  / /_  / /_  / /_")
print("(____)(____)(____)(____)(____)")
print("                                                                                                     ")
space = input(" ")

print("This is your last day journeying before you make it to Fort Kearny.")
print("                                                                                                     ")
print("You wake up to a snail inching along beside you, dew dripping off the dry grass.")
coffee = input("Would you like to make some coffee? ")
if coffee == "yes":
    morale += 15
    speed += 5

space2 = input("You smother out your fire and head out.")
print("                                                                                                     ")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("                                                                                                     ")
print(f"As Fort Kearny's high wooden walls phase into view, you hear a loud crack behind you, and your {horse_or_ox} stomps in distress. It seems like your back left wheel has cracked!")
wheel = input("Use a wheel  and toolbox to repair your broken wagon. ")
space5 = input("Your wagons all fixed and your ready to move on!")

print("                                                                                                     ")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
print("**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~")
print("                                                                                                     ")

print("You have arrived at Fort Kearny!")
print("                                                                                                     ")
print("This is the end of your journey... for now! You still have quite a ways, but we'll stop here!")
print("                                                                                                     ")
print("This whole time i've been keeping track of all the descisions youve made throught you're journey, and this will give you an insight into what type of adventure you prefer to lead!")
space5 = input("")

#money = 500 - ending range - 200-50
#health_points = 100 - ending range - 115-36
#morale = 80 - ending range - 100-50
#speed = 30 - ending range - 70-30
print(f"Your ending health was {health_points}.")
print(f"Your ending amount of money was {money}.")
print(f"You ending amount of happiness was {morale}.")
print(f"Your ending speed was {speed}.")
space5 = input("")

#money was very high
if money > morale:
    print("You are a super saver!! You really value the importance of saving your resources and are willing to accept the consequences!")
#low heath and morale
if health_points < 50 and morale < 50:
    print("You really like to live life on the edge and have quite a chaotic time!")
#morale high
if morale > health_points:
    print("You like to have a great time, even if that means sacrificing other areas of your journey!")
#high morale and health - safe
if morale > 90 and health_points > 90:
    print("You make very calculated descisions and prefer to be more on the safe side!")
#very high morale
if morale > 90:
    ("You prioritize happiness over all else, it's the simple things!")
#serious and fast
if health_points < 55 or morale < 55:
    ("You may take you journey quite seriously and have great orginization and planning!")