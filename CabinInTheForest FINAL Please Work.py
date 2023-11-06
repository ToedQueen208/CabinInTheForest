import os
import sys

#region variables
name = ""
choice = False
errorCounter = 0
health = 100
#endregion

#region functions
def check_Health():
    if health <= 0:
        print("you died RIP")
        sys.exit()

def add_Health(value):
   global health
   health = health + value
   return health

def subtract_Health(value):
     global health
     health = health - value
     value
     return health 
#endregion

#region pickup Key
def pickup_Key_Event():
    print("Pick up the key to escape the cabin")
    print("You need to get out now!!")
    add_Health(15)
    check_Health()
    print("Current Health: ", health)

    print("A: stab clown with key or B run upstairs")
    choice = False
    while choice == False:
         answer = input("what do you choose A or B: ").upper()
         if answer == "A" or answer == "B":
            choice = True
            continue
         else:
            print("please select from the options")
            choice = False

    if answer == "A":
          print("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⢹⠀⠀⡀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠴⣶⣶⣺⣿⣼⣄⠀⣟⣇⠀⢠⠀⠀⠀⣿⠀⠀⠀⡿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⢀⣤⡿⠚⣹⣧⣶⠟⣏⢛⢹⣿⣿⢉⠉⡏⡿⣿⢻⠶⣤⣰⣷⡇⠠⣰⣿⣇⢀⠆⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⠀⣸⡟⡋⢸⡆⢰⣿⣷⣄⣸⣏⣏⣹⣿⣿⡄⣸⣷⣿⣇⡟⢀⣴⣿⡟⡿⢶⣿⡟⣿⣮⣀⣠⣞⠁⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⣿⣠⣞⣽⣿⡿⢿⣷⣄⣿⣟⣧⣽⣿⣟⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⠟⣼⣿⣿⣷⡟⠿⢧⣄⡀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⢱⡄⠀⣄⣿⣿⡉⠁⢻⣿⣥⡽⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣯⣿⣿⣯⣿⣿⣿⡿⡻⠿⣶⡾⠋⢉⣶⡿⠥⠄⣠⠞⠀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠸⣆⠀⢹⣭⣿⣅⠘⣿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣻⡯⣪⣥⡶⠛⣻⣶⣿⢏⠀⣠⣟⡁⢠⠀⢈⡀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⣼⠀⠘⣶⣾⠏⣿⣿⢿⣿⣿⣿⣿⡿⠟⢉⣽⣿⣿⣿⠿⠛⠉⠉⠁⠀⠀⠈⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣷⣟⣩⣏⣹⠿⠁⣰⠃⢀⡜⠀
⠀⠀⠀⠀⠀⠀⢻⣥⡴⢋⣹⣿⣿⣽⣿⣿⣿⡿⠏⠀⣠⣿⣿⡿⠋⠀⠀⠀⠀⣀⣀⣤⣤⣄⣀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⣿⣶⡾⣷⣶⣾⡟⢉⣾⡇⠀
⠀⠀⠀⠀⠰⠂⣠⡿⣷⣾⣿⣷⣿⣿⣿⣿⠃⠀⠀⢰⣿⣿⠋⠀⠀⠀⢀⣶⣿⣿⣿⠿⠿⣿⣿⣿⣷⣄⠀⠀⠀⠈⢿⣿⣿⣻⢿⣿⣿⣿⣿⣤⣤⣾⣟⣻⣿⣿⣏⣴⡿⢋⣴⠛
 ⠀⠀⠀⠀⠀⣺⣏⣾⠟⣻⣿⣿⠇⣿⣿⡇⠀⠀⢀⣿⣿⡏⠀⠀⠀⢰⣿⣿⠟⠉⠀⠀⠀⠀⠉⠻⣿⣿⣷⡀⠀⠀⠀⢻⣿⣿⢣⡙⢿⣿⣿⣿⣿⣯⣿⣶⣾⡿⣟⣭⣶⡾⠋⠀
⠀⠠⢤⡆⣴⣳⣿⢿⣿⡿⠟⠁⠀⣿⣿⠁⠀⠀⠸⣿⣿⡇⠀⠀⠀⢸⣿⣿⣤⣤⣴⣶⣦⡀⠀⠀⠈⢿⣿⣷⠀⠀⠀⠘⣿⣿⡆⢻⠠⠟⠿⣿⣿⣿⣿⣟⡛⣻⣿⠟⠋⣀⢀⠀
⠀⠀⠀⣙⣿⣿⣿⣿⠋⣴⡄⠀⠀⣿⣿⡆⠀⠀⠀⢻⣿⣷⡀⠀⠀⠈⠻⠿⠿⠟⠛⣿⣿⣧⠀⠀⠀⢸⣿⣿⡄⠀⠀⠀⣿⣿⣇⡟⠀⠀⠀⢲⣿⣿⣿⣿⣿⣿⣶⣶⣾⡿⠟⠀
⠀⣀⣠⣿⣟⣷⡿⢁⡾⢸⡁⠀⠀⢻⣿⣷⡀⠀⠀⠈⢿⣿⣿⣤⣀⠀⠀⠀⠀⢀⣰⣿⣿⡏⠀⠀⠀⢸⣿⣿⠁⠀⠀⢠⣿⣿⡟⠀⠀⠀⢠⣿⢿⣢⡻⢿⠙⢿⣛⣏⠁⠀⠀⠀
⢠⣾⣿⠟⣽⡟⡇⠙⢿⢄⣇⠀⠀⠀⢿⣿⣷⡄⠀⠀⠀⠙⠿⣿⣿⣿⣷⣶⣿⣿⣿⡿⠋⠀⠀⠀⣠⣿⣿⡟⠀⠀⠀⣾⣿⠋⠀⠀⢀⢀⣿⡿⢷⣾⣿⣯⣄⣹⡿⠋⠀⠀⠀⠀
⠀⠉⠁⢰⣿⠁⣳⡅⠈⣦⡝⣤⡀⠀⠈⠻⣿⣿⣦⡀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⢀⣴⣿⣿⠟⠀⠀⢀⣾⠟⠁⠀⠀⢠⣬⣿⣿⣿⣞⠇⢳⡌⢿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⡿⢧⡀⠉⣩⣤⣧⣈⠙⠺⠶⣤⣄⡈⠻⣿⣿⣷⣦⣤⣀⡀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⠟⠁⠀⢀⣴⠟⠁⠀⢀⣤⣾⣿⣿⠿⣾⠷⣿⣆⡼⠓⣾⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⢦⣉⣉⣀⠤⡜⠉⠛⢶⣤⣄⣀⣉⡉⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠁⣠⠴⠞⣉⣀⣀⣤⣶⢶⣻⣿⡵⣘⠢⠈⣦⠘⢿⠇⢰⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠛⠛⠛⢧⣤⡴⠋⠀⠈⢻⡿⠾⢿⣷⣶⣤⣴⣆⣌⣭⣉⣩⣭⣉⠀⣄⡤⣄⢠⣤⣄⣠⣴⠾⣿⡿⣏⠘⠻⣧⡘⣿⡜⠶⠄⠈⢤⠞⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣯⣭⣽⣳⢦⣉⠲⢤⣠⠏⠀⠀⡼⣱⠋⢹⣿⢻⠟⠛⡟⣿⠟⢻⠟⣟⢿⠻⣟⠛⢯⢻⣯⣆⠘⣿⡌⢳⣄⢻⣷⠈⠀⠀⢀⡤⠋⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠉⠉⠻⢷⣌⠙⠲⣽⡃⠀⠀⢷⠇⠀⠸⠁⡞⠀⡀⠙⡟⠂⠀⡟⢿⣼⠀⠹⡇⠈⢧⣎⢿⣇⠸⠿⠀⠉⢮⠏⠃⢀⡴⠊⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⡀⠉⠓⢦⣞⠀⠀⠀⠀⠁⠀⠀⠀⡇⠈⠳⡷⠀⡿⠴⠀⠘⠀⠸⠋⠻⣿⠀⠀⠁⠈⢈⡧⠞⠁⠀⠀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠉⠓⠦⣄⣀⠀⠀⠀⠁⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠲⠤⢤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               
  _   _, _  _, , _   _,_  _, _,_ __,    _, _, _ __,   __, , _ __,     __, _,_ ___   _    _, __, __,   , _  _, _,_
   |   |\/| /_\ \ |   |_| /_\ | / |_    / \ |\ | |_    |_  \ | |_      |_) | |  |    |   (_  |_  |_    \ | / \ | |
   |   |  | | |  \|   | | | | |/  |     \ / | \| |     |    \| |   ,   |_) | |  |    |   , ) |   |      \| \ / | |
   ~   ~  ~ ~ ~   )   ~ ~ ~ ~ ~   ~~~    ~  ~  ~ ~~~   ~~~   ) ~~~ '   ~   `~'  ~    ~    ~  ~~~ ~~~     )  ~  `~'
                ~'                                         ~'                                          ~'        
               """)
          print("you stabby stab stab")
          input("press enter to continue")
          clown_Cave_event()
    elif answer == "B":
        print("you run away")
        runUpstairsEvent()

#endregion

#region pick up axe
def pickup_Axe_Event():  
    print("You enter the forest. You are immediately surrounded by darkness and silence.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You can hear the sound of your own heartbeat, and you can feel the hairs on the back of your neck stand up.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You see a pair of glowing eyes in the darkness, and you realize that you are not alone....")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Ahead there is a crooked bridge across the blood blackened river...which leads into the tall twisted trees.") 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    answer = input()
    if answer == "A":
        print("picked up axe")
    elif answer == "B":
        print("ran across the bridge")

#endregion

#region run upstairs
def runUpstairsEvent():
    print("As you are running upstairs in complete blackness!")
    print("You notice  a light!! It is coming from the bedroom, you can hear the tiny clown frantically laughing")
    print("His voice draws closer! And closer!")
    print("So player, what will you do?")
    print("Choose a = Enter the bedroom ? ")
    print("Choose b = Enter the bathroom ? ")

    print("_______________________________________________________________________________________________________________________________________________")
    print("_______________________________________________________________________________________________________________________________________________")
    #prints the statement "As you are running  etc=========================================================================================================}
    #this variable stores the plyers inputs which leads them to a specific outcome========================================================================+}
    #======================================================================================================================================================}
    choice = False
    while choice == False:
        answer = input ("Choose a or b").lower()
        if answer == "a" or answer == "b": #if they choose the correct answer
            choice = True
            continue
        else:
            print("please section one of the options")
            choice = False

    
    #OPTION  A ENTER BEDROOM===============================================================================================================================}
    #defines the answer input as a or b====================================================================================================================}
    if answer == "a":
        print("You entered the bedroom, as you fling open the door")
        print("___________________________________________________________________________________________________________________________________________")
        print("You get a suprise.. A man stands in the corner!!")
        print("___________________________________________________________________________________________________________________________________________")
        print("his face is filled with maggots, his eyes are bloodshot and sunken.")
        print("___________________________________________________________________________________________________________________________________________")
        print("You are scared, quickly will you stab him in the eye, or run and escape!")
        print("___________________________________________________________________________________________________________________________________________")
        print("Choose a = STAB IN THE EYE ? ")
        print("Choose b = JUMP OUT OF THE WINDOW ? ")
        #this variable stores the players answer
   
        choice = False
        while choice == False:
            answer = input ("Choose A or B").upper()
            if answer == "A" or answer == "B": #if they choose the correct answer
                choice = True
                continue
            else:
                print("please section one of the options")
                choice = False

        if answer == "A":
            print("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⢹⠀⠀⡀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠴⣶⣶⣺⣿⣼⣄⠀⣟⣇⠀⢠⠀⠀⠀⣿⠀⠀⠀⡿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⢀⣤⡿⠚⣹⣧⣶⠟⣏⢛⢹⣿⣿⢉⠉⡏⡿⣿⢻⠶⣤⣰⣷⡇⠠⣰⣿⣇⢀⠆⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⠀⣸⡟⡋⢸⡆⢰⣿⣷⣄⣸⣏⣏⣹⣿⣿⡄⣸⣷⣿⣇⡟⢀⣴⣿⡟⡿⢶⣿⡟⣿⣮⣀⣠⣞⠁⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⣿⣠⣞⣽⣿⡿⢿⣷⣄⣿⣟⣧⣽⣿⣟⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⠟⣼⣿⣿⣷⡟⠿⢧⣄⡀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⢱⡄⠀⣄⣿⣿⡉⠁⢻⣿⣥⡽⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣯⣿⣿⣯⣿⣿⣿⡿⡻⠿⣶⡾⠋⢉⣶⡿⠥⠄⣠⠞⠀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠸⣆⠀⢹⣭⣿⣅⠘⣿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣻⡯⣪⣥⡶⠛⣻⣶⣿⢏⠀⣠⣟⡁⢠⠀⢈⡀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⣼⠀⠘⣶⣾⠏⣿⣿⢿⣿⣿⣿⣿⡿⠟⢉⣽⣿⣿⣿⠿⠛⠉⠉⠁⠀⠀⠈⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣷⣟⣩⣏⣹⠿⠁⣰⠃⢀⡜⠀
⠀⠀⠀⠀⠀⠀⢻⣥⡴⢋⣹⣿⣿⣽⣿⣿⣿⡿⠏⠀⣠⣿⣿⡿⠋⠀⠀⠀⠀⣀⣀⣤⣤⣄⣀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⣿⣶⡾⣷⣶⣾⡟⢉⣾⡇⠀
⠀⠀⠀⠀⠰⠂⣠⡿⣷⣾⣿⣷⣿⣿⣿⣿⠃⠀⠀⢰⣿⣿⠋⠀⠀⠀⢀⣶⣿⣿⣿⠿⠿⣿⣿⣿⣷⣄⠀⠀⠀⠈⢿⣿⣿⣻⢿⣿⣿⣿⣿⣤⣤⣾⣟⣻⣿⣿⣏⣴⡿⢋⣴⠛
 ⠀⠀⠀⠀⠀⣺⣏⣾⠟⣻⣿⣿⠇⣿⣿⡇⠀⠀⢀⣿⣿⡏⠀⠀⠀⢰⣿⣿⠟⠉⠀⠀⠀⠀⠉⠻⣿⣿⣷⡀⠀⠀⠀⢻⣿⣿⢣⡙⢿⣿⣿⣿⣿⣯⣿⣶⣾⡿⣟⣭⣶⡾⠋⠀
⠀⠠⢤⡆⣴⣳⣿⢿⣿⡿⠟⠁⠀⣿⣿⠁⠀⠀⠸⣿⣿⡇⠀⠀⠀⢸⣿⣿⣤⣤⣴⣶⣦⡀⠀⠀⠈⢿⣿⣷⠀⠀⠀⠘⣿⣿⡆⢻⠠⠟⠿⣿⣿⣿⣿⣟⡛⣻⣿⠟⠋⣀⢀⠀
⠀⠀⠀⣙⣿⣿⣿⣿⠋⣴⡄⠀⠀⣿⣿⡆⠀⠀⠀⢻⣿⣷⡀⠀⠀⠈⠻⠿⠿⠟⠛⣿⣿⣧⠀⠀⠀⢸⣿⣿⡄⠀⠀⠀⣿⣿⣇⡟⠀⠀⠀⢲⣿⣿⣿⣿⣿⣿⣶⣶⣾⡿⠟⠀
⠀⣀⣠⣿⣟⣷⡿⢁⡾⢸⡁⠀⠀⢻⣿⣷⡀⠀⠀⠈⢿⣿⣿⣤⣀⠀⠀⠀⠀⢀⣰⣿⣿⡏⠀⠀⠀⢸⣿⣿⠁⠀⠀⢠⣿⣿⡟⠀⠀⠀⢠⣿⢿⣢⡻⢿⠙⢿⣛⣏⠁⠀⠀⠀
⢠⣾⣿⠟⣽⡟⡇⠙⢿⢄⣇⠀⠀⠀⢿⣿⣷⡄⠀⠀⠀⠙⠿⣿⣿⣿⣷⣶⣿⣿⣿⡿⠋⠀⠀⠀⣠⣿⣿⡟⠀⠀⠀⣾⣿⠋⠀⠀⢀⢀⣿⡿⢷⣾⣿⣯⣄⣹⡿⠋⠀⠀⠀⠀
⠀⠉⠁⢰⣿⠁⣳⡅⠈⣦⡝⣤⡀⠀⠈⠻⣿⣿⣦⡀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⢀⣴⣿⣿⠟⠀⠀⢀⣾⠟⠁⠀⠀⢠⣬⣿⣿⣿⣞⠇⢳⡌⢿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⡿⢧⡀⠉⣩⣤⣧⣈⠙⠺⠶⣤⣄⡈⠻⣿⣿⣷⣦⣤⣀⡀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⠟⠁⠀⢀⣴⠟⠁⠀⢀⣤⣾⣿⣿⠿⣾⠷⣿⣆⡼⠓⣾⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⢦⣉⣉⣀⠤⡜⠉⠛⢶⣤⣄⣀⣉⡉⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠁⣠⠴⠞⣉⣀⣀⣤⣶⢶⣻⣿⡵⣘⠢⠈⣦⠘⢿⠇⢰⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠛⠛⠛⢧⣤⡴⠋⠀⠈⢻⡿⠾⢿⣷⣶⣤⣴⣆⣌⣭⣉⣩⣭⣉⠀⣄⡤⣄⢠⣤⣄⣠⣴⠾⣿⡿⣏⠘⠻⣧⡘⣿⡜⠶⠄⠈⢤⠞⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣯⣭⣽⣳⢦⣉⠲⢤⣠⠏⠀⠀⡼⣱⠋⢹⣿⢻⠟⠛⡟⣿⠟⢻⠟⣟⢿⠻⣟⠛⢯⢻⣯⣆⠘⣿⡌⢳⣄⢻⣷⠈⠀⠀⢀⡤⠋⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠉⠉⠻⢷⣌⠙⠲⣽⡃⠀⠀⢷⠇⠀⠸⠁⡞⠀⡀⠙⡟⠂⠀⡟⢿⣼⠀⠹⡇⠈⢧⣎⢿⣇⠸⠿⠀⠉⢮⠏⠃⢀⡴⠊⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⡀⠉⠓⢦⣞⠀⠀⠀⠀⠁⠀⠀⠀⡇⠈⠳⡷⠀⡿⠴⠀⠘⠀⠸⠋⠻⣿⠀⠀⠁⠈⢈⡧⠞⠁⠀⠀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠉⠓⠦⣄⣀⠀⠀⠀⠁⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠲⠤⢤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               
  _   _, _  _, , _   _,_  _, _,_ __,    _, _, _ __,   __, , _ __,     __, _,_ ___   _    _, __, __,   , _  _, _,_
   |   |\/| /_\ \ |   |_| /_\ | / |_    / \ |\ | |_    |_  \ | |_      |_) | |  |    |   (_  |_  |_    \ | / \ | |
   |   |  | | |  \|   | | | | |/  |     \ / | \| |     |    \| |   ,   |_) | |  |    |   , ) |   |      \| \ / | |
   ~   ~  ~ ~ ~   )   ~ ~ ~ ~ ~   ~~~    ~  ~  ~ ~~~   ~~~   ) ~~~ '   ~   `~'  ~    ~    ~  ~~~ ~~~     )  ~  `~'
                ~'                                         ~'                                          ~'        
               """)
            input("press enter to continue")
            print("You Stabbed the man in the eye, he stil sees you. You run down the stairs")
            print("You make it to the kitchen doorway")
            print("A black cat runs past your feet, blood is trailing from its mouth")
            print("The trail leads you to a key! You collect it and try to open the backdoor! ")
            print("Its open! You are now in the Forest...survive this and you might just make it out of here!")
            input("press enter to continue")
            print("___________________________________________________________________________________________________________________________________________")
            clown_Cave_event()
    elif answer == "b":
        print("You open the bathroom door, there is a woman in the bath!")
        print("______________________________________________________________________________________________________________________________________________________________")

        print("She is dead!!! Spiders and bugs are crawling out of her mouth.")
        print("______________________________________________________________________________________________________________________________________________________________")

        print("You being to feel dizzy, you feel sick, you lose your balance")
        print("______________________________________________________________________________________________________________________________________________________________")

        print("You fainted!")
        counter = 0
        print("press a 3 times to wake up")
        for i in range(0,3):
            answer = input("press a:").lower()
            if answer == "a":
                counter +=1
        if counter == 3:
         print("you wake up")
        else:
            print("You woke up too slowly and lose 25% health")
            subtract_Health(25)
            print("Current Health: ", health)
            check_Health()

    input("press enter to continue")
    clown_Cave_event()

#endregion
  
#region exitgateeast
def tree_exit_gateeast():
 
    print("Zombies begin to chase you through the trees, you arent fast enough!")
    print(" A zombie jumps up and bites your neck just as you push open the gate")
    print("You pull your hand from your neck and see it is covered in blood...")
    print("then a gravewalker appears....towering the gate his maggot infested face is shielded by his cloak.")
    print("YOU MADE UNWISE CHOICES! YOU BECAME THE FEAST")
    print("""            ...                            
                     ;::::;                           
                     ;::::; :;                          
                    ;:::::'   :;                         
                    ;:::::;     ;.                        
                    ,:::::'       ;           OOO\         
                    ::::::;       ;          OOOOO\        
                    ;:::::;       ;         OOOOOOOO       
                    ,;::::::;     ;'         / OOOOOOO     
                    ;:::::::::`. ,,,;.        /  / DOOOOOO 
                .';:::::::::::::::::;,     /  /     DOOOO   
                ,::::::;::::::;;;;::::;,   /  /        DOOO  
                ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
                :`:::::::`;::::::;;::: ;::#  /            DOOO
                ::`:::::::`;:::::::: ;::::# /              DOO
                `:`:::::::`;:::::: ;::::::#/               DOO
                :::`:::::::`;; ;:::::::::##                OO
                ::::`:::::::`;::::::::;:::#                OO
                `:::::`::::::::::::;'`:;::#                O 
                `:::::`::::::::;' /  / `:#                  
                    ::::::`:::::;'  /  /   `#              """)
    print("YOU DIED")
    print("Don't go into cabins in the woods!!! Especially in a zombie apocalypse!") 
#endregion
#region exitgates
def tree_exit_Gates():
        print("You make your way through the tress, you see the gate in the distance, and then!")
        print("The trees begin to sway and seem to whisper, voices emerge from the trees")
        print("Welcome to the twisted trail, your almost at the end but heed my voice")
        print("Listen to my tale , then make a choice")
        print("I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I? ")
        print(" A = Tiny Killer Clown b = Your shadow")
        choice = False
        while choice == False:
            answer = input ("Choose a or b").upper()
            if answer == "A" or answer == "B": #if they choose the correct answer
                choice = True
                continue
            else:
                print("please section one of the options")
                choice = False

        if answer == "A":
            print(" Your shadow...you lost health, will you survive? press A now to exit the gate")
            subtract_Health(15)
            print("Current Health: ", health)
            check_Health()
        elif answer == "B":
            print("correct answer you gain some health")
            add_Health(15)
            print("Current Health: ", health)
            check_Health()
        input("press enter to continue")
        print("""
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣀⣠⠤⡒⢓⣒⢤⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⡠⠖⠉⠛⠛⠻⠛⠛⠉⠙⠀⠀⠐⠀⠀⠀⠷⣌⠢⡀⠀⠀⠀⠀⠀
        ⠀⠰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣳⣼⠂⠀⠀⠀⠀
        ⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠸⣄⠀⠀⠀⠀
        ⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣠⣤⣤⣤⣦⣎⡌⢱⡀⠀⠀
        ⡄⠁⠀⡀⡀⠀⡀⠀⠀⡀⠀⠀⠀⣤⣼⣿⡷⢋⣉⣉⢻⣿⣿⣆⢳⡀⠀
        ⢁⠀⣬⣾⡶⠶⠷⣶⡨⣇⠀⠀⣆⣿⣿⣿⣅⣸⣽⡻⠈⣽⣿⠿⣬⣇
        ⢸⠀⣿⣏⢰⣶⣦⣃⣭⡟⠀⠀⢹⢿⣟⠿⣯⠞⠥⠠⠂⠛⠁⠐⢫⣿⠀                                                                                                             
        ⠠⡆⠸⣯⣚⡿⢟⡽⡹⠁⠀⠀⠸⣷⣮⡂⠀⠙⠂⠄⠀⠀⠀⠀⠈⠸⡄                                                                                                               
        ⠀⣧⠀⠙⠻⠶⠴⠟⠀⡔⠀⠀⢀⣟⠻⢿⣆⠀⠀⠀⠀⠀⠀⠀⢀⠞           
        ⠀⢹⠀⠀⠀⠀⠀⠀⠀⡀⣶⣄⠸⣿⣷⣸⠟⠆⠀⠀⠀⠜⣬ ;;          
                                     ;;             
                                    ;;               
        ⠀⠀⢧⠀⠀⠀⠀⠀⠀⠍⠒⠃⠀⠁⠀⠈⠀⠀⠀⠀⠀⠀⠁⡇⠀⠀⠀                                                                                                                    
        ⠀⠀⠈⠲⣌⠀⠀⠀⠀⠀⠀⣀⣖⣠⣤⣤⣀⣀⠀⠀⠀⠀⠀⡇⠀⠀⠀                                                                                                                   
        ⠀⠀⠀⠀⠙⢮⣠⠀⠀⣠⣾⡟⣿⢑⣏⢿⣄⣿⣽⣾⣄⠀⠀⡇⠀⠀⠀                                                                                                                 
        ⠀⠀⠀⠀⠀⠀⢳⡀⢠⡿⢷⢿⢿⣿⠿⠟⢛⠯⠋⠀⠀⠀⢰⠇⠀⠀⠀                                                                                                                
                  ⢳     ⠐⠁       ⡜o
        ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣆⠀⠀⠀⢀⣄⣀⡤⠒⠁⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

              """)
        print("You are facing a Seven foot tall wrought iron gate, at its peak the face of a gargoyle seems to be smiling at you....")
        print("then a gravewalker appears....towering the gate his maggot infested face is shielded by his cloak.")
        print("Congratulations Day walker YOU WIN!! ")
        print("ACSII ART===============================================================================================")
        print("You survived the Feasting Forest with {} health by making wise decisions.".format(health))
        print("But there was an even wiser decision...")
        print("Don't go into cabins in the woods!!! Especially in a zombie apocalypse!") 
        sys.exit()
#endregion

#region ClownCave
def clown_Cave_event():

     print("You enter the forest. You are immediately surrounded by darkness and silence.")
     print("You can hear the sound of your own heartbeat, and you can feel the hairs on the back of your neck stand up.")
     print("You see a pair of glowing eyes in the darkness, and you realize that you are not alone....")
     print("Ahead there is a crooked bridge across the blood blackened river...which leads into the tall twisted trees.") 
     input("press enter to continue")

     print("""
                        _,,--.._
                       /. ` ` .  `.
                      )|       `  `.
         .           / |         `  `
          `.        / /            ` `
           `.`.    / /              ` `
             `.`.'' /                ' :
              <','/'`                . ;
             ,-'.-    `             , /
         _.-',-^`       `      _.-----
   /`==::.,-'     `       ` ,-'
 / /               `     .;
 | |..               ` .,' `.
 | ':`....---.       ,'`'.   `.
   .`:.:.:.:.:-..    /     `.   `.
   .`ccoccoccoc'``./        `.   `.
    `.`CQCCQCCCQCC/           `.   `.
      `.`8O8O8O8O8(             `.   `.
         `.`_-_@-@_-;              `. .'"'.
              '""'                   :,' ,--'
                                      `.` _,--
               S                        `.  _,',.
              (@)                         `. .-' `_
                                            `. ,-^.`.
                 W                            `. - _.-.
                (@)                             `.', ,'-
                                                  `. _,-`__
                                                    `. _-,`|
                                                      |,_-`|
#   PICK UP THE AXE TO INCREASE YOUR HEALTH           '----' """)
     print(" A: CROSS THE BRIDGE  OR B:PICK UP AXE ")
     choice = False
     while choice == False:
        answer = input ("Choose a or b").lower()
        if answer == "a" or answer == "b": #if they choose the correct answer
            choice = True
            continue
        else:
            print("please section one of the options")
            choice = False
     if answer == "a":
               print("You crossed the bridge! But you have no weapon to defend yourself from the tiny clowns attack")
               print("You find push a table across the entrance to block the tiny clown")
               print("but now you are trapped inside")
               print("You lose 25 health and are now stuck inside a cave, afraid and alone")
               subtract_Health(25)
               print("You see two cards on the floor")
               print("Current Health: ", health)
               check_Health()
     if answer == "b":
        print("You picked up the axe, the tiny clown follows you and chases you into a cave")
        print("You turn around and chop off the tiny clowns head...it rolls across the floor")
        print("You see a table above the clowns head, there are two cards on the table")
        print("")
    
     print("""


                          _____
                   _____ |J  ww|  
                  |8    ||   {)|
                  |  v v||(v)% | 
                  |v v v|| v % |       
                  |v v v||__%%[|               
                  |___ 8|       
                     __, _  _, _,_    _,    _,  _, __, __,  _   
                     |_) | / ` |_/   /_\   / ` /_\ |_) | \ ( )  
                     |   | \ , | \   | |   \ , | | | \ |_/  /   
                     ~   ~  ~  ~ ~   ~ ~    ~  ~ ~ ~ ~ ~    .     
                     """)
     input("Press any key to continue")
     print(" You have one more chance to survive")
     print("So my friend, pick a card to escape!")
     print("Choose A = Eight of Hearts")
     print("Choose B = The Joker")
     choice = False
     while choice == False:
        answer = input ("Choose a or b").lower()
        if answer == "a" or answer == "b": #if they choose the correct answer
            choice = True
            continue
        else:
             print("please section one of the options")
             choice = False
     if answer == "a":
          print("""    ⠀⠀⠀⣠⣤⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠤⣤⣀⠀⠀⠀⠀
                        ⠀⣬⣿⡗⢊⣁⡇⡐⣠⣼⣿⣟⣢⣴⣶⣼⡀⡰⢺⣿⣥⠀⠀⠀
                        ⢰ ⣸⣿⣿⣿⡀⠀⡧⠟⠛⠉⢻⣏⠙⢿⣿⣿⠀⢀⣾⣿⣿⡇⡄⠀
                       ⠄⣿⣿⣿⣿⣧⠎⠀⠀⠀⠀⠈⠛⢷⣦⣬⣽⣷⣼⣿⣿⣿⣿⠠⠁
                      ⡈⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⣈⡉⠉⣿⣿⣿⣿⣿⣿⢁⡀
                      ⠹⣽⣿⣿⣿⣿⡇⠀⠎⡀⢡⠀⠀⡘⢀⠘⠀⢸⣿⣿⣿⣿⣯⠞⠀
                       ⠨⠻⣿⡙⢿⠁⢰⣴⣷⣼⠀⠀⣇⣼⣤⡇⢸⡟⣽⣿⢟⠍⠀⠀
                        ⠀⠀⠉⢣⢸⡇⠘⢿⣶⠟⠀⠀⢻⣦⡿⠃⢸⢣⠛⠉⠀⠀⠀⠀
                         ⠀⠀⠀⠂⡇⢠⡀⠃⠠⣿⣿⡆⠘⢀⡀⠘⡌⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⢰⠘⣿⡶⠶⣾⣿⡶⣶⡿⢁⠋⠀⠀⠀⠀⠀⠀⠀
                       ⠀⠀⠀⠀⠀⠀⠈⢂⠘⣿⡳⠶⠖⣲⡿⢁⠎⣄⠀⠀⠀⠀⠀⠀⠀
                       ⠀⠀⠀⠀⢠⣶⡇⠈⢄⠈⠻⠿⠿⠋⢀⠎⠀⢿⣿⠷⠀⠀⠀⠀⠀
                       ⠀⠀⠀⣠⢡⠈⢁⠒⠈⠦⢀⣀⣀⠤⠦⠀⣒⡈⢠⠠⢱⠄⠀⠀⠀
                        ⠀⠀⠈⠀⣌⠔⢩⢀⠔⠐⢄⠀⠔⠁⠢⡀⠁⠈⠘⠆⠀⠁⠀⠀⠀
                          ⠀⠀⠀⠀⠀⠘⠁⠀⠀⠈⠎⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀""")

          print("Hahaha,to fool a fool.")
          print("The jokes on you. You chose eight hearts, not seeing the trick means the feasting can start!") 
          print("It is time for my meal, so where should I start...")
          print("Would you like to live deliciously?")
        
          subtract_Health(20)
          print("Current Health: ", health)
          check_Health()
          
          twins_picnic_event()

     if answer == "b":
            print("you chose correctly")
            twins_picnic_event()

#endregion

#region twins
def twins_picnic_event():
  print("You come out of the cave and two identical twins stand there,")
  print("join us join us, join us!!")
  print("Will you kill them, they are only children after all")
  print("Choose carefully, you have made it this far!!")
  print("A = KILL TWINS RUN TO WEST GATE, B = RUN TO THE EAST")
  choice = False 
  while choice == False:
        answer = input("Choose: ").upper()
        if answer == "A" or answer == "B": #if they choose the correct answer
            choice = True
            continue
        else:
             print("please section one of the options")
             choice = False
  if answer == "A":
        tree_exit_gateeast()
       
  elif answer == "B":
        tree_exit_Gates()
      


#endregion


#region START SCREEN
os.system('cls') #clears the screen

print("""                                    
    _,  _, __, _ _, _   _ _, _   ___ _,_ __,   __, __,  _,  _, ___ _ _, _  _,   __,  _, __, __,  _, ___
   / ` /_\ |_) | |\ |   | |\ |    |  |_| |_    |_  |_  /_\ (_   |  | |\ | / _   |_  / \ |_) |_  (_   | 
   \ , | | |_) | | \|   | | \|    |  | | |     |   |   | | , )  |  | | \| \ /   |   \ / | \ |   , )  | 
    ~  ~ ~ ~   ~ ~  ~   ~ ~  ~    ~  ~ ~ ~~~   ~   ~~~ ~ ~  ~   ~  ~ ~  ~  ~    ~    ~  ~ ~ ~~~  ~   ~")
      

                      _, ___  _, __, ___    _,  _, _, _ __,   _,_ __, __, __,
                     (_   |  /_\ |_)  |    / _ /_\ |\/| |_    |_| |_  |_) |_ 
                     , )  |  | | | \  |    \ / | | |  | |_    | | |__ | \ |__
                   ~~ ~   ~  ~ ~ ~ ~  ~     ~  ~ ~ ~  ~ ~~~   ~ ~ ~~~ ~ ~ ~~~~~~ """)
#====================================================================================================================================================================
print("Escape the Cabin in the Feasting Forest!! Play as Mike and Evie, two survivors of the zombie apocalypse")
print("The year is 2044 they have been on the run for weeks, and are starting to lose hope.Running out of food and water")
print("They flee the city and approach a cabin in the forest ")
print("The cabin is a place where the Gravewatchers hide and the zombies that are raging the cities won't dare go inside")
print("they say in the forest that they like to eat ears, they like to eat fingers, they make dipsticks with toes!")
print ("In order to win the game, and survive you need to investigate, and make it out ALIVE")
print("You can hear strange noises coming from the forest, and you can see strange lights flickering in the darkness....")

print("So player, what will you do?")
print("_____________________________________________________________________________________________________________________________________________________________")

#=====================================================================================================================================================================
while choice == False: 
  print("There are two characters, Mike and Evie")
  name = input("Choose your player now: ").lower()
  print("You have chosen", name)
  if name == "mike" or name == "evie":
      choice = True

print("______________________________________________________________________________________________________________________________________________________________")

#endregion

#region lightswitch
print("""


                                       
          ___                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
      .-"`   `"-.          ((((()                                                                                ((()))
    .'           '.    (((((()                                                                                        (((())
   /               \ ((())                                                                                                ((((())
  /  #              \)))                                                                                                        (((())
  | #                ;     _, _  _ _ ___  _, _,_    _, _, _   _,  _  _, _,_ ___   , _ __,  _,    _, __,   _, _  _,  _               (((()
  ;                  ;    (_  |  | |  |  / ` |_|   / \ |\ |   |   | / _ |_|  |    \ | |_  (_    / \ |_)   |\ | / \ ( )               (((())
  ;                  ;    , ) |/\| |  |  \ , | |   \ / | \|   | , | \ / | |  |     \| |   , )   \ / | \   | \| \ /  /               (((())))           
  ;     .-~~~-.      ;    ~  ~  ~ ~  ~   ~  ~ ~    ~  ~  ~   ~~~ ~  ~  ~ ~  ~      ) ~~~  ~     ~  ~ ~   ~  ~  ~   .               ))(()  
  |                 |                                                                                                           (((((
   ;     )   (     ; ((()))                                                                                                 ((((()
    \   (     )   /   (((())))                                                                                           ((((()
     \   \   /   /        (((((())                                                                                    ((((()
      \   ) (   /             (((())))                                                                             ((((()
       |  | |  |                 OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
       |__|_|__|
     SG{=======}
       }======={
       {=======}JC
       }======={
     SW{=======}
        `""u""`  """)
print("________________________________________________________________________________________________________________________________________________________________")
print(" You  enter the cabin, it is dark and there is a long hallway ahead of you, you hear noises coming from the distance")
print("________________________________________________________________________________________________________________________________________________________________")
print(" There is a light switch to your left, will you swtich it on YES/NO")
choice = False
while choice == False:
    answer = input("Choose YES/NO: ").lower()
    if answer == "yes" or answer == "no":
        choice = True
        continue
    else:
        print("please select yes or no")
        choice = False
    

print("________________________________________________________________________________________________________________________________________________________________")
#========================================================================================================================================================================
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if answer == "yes":
  print("you choose to switch on the light!")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("Your eyes adjust to the brightness, you scan the cabin....all of a sudden BANG")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("The lights black out and footsteps begin approaching you, you run to the end of the hallway, there are two doors...One on the left and one straight ahead.")
  print("""

        """)
  choice = False
  while choice == False:
    answer = input("Choose Left or Straight: ").lower()
    if answer == "left" or answer == "straight":
        choice = True
        continue
    else:
        print("please select from the options")
        choice = False
    
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  #region left or straight
  if answer == "left":
        print("""



                                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣶⣦⣌⣆⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                  ⢀⣴⠖⠀⠀⠀⢀⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⢀⠀
                                                  ⣼⣿⣦⣀⣠⣴⣿⣿⣿⣿⢿⡿⠋⠻⣿⣿⣿⣿⣿⡟⢿⡿⣿⣶⣄⡀⠀⠀⢸⣇
                                                  ⣿⣿⣿⣿⣿⣿⡿⠋⠈⠀⠀⠀⠀⠀⣿⣿⣿⣿⠟⠀⠈⠀⠈⢿⣿⣿⣷⣾⣿⣿
                                                  ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⣠⣴⠿⠋⠙⠇⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣯
                                                  ⠸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿
                                                  ⠀⣼⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⠃
                                                  ⠀⠘⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠀
                                                  ⠀⠀⠀⠙⣻⣿⣯⢃⠀⠤⠀⢀⡇⠀⠀⠀⠀⠀⢁⠀⠤⠀⢰⣻⣿⣿⠿⠋⠀⠀
                                                  ⠀⠀⠀⠀⠈⠛⠿⡎⡀⠀⢰⣈⣣⣀⢀⢰⠀⣀⠞⣢⠀⠀⣮⣿⠯⠁⠀⠀⠀⠀
                                                  ⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⢀⡽⠉⠀⠀⠀⠀⠈⠉⢻⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀
                                                  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢏⠀⠀⠶⣶⣴⡶⠆⠀⢀⡷⢸⠀⠀⠀⠀⠀⠀⠀⠀
                                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠣⡀⠀⠁⢲⣤⣬⣩⣤⡴⠂⢁⡠⠜⠀⠀⠀⠀⠀⠀⠀⠀
                                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⡀⠹⣳⣶⡿⢁⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⣀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

   
              """)
        
        print("You enter the doorway {}, a tiny killer clown starts kicking you in the shins ".format(name))
        print("he has blood filLed eyes and IT is laughing hysterically....You look at the tiny clown and with one kick.") 
        print("Kick clown in face A), or kick clown in pompoms B)")
         #this variable stores the players answer
        choice = False
        while choice == False:
            answer =  answer = input ("Choose A or B: ").upper() 
            if answer == "A" or answer == "B":
                choice = True
                continue
            else:
                print("please select from the options")
                choice = False

        if answer == "A":
            add_Health(15) #adds health to the player
            print(health) #check_health shows health so add to print
            check_Health()
            print("You kicked the clown in the face, you legend, he flew out the window and you managed to exit the cabin, nice move!")
            print("You are now in the Forest...survive this and you might just make it out of here!")
            clown_Cave_event()
        elif answer == "B":
            #Sophia please add option B pom pom text
            subtract_Health(15)
            print(health)
            check_Health()
            print("You Kicked the clown in the pompoms")
            print("What are you  dummy, what did you expect to happen")
            print("The clown stuffed his pompoms in your mouth then he strangled you to death")
            pickup_Key_Event()
        
  elif answer == "straight":
        print("""
              
        ⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⡆⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⣾⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣷⡦⠀⠀⠀⠀⢰⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠃⣠⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣆⠀⠀⠀⣾⣿⣿⣿⣷⠄⠀⠰⠤⣀⠀⠀⣴⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠃⢺⣿⣿⣿⣿⡄⠀⠀⣿⣿⢿⣿⣿⣦⣦⣦⣶⣼⣭⣼⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⡆⠂⣿⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢙⣿⣿⣿⣿⣷⠸⣿⣿⣿⣿⣿⣿⠟⠻⣿⣿⣿⣿⡿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢿⣿⣿⣿⣿⡄⣿⣿⣿⣿⣿⣿⡀⢀⣿⣿⣿⣿⠀⢸⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡀⣠⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣻⣿⣿⣿⣿⣿⡟⠋⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⠿⢿⡿⠛⠋⠁⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣅⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⡟⠃⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣿⣿⣿⣿⣿⣤⡀⠀⠀⠀
⠀⠜⢠⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣦⠄⣠⠀
⠠⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠛⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⢳⣾⣿⣿⣿⣿⣿⣿⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⢨⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡿⡿⠿⠛⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠏⠉⠻⠿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀



              """)
        print("A cat runs past your feet, the light flickering on and off, you are in a kitchen.")
        print("A key drenched in blood is on the floor, there is a trail of blood where the cat passed you by, as you follow the trail you spot a key......  ")
        print("A: pick up key | B: run upstairs")
        print("current Health:", health)
        choice = False
        while choice == False:
            answer = input("choose A or B: ").upper()
            if answer == "A" or answer == "B":
                choice = True
                continue
            else:
                print("please select from the options")
                choice = False
        if answer == "A":
            pickup_Key_Event()
        elif answer == "B":
            runUpstairsEvent()
       
    
    
    #endregion

elif answer == "no":
    print("""
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|
                                ScW


""")
    print("A cat runs past your feet, the light flickering on and off, you are in a kitchen.")
    print("A key drenched in blood is on the floor, there is a trail of blood where the cat passed you by!")
    print("As you follow the trail you spot a key......  ")
    print("A: pick up key | B: run upstairs")
    print("current Health:", health)
    choice = False
    while choice == False:
         answer = input("choose A or B: ").upper()
         if answer == "A" or answer == "B":
            choice = True
            continue
         else:
            print("please select from the options")
            choice = False

    if answer == "A":
        pickup_Key_Event()
    elif answer == "B":
       runUpstairsEvent()
#endregion

#region family picknic
def family_picnic():
    print("""
             __, _,  __,  _,  _, __,    __,  _, _ _, _   _,_  _,
             |_) |   |_  /_\ (_  |_    , |  / \ | |\ |   | | (_ 
             |   | , |   | | , ) |     ( |  \ / | | \|   | | , )
             ~   ~~~ ~~~ ~ ~  ~  ~~~    ~~   ~  ~ ~  ~   `~'  ~ 
""")
    print("After escaping the clown you come across a family picnic in the forst")
    print("They are all wearing matching outfits, they have white eyes")
    print("They grin at you in unision and chant 'Please Join us")
    print("A: Join Family |B: Run into cave")
    while choice == False:
        answer = input("choose A or B: ").upper()
        if answer == "A" or answer == "B":
             choice = True
             continue
        else:
             print("please select from the options")
             choice = False

    if answer == "A":
        tree_exit_gateeast()
    
    elif answer == "B":
        region_riverspiders()
#endregion

#region riverspiders
    def region_riverspiders():
         print("You run across the brige, just as you reach its end, a Giant spider blocks your exit")
    print("All of a sudden thousands of spiders begin to emerge, a giant web glistens in the dark shadows")
    print("The Giant spider climbs the web. Theres only one way to the other side")
    print("Choose a= Break through web to cross or b = Jump into the bloody river")
    if answer == input("a"):
     tree_exit_Gates()
    elif answer == "b":
     tree_exit_gateeast()

#endregion



