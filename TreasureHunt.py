print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome To Treasure Hunt 👋.\n")
print("Your Mission Is To Find The Treasure🕵‍♂🔎\n")
direction =input("Which Direction Do You Want To Choose 👈👉? ('left'or'right')")
if(direction=="right"):
    print("ohhh, you Fell Into a Hole 🤦‍♂️, Game Over 😓")
elif(direction=="left"):
    print("You Are On The Right Path, Keep Going 🏃‍♂️")
    decision  = input("Do You Want To Swim 🏊‍♂️ Or Wait ⌛ ?")
    if(decision=="swim"):
        print("ohhh, you drowned in the sea 🤦‍♂️ , Game Over 😓")
    elif(decision=="wait"):
       print("You Choose The Correct Choice ✅ , Keep Going 🏃‍♂️")
       door=input("Which Door Do You Want To Choose 🚪? ('red'or'blue'or'yellow')")
       if(door=="red"):
           print("ohhh, You Entered The Red Door And Found A Fire-Breathing Dragon! 🐉, Game Over😓")
       elif(door=="blue"):
           print("ohhh, You Entered The Blue Door And Fell Into A Pit Of Snakes! 🐍, Game Over😓")
       elif(door=="yellow"):
           print("Congratulations! You Entered The Yellow Door And Found A Room Full Of Treasure! 💰")
