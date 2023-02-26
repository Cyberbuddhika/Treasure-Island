print('''
  _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Game will ask you to take a decision")
print("You just have enter the correct number of the action you choose and hit 'enter'")
scene2=0
scene3=0
scene4=0
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You went to a island for holiday and walking down the beach. Suddenly you see a bottle washed up on the shore. What would you do?")
answer1=input("1.Walk away\n2.Throw it back to the see \n3.See inside the bottle. \nType the correct number for your answer: ")
if answer1 =="3":
  print()
  print("Great. You found a map inside. Exciting!")
  print()
  print("Now you are following the map. There should be cocunut tree near a big rock, which look like a huge rhino. Let's go and find it.")
  print('''
                      ,-.             __
                    ,'   `---.___.---'  `.
                  ,'   ,-                 `-._
                ,'    /                       \
             ,\/     /                        \\
         )`._)>)     |                         \\
         `>,'    _   \                  /       |\
           )      \   |   |            |        |\\
  .   ,   /        \  |    `.          |        | ))
  \`. \`-'          )-|      `.        |        /((
   \ `-`  .a`     _/ ;\ _     )`-.___.--\      /  `'
    `._         ,'    \`j`.__/        \  `.    \
      / ,    ,'       _)\   /`        _) ( \   /
      \__   /        /nn_) (         /nn__\_) (
        `--'           /nn__\             /nn__\
                                      hjw
''')
  answer2=input("Which direction do you want to go?\n1.North\n2.South\n3.West\n4.East \nType the correct number for your answer: ")
  if answer2 == "1":
      print()
      print("Great! you found the rock.")
      print("It's time to dig up the Treasure.")
      print()
      print("A few moments later....")
      print()
      print("You found it. Now is the tricky part. treasure box has 03 buttons. Red, Blue and Green. If you press wrong one, you are dead. Please be careful. Choose the color")
      answer3=input("Which you do you choose?\n1.Red\n2.Green\n3.Blue\nType the correct number for your answer: ")
      if answer3 == '1':
        print()
        print("Congratulations! You Won. Enjoy your treasure.")
        print('''
           __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%
  ''')
      else:
          print("Oh! You are lost. Game Over.")
  elif answer2 == "2":
    print("You were bit by a Snake. You are dead. Game over.")
    print('''
      --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.      cjr
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`

  ''')
  elif answer2 == "3":
    print("You were killed by a Lion. You are dead. Game over.")
    print('''
                                                  ,w.
                                              ,YWMMw  ,M  ,
                         _.---.._   __..---._.'MMMMMw,wMWmW,
                    _.-""        """           YP"WMMMMMMMMMb,
                 .-' __.'                   .'     MMMMW^WMMMM;
     _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
  ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
 ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
 WMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
 "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
            /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
           /  .'             /  (       .'  /     Ww._     `.  `"
          /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
 fsc     (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
          `"""                    `"""   `"'                  `---" 

  ''')
  elif answer2 == "3":
    print("You were fallen off from a cliff. You are dead. Game over.")
  else:
    print("Oh! You are lost. Game Over.")


  
else:
  print("Oh! You are lost. Game Over.")



