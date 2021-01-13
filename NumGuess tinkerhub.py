import random
import time
answer=random.randint(1,100)
difficulty=10
profiles={}
currentuser=""

def profilescreen():
    global profiles
    global currentuser
    proflist=list(profiles.keys())
    print(f"{'*'*75}")
    print("\t\t\t\tPROFILE SETTINGS")
    print(f"{'*'*75}")
    print("\n\nSelect username:\n\n")
    for i in range(0,len(proflist)):
        print(proflist[i])
    print("+ Enter \'0\' if you are a new user")
    selection=input()
    if selection=='0':
        currentuser=input("Please Enter your desired username : ")
        profiles[currentuser]=-1
        mainmenu()
    elif selection in proflist:
        currentuser=selection
        mainmenu()
    else:
        print("Please enter a valid name or \'0\'to create a new username")
        time.sleep(3)
        profilescreen()


def mainmenu():
    print(f"{'*'*75}")
    print(f"\n\t\tWELCOME TO THE NUMBER GUESSING GAME, {currentuser} !\n")
    print(f"{'*'*75}")
    print("\nMAIN MENU\n\n1. New Game\n2. Change difficulty\n3. Personal High Score\n4. Change User\n5. How to play\n6. Quit Game")
    selection=int(input("Enter a choice : "))

    if selection==1:
        game()
    elif selection==2:
        print("Main menu difficulty=",difficulty)
        changedifficulty()
    elif selection==3:
        highscore()
    elif selection==4:
        profilescreen()
    elif selection==5:
        howtoplay()    
    elif selection==6:
        quitgame()
    else:
        print("Sorry, please enter a valid choice")
        mainmenu()

def game():

    score=100
    guess=-1
    global highscore
    print(f"{'*'*75}")
    print("\n\t\t\tGET READY TO PLAY")
    print(f"{'*'*75}")
    time.sleep(3)
    while guess!=answer:
        guess=int(input("Enter your guess : "))

        if guess<answer:
            print("Target is higher\n")
            score-=difficulty
            if score<0:
                print("GAME OVER!")
                time.sleep(3)
                mainmenu()

        elif guess>answer:
            print("Target is lower\n")
            score-=difficulty
            if score<0:
                print("GAME OVER!")
                time.sleep(3)
                mainmenu()

        else:
            print("\nRIGHT ANSWER!!!")
            print(f"Your score is {score}\n")
            if score>profiles[currentuser]:
                profiles[currentuser]=score
                print("NEW HIGH SCORE : ",profiles[currentuser])
            time.sleep(3)
            input("\n\n***Press enter to continue***")
            mainmenu()


def howtoplay():
    print("\n\n*****HOW TO PLAY*****")
    print(f"Finish the game with maximum points\nYou have 100 points to start with.\nGuess the target in {int(100/difficulty)} chances to win.\nEvery wrong guess reduces {difficulty} points.\n*****ALL THE BEST!*****")
    time.sleep(3)
    input("\n\n***Press enter to continue***")
    mainmenu()

def changedifficulty():
    print(f"{'*'*75}")
    print("\t\t\tDIFFICULTY SETTINGS MENU")
    print(f"{'*'*75}")
    print("\n\nChoose your difficulty :\n1. Easy\n2. Hard")
    global difficulty
    newdiff=int(input("Enter your choice : "))
    if (newdiff==1 or newdiff==2):
        difficulty=newdiff*10
        print("function diff=",difficulty)
        mainmenu()
    else:
        print("Sorry, you did not enter a valid choice.")
        changedifficulty()
        
def highscore():
    print(f"{'*'*75}")
    print("\t\t\tHIGH SCORE")
    print(f"{'*'*75}")
    print("\n\nYour personal high score is : ", profiles[currentuser])
    input("\n\n***Press enter to continue***")
    mainmenu()

    
def quitgame():
    print(F"{'*'*75}\n\nTHANK YOU FOR PLAYING\n\n\n\t\t\t\t\t-NIKHIL G\n\n{'*'*75}")    
    time.sleep(5)
    quit()

profilescreen()
