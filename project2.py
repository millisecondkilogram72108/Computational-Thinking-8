print("Build you dream life")
answer1 = input("What type of house would you like? Options: cabin, apartment, small house, or modern house: ")




if answer1 == "cabin":
    print("Cozy!")
    answer12 = input("Where would you like the cabin to be? Options: forest or lake: ")
    print("Okay, great choice!")
    answerall = input("Would you like a pet? ")
    if answerall == "yes":
        answerall2y = input("What type of pet would you like? Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
        if answerall2y == "dog":
            answerall3y = input("Aw! Any specific type? ")
            if answerall3y == "bernese mountain dog" or answerall3y == "catahoula" or answerall3y == "golden retriever" :
                print("I have one of those too, they are the best!")
            elif answerall3y == "no":
                    print("Okay!")
            
        elif answerall2y == "rodent":
            answerrodent = input("Cute! What kind? ")
            print("Adorable!")
            finalrodent = input("Alright, press enter for your dream life!")
            print("                                                                                                     ")
            print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
            print(f"You live at a cabin near a {answer12}. Your {answerrodent} sits quietly in your pocket, wacthing a bird fly past the window. You look out at the {answer12}, watching the wind blow through the trees. Your happy here, this is what you've always wanted.")
            print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
        elif answerall2y == "lizard":
            print("Cute!")
        elif answerall2y == "cat":
            print("Aw!")
        elif answerall2y == "bird":
            print("Aw, such a nice buddy!")
        
        
        
        else:
                print("Choose something from the list of options please!")
                answerpetwrong1 = input("Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
                if answerpetwrong1 == "dog":
                            answerall3ywrong = input("Aw! Any specific type? ")
                            if answerall3ywrong == "bernese mountain dog":
                                print("I have a berner too, they are the best!")
                            elif answerall3ywrong == "no":
                                    print("Okay!")
                            
                elif answerpetwrong1 == "rodent":
                            answerrodentwrong = input("Cute! What kind? ")
                            print("Adorable!")
                            finalrodentwrong = input("Alright, press enter for your dream life!")
                            print("                                                                                                     ")
                            print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                            print(f"You live at a cabin near a {answer12}. Your {finalrodentwrong} sits quietly in your pocket, wacthing a bird fly past the window. You look out at the {answer12}, watching the wind blow through the trees. Your happy here, this is what you've always wanted.")
                            print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                            quit()
                
                elif answerpetwrong1 == "lizard":
                            print("Cute!")
                elif answerpetwrong1 == "cat":
                            print("Aw!")
                elif answerpetwrong1 == "bird":
                            print("Aw, such a nice buddy!")
                finalwrong1 = input("Alright, press enter for your dream life!")
                print("                                                                                                     ")
                print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                print(f"You live at a cabin near a {answer12}. Your {answerpetwrong1} sits quietly at your feet, wacthing a bird fly past the window. You look out at the {answer12}, watching the wind blow through the trees. Your happy here, this is what you've always wanted.")
                print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                quit()
                



    
        final = input("Alright, press enter for your dream life!")
        print("                                                                                                     ")
        print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
        print(f"You live at a cabin near a {answer12}. Your {answerall2y} sits quietly at your feet, wacthing a bird fly past the window. You look out at the {answer12}, watching the wind blow through the trees. Your happy here, this is what you've always wanted.")
        print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
    elif answerall == "no":
         print("Okay!")
         print("Alright, here is your dream life!")
         print("                                                                                                     ")
         print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
         print(f"You live at a cabin near a {answer12}. You look out at the {answer12}, watching the wind blow through the trees. Your happy here, this is what you've always wanted.")
         print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
               
if answer1 == "apartment":
     answer22 = input("Would you like to be in a big city or a small city? ")
     if answer22 == "big city" or answer22 =="small city":
          print("Alright!")
          answerall1 = input("Would you like a pet? ")
          if answerall1 == "yes":
                  answerall22 = input("What type of pet would you like? Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
                  if answerall22 == "dog":
                      answerall22y = input("Aw! Any specific type? ")
                      if answerall22y == "bernese mountain dog":
                          print("I have a berner too, they are the best!")
                      elif answerall22y == "no":
                              print("Okay!")
                  elif answerall22 == "rodent":
                              answerrodent = input("Cute! What kind? ")
                              print("Adorable!")
                              finalrodent2 = input("Alright, press enter for your dream life!")
                              print("                                                                                                     ")
                              print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                              print(f"You live in an apartment in a {answer22}. Your {answerrodent} sits quietly in your pocket, wacthing a bird fly past the window. You look out at the {answer22}, watching the bustling streets. Your happy here, this is what you've always wanted.")
                              print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                  elif answerall22 == "lizard":
                              print("Cute!")
                  elif answerall22 == "cat":
                              print("Aw!")
                  elif answerall22 == "bird":
                              print("Aw, such a nice buddy!")
                  
                  
                  else:
                    print("Choose something from the list of options please!")
                    answerpetwrong2 = input("Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
                    if answerpetwrong2 == "dog":
                                                answerall4ywrong = input("Aw! Any specific type? ")
                                                if answerall4ywrong == "bernese mountain dog":
                                                  print("I have a berner too, they are the best!")
                                                elif answerall4ywrong == "no":
                                                      print("Okay!")
                                              
                    elif answerpetwrong2 == "rodent":
                                                        answerrodentwrong = input("Cute! What kind? ")
                                                        print("Adorable!")
                                                        finalrodentwrong2 = input("Alright, press enter for your dream life!")
                                                        print("                                                                                                     ")
                                                        print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                                        print(f"You live in an apartment in a {answer22}. Your {finalrodentwrong2} sits quietly in your pocket, wacthing a bird fly past the window. You look out your window, watching the city beneath you. Your happy here, this is what you've always wanted.")
                                                        print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                                        quit()
                    elif answerpetwrong2 == "lizard":
                                                  print("Cute!")
                    elif answerpetwrong2 == "cat":
                                                  print("Aw!")
                    elif answerpetwrong2 == "bird":
                                                  print("Aw, such a nice buddy!")
                    finalwrong1 = input("Alright, press enter for your dream life!")
                    print("                                                                                                     ")
                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                    print(f"You live in an apartment in a {answer22}. Your {answerpetwrong2} sits quietly at your feet, wacthing a bird fly past the window. You look out at the {answer22}, watching the bustling streets. Your happy here, this is what you've always wanted.")
                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                    quit()

                                        
                  final2 = input("Alright, press enter for your dream life!")
                  print("                                                                                                     ")
                  print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                  print(f"You live in an apartment in a {answer22}. Your {answerall22} sits quietly at your feet, wacthing a bird fly past the window. You look out at the {answer22}, watching the bustling streets. Your happy here, this is what you've always wanted.")
                  print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
          elif answerall1 == "no":
                               print("Okay!")
                               print("Alright, here is your dream life!")
                            
                               print("                                                                                                     ")
                               print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                               print(f"You live in an apartment in a {answer22}. You look out at the {answer22}, watching the bustling streets. Your happy here, this is what you've always wanted.")
                               print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")

if answer1 == "modern house":
     answer33 = input("Would you like art or no art in your house? ")
     if answer33 == "art":
          print("Nice!")
     elif answer33 == "no art":
          print("Okay.") 
     answerall13 = input("Would you like a pet? ")
     if answerall13 == "yes":
            answerall33 = input("What type of pet would you like? Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
            if answerall33 == "dog":
                                answerall33y = input("Aw! Any specific type? ")
                                if answerall33y == "bernese mountain dog":
                                    print("I have a berner too, they are the best!")
                                elif answerall33y == "no":
                                        print("Okay!")
            elif answerall33 == "rodent":
                                                    answerrodent = input("Cute! What kind? ")
                                                    print("Adorable!")
                                                    finalrodent = input("Alright, press enter for your dream life!")
                                                    print("                                                                                                     ")
                                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                                    print(f"You live in a large house with {answer33} on the walls. Your {answerrodent} sits quietly in your pocket, wacthing a bird fly past the window. You look out at the streets from your window, watching the wind blow through the various plants and flowers on the sidewalk. Your happy here, this is what you've always wanted.")
                                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
            elif answerall33 == "lizard":
                                                    print("Cute!")
            elif answerall33 == "cat":
                                                    print("Aw!")
            elif answerall33 == "bird":
                                                    print("Aw, such a nice buddy!")
            else:
                                    print("Choose something from the list of options please!")
                                    answerpetwrong2 = input("Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
                                    if answerpetwrong2 == "dog":
                                                                                    answerall4ywrong = input("Aw! Any specific type? ")
                                                                                    if answerall4ywrong == "bernese mountain dog":
                                                                                      print("I have a berner too, they are the best!")
                                                                                    elif answerall4ywrong == "no":
                                                                                          print("Okay!")
                                                                                    else:
                                                                                        print("Adorable!")
                                                                                  
                                    elif answerpetwrong2 == "rodent":
                                                                                            answerrodentwrong = input("Cute! What kind? ")
                                                                                            print("Adorable!")
                                                                                            finalrodentwrong2 = input("Alright, press enter for your dream life!")
                                                                                            print("                                                                                                     ")
                                                                                            print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                                                                            print(f"You live in a large house with {answer33} on the walls. Your {answerrodentwrong} sits quietly in your pocket, wacthing a bird fly past the window. You look out at the streets from your window, watching the wind blow through the various plants and flowers on the sidewalk. Your happy here, this is what you've always wanted..")
                                                                                            quit()
                                    elif answerpetwrong2 == "lizard":
                                                                                      print("Cute!")
                                    elif answerpetwrong2 == "cat":
                                                                                      print("Aw!")
                                    elif answerpetwrong2 == "bird":
                                                                                      print("Aw, such a nice buddy!")
                                    finalwrong1 = input("Alright, press enter for your dream life!")
                                    print("                                                                                                     ")
                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                    print(f"You live in a large house with {answer33} on the walls. Your {answerall33} sits quietly iat yur feet, wacthing a bird fly past the window. You look out at the streets from your window, watching the wind blow through the various plants and flowers on the sidewalk. Your happy here, this is what you've always wanted.")
                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                    quit()
     elif answerall13 == "no":
                                         print("Okay!")
                                         finalnopet3 = input("Alright, press enter for your dream life!")
                                         print("                                                                                                     ")
                                         print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                         print(f"You live in a large house with {answer33} on the walls. You look out at the streets from your window, watching the wind blow through the various plants and flowers on the sidewalk. Your happy here, this is what you've always wanted.")
                                         print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
     final3 = input("Alright, press enter for your dream life!")
     print("                                                                                                     ")
     print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
     print(f"You live in a large house with {answer33} on the walls. Your {answerall33} sits quietly at your feet, wacthing a bird fly past the window. You look out at the streets from your window, watching the wind blow through the various plants and flowers on the sidewalk. Your happy here, this is what you've always wanted.")
     print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")                                                               



if answer1 == "small house":
     answer44 = input("Would you like to live in a big city or small city? ")
     if answer44 == "small city":
          print("Nice!")
     elif answer44 == "big city":
          print("Alright!") 
     answerall14 = input("Would you like a pet? ")
     if answerall14 == "yes":
            answerall44 = input("What type of pet would you like? Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
            if answerall44 == "dog":
                                answerall4y = input("Aw! Any specific type? ")
                                if answerall4y == "bernese mountain dog":
                                    print("I have a berner too, they are the best!")
                                elif answerall4y == "no":
                                        print("Okay!")
            elif answerall44 == "rodent":
                                                    answerrodent4 = input("Cute! What kind? ")
                                                    print("Adorable!")
                                                    finalrodent4 = input("Alright, press enter for your dream life!")
                                                    print("                                                                                                     ")
                                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                                    print(f"You live in a small house in a {answer44}. Your {answerrodent4} sits quietly in your pocket, wacthing a bird fly past the window. You look out at the {answer44}, watching the streets from your window. Your happy here, this is what you've always wanted.")
                                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
            elif answerall44 == "lizard":
                                                    print("Cute!")
            elif answerall44 == "cat":
                                                    print("Aw!")
            elif answerall44 == "bird":
                                                    print("Aw, such a nice buddy!")
            else:
                                    print("Choose something from the list of options please!")
                                    answerpetwrong4 = input("Options: dog, cat, lizard, bird, rodent (hamster, mouse, chencilla etc... ")
                                    if answerpetwrong4 == "dog":
                                                                                    answerall4ywrong = input("Aw! Any specific type? ")
                                                                                    if answerall4ywrong == "bernese mountain dog":
                                                                                      print("I have a berner too, they are the best!")
                                                                                    elif answerall4ywrong == "no":
                                                                                          print("Okay!")
                                                                                    else:
                                                                                        print("Adorable!")
                                                                                  
                                    elif answerpetwrong4 == "rodent":
                                                                                            answerrodentwrong4 = input("Cute! What kind? ")
                                                                                            print("Adorable!")
                                                                                            finalrodentwrong4 = input("Alright, press enter for your dream life!")
                                                                                            print("                                                                                                     ")
                                                                                            print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                                                                            print(f"You live in a small house in a {answer44}. Your {answerrodentwrong4} sits quietly in your pocket, wacthing a bird fly past the window. You look out at the {answer44}, watching the streets from your window. Your happy here, this is what you've always wanted.")
                                                                                            print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                                                                            quit()
                                    elif answerpetwrong4 == "lizard":
                                                                                      print("Cute!")
                                    elif answerpetwrong4 == "cat":
                                                                                      print("Aw!")
                                    elif answerpetwrong4 == "bird":
                                                                                      print("Aw, such a nice buddy!")
                                    finalwrong4 = input("Alright, press enter for your dream life!")
                                    print("                                                                                                     ")
                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                    print(f"You live in a small house in a {answer44}. Your {answerpetwrong4} sits quietly at your feet, wacthing a bird fly past the window. You look out at the {answer44}, watching the streets from your window. Your happy here, this is what you've always wanted.")
                                    print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                    quit()
     elif answerall14 == "no":
                                         print("Okay!")
                                         finalnopet4 = input("Alright, press enter for your dream life!")
                                         print("                                                                                                     ")
                                         print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
                                         print(f"You live in a small house in a {answer44}. You look out at the {answer44}, watching the streets from your window. Your happy here, this is what you've always wanted.")
                                         print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
     final3 = input("Alright, press enter for your dream life!")
     print("                                                                                                     ")
     print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")
     print(f"You live in a small house in a {answer44}. Your {answerall44} sits quietly at your feet, wacthing a bird fly past the window. You look out at the {answer44}, watching the streets from your window. Your happy here, this is what you've always wanted.")
     print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*")           

