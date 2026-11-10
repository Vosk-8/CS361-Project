LINE = "_" * 52

def ask(num_choices):
    """Keep asking until the player types a valid number."""
    while True:
        raw = input("> ").strip()
        if raw.isdigit() and 1 <= int(raw) <= num_choices:
            return int(raw)
        print("Please type one of the listed numbers.")

def title_screen():
    print(LINE)
    print ("FULL METAL SPROCKET")
    print("A GAME OF TACTICAL ESPIONAGE ACTION")
    print("A game made by Adonai Garcia")
    print(LINE)
    print("1.) Start Game")
    print("2.) How To Play")
    print("3.) Quit")
    print(LINE)
    return ask(3)
    

def obtain_name():
    repeat = True
    while repeat:
        name = input("Enter agent name, must be 1-20 characters. Press enter without typing to be called 'agent': ")
        if name == "":
            name = "agent"
            repeat = False
            return name
            
        elif len(name) > 20 or len(name) < 1:
            print("agent name must be 1-20 characters. Please try again.")
        else:
            repeat = False
            return name
            

def game_over_room1(risk,detection_roll):
    print(LINE)
    print("Sadly, the guard noticed you trying to dash through the door. He quickly arrests you, and your mission ends in a quick, decisive failure.\n")
    print(f"Detection risk {risk}% | Your Roll {detection_roll}| Rolls between 1 and {risk} get you caught.\n")
    print("GAME OVER")
    print("1.) Retry (starts over at Scene 1, risk resets to 0%)\n")
    print("2.) Return to Title")
    print("3.) Quit")
    print(LINE)
    return ask(3)

def game_over_room2(risk,detection_roll):
    print(LINE)
    print("With a metallic clatter the provision tin hits the floor, as you clumsily drop it.\n")
    print("The guards quickly arrive at your location. You are able to fend off some of them, but you are eventually overwhelmed by the constant influx of guards.\n")
    print(f"Detection risk {risk}% | Your Roll {detection_roll}| Rolls between 1 and {risk} get you caught.\n")
    print("GAME OVER")
    print("1.) Retry (starts over at Scene 1, risk resets to 0%)\n")
    print("2.) Return to Title")
    print("3.) Quit")
    print(LINE)
    return ask(3)

def game_over_room3(risk,detection_roll):
    print(LINE)
    print("Even with the provision tossed, the sound of your footsteps is louder than the provision tin hitting the ground.\n")
    print(" Before you can plant the C4 charge, the guards take you down. You were almost there, close but no cigar!\n")
    print(f"Detection risk {risk}% | Your Roll {detection_roll}| Rolls between 1 and {risk} get you caught.\n")
    print("GAME OVER")
    print("1.) Retry (starts over at Scene 1, risk resets to 0%)\n")
    print("2.) Return to Title")
    print("3.) Quit")
    print(LINE)
    return ask(3)

def victory(name,risk):
    print(LINE)
    print("With quick speed and finesse, you plant the C4 charge and quickly escape the base!\n")
    print(" With a loud bang, the entire Metal Sprocket base is engulfed in flames.\n")
    print(f"With the base destroyed, your mission is successful {name}!\n")
    print(f"Final detection risk: {risk}%\n")
    print("CONGRATULATIONS! YOU WIN!")
    print("GAME OVER")
    print("1.) Play again (starts over at Scene 1, risk resets to 0%)\n")
    print("2.) Return to Title")
    print("3.) Quit")
    print(LINE)
    return ask(3)
    

def game_over_room3_rush(risk,detection_roll):
    print(LINE)
    print("The guards quickly hear your footsteps as you rush toward Metal Sprocket.\n")
    print("Before you can plant the C4 charge, they take you down. You were almost there, close but no cigar!\n")
    print(f"Detection risk {risk}% | Your Roll {detection_roll}| Rolls between 1 and {risk} get you caught.\n")
    print("GAME OVER")
    print("1.) Retry (starts over at Scene 1, risk resets to 0%)\n")
    print("2.) Return to Title")
    print("3.) Quit")
    print(LINE)
    return ask(3)

def game_over_room3_provision(risk,detection_roll):
    print(LINE)
    print("The guards quickly hear the sound of the provision tin hitting the ground.\n")
    print("Before you can plant the C4 charge, they take you down. You were almost there, close but no cigar!\n")
    print(f"Detection risk {risk}% | Your Roll {detection_roll}| Rolls between 1 and {risk} get you caught.\n")
    print("GAME OVER")
    print("1.) Retry (starts over at Scene 1, risk resets to 0%)\n")
    print("2.) Return to Title")
    print("3.) Quit")
    print(LINE)
    return ask(3)


def how_to_play():
    print(LINE)
    print(f"Goal: Sneak into the terrorist base and destroy the Metal Sprocket weapon. A mission has 3 scenes and takes about 3 minutes.\n")
    print(f"Each scene, choose an action by typing its number. Every action adds to your Detection Risk, then the game rolls a number from 1 to 100.\n")
    print(f" If the roll is between 1 and your total risk, you are caught.\n")
    print(f"Example: at 40% risk, rolls of 1-40 get you caught.\n")
    print(f"Risk adds up across scenes. Retrying resets it to 0%.\n")
    print(f"Good luck, agent. You will need it.\n")
    print(f"1.) Return to Title")
    print(LINE)
    return ask(1)
    




class Room1:
    def play(self, name, risk):
        print(f"Scene 1 of 3 | Detection risk: {risk}%")
        print(LINE)
        print(f"You are special agent {name}. You are tasked with stopping the "
              "activation of a dangerous nuclear weapon named Metal Sprocket.\n"
              "You have snuck onto the terrorists' base and are hiding among the "
              "cargo crates and other supplies. Ahead of you is a lone guard, "
              "patrolling and guarding the door to the armory.\n"
              "To succeed, you need to sneak past the guard. How do you do this?")
        print(LINE)
        print("(Type a number and press Enter)")
        print("1.) Quietly sneak into the armory (+0% risk: none)")
        print("2.) Rush past the guard when their back is turned (+40% risk: High)\n")
        print("3.) Return to Title (ends this mission)")

        choice = ask(3)
        if choice == 1:
            return risk + 0
        elif choice == 2:
            return risk + 40
        else:
            return None          # None means "back to title"


class Room2:
    def __init__(self):
        self.choice = 0                  
    def play(self, name, risk):
        print(f"Scene 2 of 3 | Detection risk: {risk}%\n")
        # ...same pattern: print the scene, call ask(), return the new risk
        print(LINE)
        print(f"You slip past the guard and go into the armory. You find a sizable amount of C4 explosives.\n")
        print(f"You then advance to the next room, a storage area for provisions with only 2 guards patrolling nearby.\n")
        print(f"A provision could serve as a valuable distraction later, but grabbing a bigger one can draw more attention from the guards. What do you do?\n")
        print(LINE)
        print("(Type a number and press Enter)")
        print("1.) Grab a small provision (+0% risk: none)")
        print("2.) Grab a large provision (+20% risk: medium). Throwing it later is more effective than the small provision.\n")
        print("3.) Return to Title (ends this mission)")

        choice = ask(3)
        self.choice = choice
        if choice == 1:
            return risk + 0
        elif choice == 2:
            return risk + 20
        else:
            return None          # None means "back to title"


class Room3:
    def __init__(self):
        self.choice = 0
    def play(self, name, risk,room2_choice):
        print(f"Scene 3 of 3 | Detection risk: {risk}%\n")
        # ...same pattern
        print(LINE)
        print(f"You grab the provision and continue deeper into the base. There it is!\n")
        print(f"You find Metal Sprocket in its hangar. There are dozens of guards.\n")
        print(f" Metal Sprocket must be destroyed, but you could distract the guards first. What do you do?\n")
        print(LINE)
        print("(Type a number and press Enter)")
        print(f"1.) Rush to Metal Sprocket and attach C4 charge (+40% risk: high)\n")
        if room2_choice == 2:
            print("2.) Throw your provision to distract the guards (+0% risk: none)\n")
        else:
            print("2.) Throw your provision to distract the guards (+10% risk: low)\n")
        print(f"3.) Return to Title (ends this mission)")

        choice = ask(3)
        self.choice = choice            
        if choice == 1:
            return risk + 40
        elif choice == 2:
            if room2_choice == 2:
                return risk + 0
            else:
                return risk + 10
        else:
            return None


              


