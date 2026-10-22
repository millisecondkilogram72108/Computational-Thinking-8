import random
import time
print("Welcome! This is a fishing game, which I shouldnt have to explain because it's in the name.")
print("To determine what fish you catch, you get to decide how far to cast your line.")

for i in range (30):
    depth = input("How far woud you like to cast your line? options: 1, 2, 3, 4 ")
    if depth == "1":
        fish_list = ["a Chinook Salmon", "a Blue Rockfish", "a Squid", "a Black Bullfish", "an Arrowtooth Flounder", "a Longfin Smelt"]
        fish = random.choice(fish_list)
        input("Press any button to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")
    elif depth == "2":
        fish_list_2 = ["an Albacore Tuna", "a Bank Rockfish", "a Bluegill", "a Brook Trout", "a Canary Rockfish", "a Lingcod"]
        fish = random.choice(fish_list_2) 
        input("Press any button to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")
    elif depth == "3":
        fish_list_3 = ["a China Rockfish", "a Chum Salmon", "a Coho Salmon", "a Coastal Cutthroat Trout", "a Copper Rockfish", "a Pacific Cod"]
        fish = random.choice(fish_list_3)
        input("Press any button to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")
    elif depth == "4":
        fish_list_4 = ["an English Sole", "a Eulachon Smelt", "a Golden Trout", "a Green Sturgeon", "a Jack Mackeral", "a Bluefin Tuna"]
        fish = random.choice(fish_list_4)
        input("Press any button to cast your line ")
        print("                                                                                                     ")
        print("Line casted!")
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(2)
        print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        time.sleep(1)
        input(f"You've caught {fish}!")