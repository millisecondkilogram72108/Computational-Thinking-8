import random
import time
caught_list = []
money = 0

print("Welcome! This is a fishing game, which I shouldnt have to explain because it's in the name.")
print("                                                                                                     ")
print("To determine what fish you catch, you get to decide how far to cast your line.")
print("If at any point your done, type 'end' into the 'how far?' space.")


# For loop starts here, repeats line 11 to 75
for i in range (30):
    print("                                                                                                     ")
    depth = input("How far woud you like to cast your line? options: 1, 2, 3, 4 ")
    if depth == "1":
        fish_list = ["a Chinook Salmon", "a Blue Rockfish", "a Squid", "a Black Bullfish", "an Arrowtooth Flounder", "a Longfin Smelt", "nothing", "nothing"]
        fish = random.choice(fish_list)
        input("Press enter to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")
        caught_list.append(fish)
        money += 15
    elif depth == "2":
        fish_list_2 = ["an Albacore Tuna", "a Bank Rockfish", "a Bluegill", "a Brook Trout", "a Canary Rockfish", "a Lingcod", "a Dogfish", "nothing"]
        fish = random.choice(fish_list_2) 
        input("Press enter to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")
        caught_list.append(fish)
        money += 20
    elif depth == "3":
        fish_list_3 = ["a China Rockfish", "a Chum Salmon", "a Coho Salmon", "a Coastal Cutthroat Trout", "a Copper Rockfish", "a Pacific Cod"]
        fish = random.choice(fish_list_3)
        input("Press enter to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")
        caught_list.append(fish)
        money += 30
    elif depth == "4":
        fish_list_4 = ["an English Sole", "a Eulachon Smelt", "a Golden Trout", "a Green Sturgeon", "a Jack Mackeral", "a Bluefin Tuna", "a King Salmon"]
        fish = random.choice(fish_list_4)
        input("Press enter to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")
        caught_list.append(fish)
        money += 40
    elif depth == "end":
        break
# For loop ends here


# ending sequence with amount and types of fish caught and how much money you could make by selling
print("                                                                                                     ")
print("You caught:")
print(f"{caught_list}")
print("                                                                                                     ")
print("Now it's time to sell your haul!")
print("                                                                                                     ")
print(f"You got ${money} from all the fish you caught, great job!")