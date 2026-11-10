import room_data
import random
import sys



def run_game():                     # title screen loop.
    while True:
        choice = room_data.title_screen()
        if choice == 1:
            main()
        elif choice == 2:
            room_data.how_to_play()
        else:
            break

def main():
    #obtains the player name.
    name = room_data.obtain_name()

    while True:
        risk = 0
        #creates room objects for each room
        room1 = room_data.Room1()
        room2 = room_data.Room2()
        room3 = room_data.Room3()

        # Play through the rooms

        risk = room1.play(name, risk)
        detection_roll = random.randint(1, 100)
        if risk is None:
            return  # Player chose to return to title
        elif detection_roll <= risk:
            choice = room_data.game_over_room1(risk, detection_roll)
            if choice == 1:
                continue #ends the current pass of the inner loop. Starts at the top of the inner loop (Scene 1 again)
            elif choice == 2: 
                return #Ends the main function, returning to the title screen loop (Run game function)
            elif choice == 3:
                sys.exit()
            


        risk = room2.play(name, risk)
        detection_roll = random.randint(1, 100)
        if risk is None:
            return  # Player chose to return to title
        elif detection_roll <= risk:
                    choice = room_data.game_over_room2(risk, detection_roll)
                    if choice == 1:
                        continue
                    elif choice ==2: 
                        return
                    elif choice == 3:
                        sys.exit()


        
        risk = room3.play(name, risk, room2.choice)
        detection_roll = random.randint(1, 100)
        if risk is None:
            return  # Player chose to return to title
        elif detection_roll <= risk:
        
            if room3.choice == 1:
                choice = room_data.game_over_room3_rush(risk, detection_roll)
            else:
                choice = room_data.game_over_room3_provision(risk, detection_roll)

            if choice == 1:
                continue                # Retry
            elif choice == 2:
                return                  # Return to Title
            else:
                sys.exit()              # Quit
        else:
            room_data.victory(name, risk)
            choice = room_data.victory(name, risk)
            if choice == 1:
                continue                # Play again
            elif choice == 2:
                return                  # Return to Title
            else:
                sys.exit()              # Quit
    
# Starts the game by calling the run_game() function, which displays the title screen and handles user input to start the game, view instructions, or quit.
run_game()
