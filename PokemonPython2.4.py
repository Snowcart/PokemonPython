import time
print("""

               / _ \\/___\\/\\ /\\___  /\\/\\   /___\/\\ \\ \\
              / /_)//  // //_/ _ \/    \ //  //  \/ /
             / ___/ \_// __ \  __/ /\/\ | \_// /\  / 
             \/   \___/\\/  \\/\___\\/    \\|___/\\_\\ \\/
                  _____                     
                 /  ___|                    
                 \ `--. _ __   _____      __
                  `--. \ '_ \ / _ \ \ /\ / /
                  \__/ / | | | (_) \ V  V / 
                 \____/|_| |_|\___/ \_/\_/  
                           
                 By: Carter "Snowcart" Snowden
             Version 2.4 Realsese Version
                       Do Not Distribute
            Text and Mewtwo ascii art done by a converter
            Props to Mr. Cheng, for teaching me how to do this

            """)
                                     

print("""
      .
      |\\
      | \\.,,,___________
     /            ___!!/
     | (%)    (%)  |
    ()    .     () |
     \   ___      /
     /            \\
  \\"/       \\''\\  |
    \\          <_/
     \\         <_'|
      .,..,,/\\"/, /\\
      \\  |  \\___/  \\\\
       ""        __//
         _____   ||..
        /  /  \\\\ ||
       /  /    \\, |
      |__|      \\ 
Welcome to the Pokemon World, Your Journey begins today, your starter Pokemon is this Pickachu. Time to catch your first pokemon.""")


game_over = False
level_one = False
level_two = False
level_three = False
exit_game_1 = False
exit_game_2=False
exit_game_3=False
player_won=False
import random
import time
word_list_1 = ["dog", "pokemon", "geodude", "lava", "lamp", "candle", "sing", "music"]
word_list_2 = ["taco", "friends", "ferret", "shirt", "pencil", "mewtwo", "pants"]
word_list_3 = ["gears", "belt", "super", "batman", "hellboy", "computer", "motherboard"]

user_name = input("Trainer, Enter your name...")
print(" Welcome to Pokemon World " + ( user_name))
print ("Time to Enter the Pokemon World")
time.sleep(3)

level_one = True
while (level_one == True):            
    while (exit_game_1 == False):
        secret_word = word_list_1[ random.randint( 0, len(word_list_1) - 1 ) ]
        guesses_remaining = 6
        previously_guessed_letters = []
        game_over = False
        print("""
  ______            
 / _\\_\\_\\
 \_;  ,()                     ______
  |  |        _______        /\\_\\_\\_\\
  \  \       ,       ,       ()    _/
   \  \     /         \       \   _|
    \  \__,/.  .\  /. /\       / /
     \_=____\  ______/\ \_____/ /
             \/_____,| \___==__/
       Wild Geodude Jump Out!   """)
        


        while (game_over == False):


            for letter in secret_word: 
                if (letter in previously_guessed_letters):
                    print(letter, end="")
                else:
                    print(" _ ", end="")
            print("")

            guessed_letter = input("Guess a letter (in lower case): ")



            if (guessed_letter in secret_word):
                all_letters_guessed = True
                for letter in secret_word:
                    if (letter not in previously_guessed_letters):
                         all_letters_guessed = False


                if (all_letters_guessed == True):
                    game_over = True
                    player_won = True

                print("""
                     #  #
  ______            ######
 / _\\_\\_\\            #  #
 \_;  ,()                     ______
  |  |        _______        /\\_\\_\\_\\
  \  \       ,       ,       ()    _/
   \  \     /         \       \   _|
    \  \__,/.  .\  /. /\       / /
     \_=____\  ______/\ \_____/ /
             \/_____,| \___==__/
                                """)
                print ("HP" + str(guesses_remaining))
               
            elif (guessed_letter in previously_guessed_letters):
                guesses_remaining =  guesses_remaining - 1
                print("""
                     #  #
  ______            ######
 / _\\_\\_\\            #  #
 \_;  ,()                     ______
  |  |        _______        /\\_\\_\\_\\
  \  \       ,       ,       ()    _/
   \  \     /         \       \   _|
    \  \__,/.  .\  /. /\       / /
     \_=____\  ______/\ \_____/ /
             \/_____,| \___==__/
                                """)
                print ("HP" + str(guesses_remaining))
            else:
                guesses_remaining =  guesses_remaining - 1
                print("""
                     #  #
  ______            ######
 / _\\_\\_\\            #  #
 \_;  ,()                     ______
  |  |        _______        /\\_\\_\\_\\
  \  \       ,       ,       ()    _/
   \  \     /         \       \   _|
    \  \__,/.  .\  /. /\       / /
     \_=____\  ______/\ \_____/ /
             \/_____,| \___==__/
                                """)
                print ("HP" + str(guesses_remaining))

            if (guesses_remaining == 0):
                game_over = True
                player_won = False
    
            if (guessed_letter not in previously_guessed_letters):
                previously_guessed_letters.append(guessed_letter)

            if (guessed_letter in secret_word):
                all_letters_guessed = True
            for letter in secret_word:
                if (letter not in previously_guessed_letters):

                    all_letters_guessed = False

          
            if (all_letters_guessed == True):
                game_over = True
                player_won = True
                         

    

        if (player_won == True):
            print("You won!")
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
           Geodude Captured!!!!!
           """)
          
            level_one=False
            level_two=True
            exit_game_1=True
            exit_game_2=False
        else:
            print("Try again next time.")
            level_one=False
            level_two=False
            exit_game_1=True
            if exit_game_1==True:
                play_again1=str(input("Capture Again?"))
            if play_again1==("Yes"):
                exit_game_1=False
                level_one=True
            else:
                print("Good luck on your journy trainer")

while (level_two == True):            
    while (exit_game_2 == False):
        secret_word = word_list_2[ random.randint( 0, len(word_list_2) - 1 ) ]
        guesses_remaining = 6
        previously_guessed_letters = []
        game_over = False

        name1=str(input("""Congragulations, Geodude caught!
give a nickname to geodude??"""))

        if name1==str("yes"):
            Geodude=str(input("Give Geodude a nickname!"))
        else:
            Geodude=(str("Geodude"))

        choose1=str(input("""What Pokemon would you like to use for the next battle (Pickachu or Geodude)"""))
        print("""


                       ///////
                      ///////
                     /////// 
                     ----- 
                   / O O   \\
                   ! _____ !
                   \\ \/ \/ /
                    -------
                   Wild Gastly Jump Out """)        

        if choose1==str("Pickachu"):
            print("Go Pickachu!!")
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
            """)
            time.sleep(2)

            print("""

      .
      |\\
      | \\.,,,___________
     /            ___!!/
     | (%)    (%)  |
    ()    .     () |
     \   ___      /
     /            \\
  \\"/       \\''\\  |
    \\          <_/
     \\         <_'|
      .,..,,/\\"/, /\\
      \\  |  \\___/  \\\\
       ""        __//
         _____   ||..
        /  /  \\\\ ||
       /  /    \\, |
      |__|      \\
      """)

        elif choose1==("Mewtwo"):
            print("""
                  hhy+.              `                       
                 oNNNh             yNo                      
                 `mNNm.-+syhys/.`:hNNN/                     
                  sNNNdhmNNNNNNNmmmmmd.                     
                  oNNNNmyhmNNNNNNNmmy`                      
                  yNNNNNNhmNNNNNNNNd`                       
                 -NNNNNNNNNNNNNNNNNh                        
                 yNNNNmNNNmNNNNNNNNNo                       
                 dNNNmNsdNmdNNNNNNNd-                       
                 `hdmhNs/yhyNNNNmy:                         
                 `mNyosddsdmNNNNs- -smNhsooo+-              
                  -mhmdsdNNNNNNy` `NNNm     .+ys-           
                  `-hNmdo/hhmms`  `mNNN/       -yd/         
                /mNNmNNmNNNddh:    :NNNNo`       /Nm/       
                oNNNdNhNNNdshy:     :mNNNh.       +NNd-     
               `yNNhNmyNNmodNN-      -mNNNm/       dNmy:`   
              `yd+++yhyysys+oNh`      :NNNNN+      +hyo+/`  
             .dN/  sNNNNNNmo .dd-      yNNNNm:     :sso+//` 
           `+my. `:mNNNNNNmh//-yNo`    yNNNNmy     -sssso/: 
        `/ymy.  +mdddddhdNNdNNNhmNm.  :NNNNNmd`     sdddyo/.
       /mNNy`  ymdhNNNNdyydNNNNhmNmo:yNNNNNNmd`     .dNNNh+-
      /NNNs`  oNhyNNNNmhhshNNNdmNNyNNyNNNNNNdo       `+dNNo-
   -+yNNd/   .NdhhNNNNdyysoyNyNNNymNNNyNNNNmd.          `-. 
  :mdm+o/    /NNshNNNNdyyyo+yyNNmsNNNNhmNmdh:               
`ommdhyh-    .NNm+hdddhyshhssNNNhdNNNNNshyy/                
:dmh+omyNh    -hNhoysss+sdmNNNNNhNNNNNm/o+-                 
  //  `...      /mhoo////oyNNhdNddNNNNh:-`                  
                `dmm/+///omy/:sNN+dNNmy`                    
                :NNo   `..-----::.`ommy                     
               /NNN+                +mm:                    
             :hNNdmms-               yNm:                   
          `/dNNNhdNNNo               :NNN+`                 
        -omNNNNy/-//.                .NNNNd-                
   `/shmNNNNNh-                      oNNNNNm:               
   dNmhmNNNNo`                       /NNNNNNm-              
   `.`yNNmy-                          ommdhNNm:             
       ``                              dNNmsNNNs            
                                       +hdy-:+o+                               SEND OUT!! MEWTWO!!
                              (MEWTWO'S MOVES, RECOVER)
                              """)
        else:
            print("Go " + str(Geodude))
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
            """)
            time.sleep(2)


            print("""

                     #  #
  ______            ######
 / _\\_\\_\\            #  #
 \_;  ,()                     ______
  |  |        _______        /\\_\\_\\_\\
  \  \       ,       ,       ()    _/
   \  \     /         \       \   _|
    \  \__,/.  .\  /. /\       / /
     \_=____\  ______/\ \_____/ /
             \/_____,| \___==__/
                                """)
            time.sleep(2)

                
        while (game_over == False):

                              

            for letter in secret_word:
                if (letter in previously_guessed_letters):
                    print(letter, end="")
                else:
                    print(" _ ", end="")
            print("")

            guessed_letter = input("Guess a letter (in lower case): ")
            if choose1==("Mewtwo"):
                if guessed_letter==("Recover"):
                    guesses_remaining=guesses_remaining+2



            if (guessed_letter in secret_word):
                all_letters_guessed = True
                for letter in secret_word:
                    if (letter not in previously_guessed_letters):
                         all_letters_guessed = False

               

                if (all_letters_guessed == True):
                    game_over = True
                    player_won = True
                print("""
                     #  #
                    ######
                     #  #

                       ///////
                      ///////
                     /////// 
                     ----- 
                   / O O   \\
                   ! _____ !
                   \\ \/ \/ /
                    -------

                                """)
                print ("HP" + str(guesses_remaining))
               
            elif (guessed_letter in previously_guessed_letters):
                guesses_remaining =  guesses_remaining - 1
                print("""
                     #  #
                    ######
                     #  #

                       ///////
                      ///////
                     /////// 
                     ----- 
                   / O O   \\
                   ! _____ !
                   \\ \/ \/ /
                    -------

                                """)
                print ("HP" + str(guesses_remaining))
            else:
                guesses_remaining =  guesses_remaining - 1
                print("""
                     #  #
                    ######
                     #  #

                       ///////
                      ///////
                     /////// 
                     ----- 
                   / O O   \\
                   ! _____ !
                   \\ \/ \/ /
                    -------

                                """)
                print ("HP" + str(guesses_remaining))

            if (guesses_remaining == 0):
                game_over = True
                player_won = False
                print("""
      ∫∫˚˙˚
    Ω˚¬µ¨ø
   ˚∂∂˚¬˚¬¬
   ˚¬∂¬…∂∂¬…
    """)
            if (guessed_letter not in previously_guessed_letters):
                previously_guessed_letters.append(guessed_letter)
            if (guessed_letter in secret_word):
                all_letters_guessed = True
            for letter in secret_word:
                if (letter not in previously_guessed_letters):
                    all_letters_guessed = False

            if (all_letters_guessed == True):
                game_over = True
                player_won = True


            if (guessed_letter in secret_word):
                all_letters_guessed = True
            for letter in secret_word:
                if (letter not in previously_guessed_letters):
                    all_letters_guessed = False

            if (all_letters_guessed == True):
                    game_over = True
                    player_won = True

        if (player_won == True):
            print("Conrgadulations You captured Gastly")
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
           Gastly Captured!!!!!
           """)
            level_two=False
            level_one=False
            level_three=True
            exit_game_1=True 
            exit_game_2=True
            exit_game_3=False
            
        else:
            print("Try again next time.")
            level_two=False
            level_three=False
            level_one=False
            exit_game_2=True
            if exit_game_2==True:
                play_again1=str(input("Capture Again?"))
                if play_again1==("yes"):
                    exit_game_3=True
                    exit_game_2=True
                    exit_game_1=False
                    level_one=True
                    level_two=False
                    level_three=False
                else:
                    print("Good luck on your journy trainer")



while (level_three == True):            
    while (exit_game_3 == False):
        secret_word = word_list_3[ random.randint( 0, len(word_list_3) - 1 ) ]
        guesses_remaining = 6
        previously_guessed_letters = []
        game_over = False

        name2=str(input("""Congragulations, Gastly caught!
give a nickname to Gastly??"""))

        if name2==str("yes"):
            Gastly=str(input("Give Gastly a nickname!"))
        else:
            Gastly=(str("Gastly"))

        choose2=str(input("""What Pokemon would you like to use for the next battle (Pickachu or Geodude or Gastly)"""))



        if choose2==str("Gastly"):
            print("Go! "+ (Gastly))
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
            """)
            time.sleep(2)


            print("""


                       ///////
                      ///////
                     /////// 
                     ----- 
                   / O O   \\
                   ! _____ !
                   \\ \/ \/ /
                    -------
                    """)        

        elif choose2==str("Pickachu"):
            print("Go Pickachu!!")
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
            """)
            time.sleep(2)

            print("""

      .
      |\\
      | \\.,,,___________
     /            ___!!/
     | (%)    (%)  |
    ()    .     () |
     \   ___      /
     /            \\
  \\"/       \\''\\  |
    \\          <_/
     \\         <_'|
      .,..,,/\\"/, /\\
      \\  |  \\___/  \\\\
       ""        __//
         _____   ||..
        /  /  \\\\ ||
       /  /    \\, |
      |__|      \\
      """)

        elif choose2==("Mewtwo"):
            print("""
                                                                   
                 oNNNh             yNo                      
                 `mNNm.-+syhys/.`:hNNN/                     
                  sNNNdhmNNNNNNNmmmmmd.                     
                  oNNNNmyhmNNNNNNNmmy`                      
                  yNNNNNNhmNNNNNNNNd`                       
                 -NNNNNNNNNNNNNNNNNh                        
                 yNNNNmNNNmNNNNNNNNNo                       
                 dNNNmNsdNmdNNNNNNNd-                       
                 `hdmhNs/yhyNNNNmy:                         
                 `mNyosddsdmNNNNs- -smNhsooo+-              
                  -mhmdsdNNNNNNy` `NNNm     .+ys-           
                  `-hNmdo/hhmms`  `mNNN/       -yd/         
                /mNNmNNmNNNddh:    :NNNNo`       /Nm/       
                oNNNdNhNNNdshy:     :mNNNh.       +NNd-     
               `yNNhNmyNNmodNN-      -mNNNm/       dNmy:`   
              `yd+++yhyysys+oNh`      :NNNNN+      +hyo+/`  
             .dN/  sNNNNNNmo .dd-      yNNNNm:     :sso+//` 
           `+my. `:mNNNNNNmh//-yNo`    yNNNNmy     -sssso/: 
        `/ymy.  +mdddddhdNNdNNNhmNm.  :NNNNNmd`     sdddyo/.
       /mNNy`  ymdhNNNNdyydNNNNhmNmo:yNNNNNNmd`     .dNNNh+-
      /NNNs`  oNhyNNNNmhhshNNNdmNNyNNyNNNNNNdo       `+dNNo-
   -+yNNd/   .NdhhNNNNdyysoyNyNNNymNNNyNNNNmd.          `-. 
  :mdm+o/    /NNshNNNNdyyyo+yyNNmsNNNNhmNmdh:               
`ommdhyh-    .NNm+hdddhyshhssNNNhdNNNNNshyy/                
:dmh+omyNh    -hNhoysss+sdmNNNNNhNNNNNm/o+-                 
  //  `...      /mhoo////oyNNhdNddNNNNh:-`                  
                `dmm/+///omy/:sNN+dNNmy`                    
                :NNo   `..-----::.`ommy                     
               /NNN+                +mm:                    
             :hNNdmms-               yNm:                   
          `/dNNNhdNNNo               :NNN+`                 
        -omNNNNy/-//.                .NNNNd-                
   `/shmNNNNNh-                      oNNNNNm:               
   dNmhmNNNNo`                       /NNNNNNm-              
   `.`yNNmy-                          ommdhNNm:             
       ``                              dNNmsNNNs            
                                       +hdy-:+o+ 
                              SEND OUT!! MEWTWO!!
                              (MEWTWO'S MOVES, RECOVER)
                              """)





        else:
            print("Go " + str(Geodude))
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
            """)
            time.sleep(2)


            print("""

                     #  #
  ______            ######
 / _\\_\\_\\            #  #
 \_;  ,()                     ______
  |  |        _______        /\\_\\_\\_\\
  \  \       ,       ,       ()    _/
   \  \     /         \       \   _|
    \  \__,/.  .\  /. /\       / /
     \_=____\  ______/\ \_____/ /
             \/_____,| \___==__/
                                """)
            time.sleep(2)


        while (game_over == False):
            print("""

                 ______
	        /      \\
	    ___I_ 0 0  I______
           /     \ ()  /      \\
          I  0 0 I     I 0 0  I
          I   () I     I ()   I
        ##I      I_____I      I##
      ####I      I#####I      I####
     ###############################
     """)
            print("HP " + str(guesses_remaining) )

                    

            for letter in secret_word:
                if (letter in previously_guessed_letters):
                    print(letter, end="")
                else:
                    print(" _ ", end="")
            print("")

            guessed_letter = input("Guess a letter (in lower case): ")
            if choose1==("Mewtwo"):
                if guessed_letter==("Recover"):
                    guesses_remaining=guesses_remaining+2



            if (guessed_letter in secret_word):
                all_letters_guessed = True
                for letter in secret_word:
                    if (letter not in previously_guessed_letters):
                         all_letters_guessed = False

                if (all_letters_guessed == True):
                    game_over = True
                    player_won = True
               
            elif (guessed_letter in previously_guessed_letters):
                guesses_remaining =  guesses_remaining - 1
                print("""

                 ______
	        /      \\
	    ___I_ 0 0  I______
           /     \ ()  /      \\
          I  0 0 I     I 0 0  I
          I   () I     I ()   I
        ##I      I_____I      I##
      ####I      I#####I      I####
     ###############################
     """)
                print("HP " + str(guesses_remaining))
            
            else:
                guesses_remaining =  guesses_remaining - 1
                print("""

                 ______
	        /      \\
	    ___I_ 0 0  I______
           /     \ ()  /      \\
          I  0 0 I     I 0 0  I
          I   () I     I ()   I
        ##I      I_____I      I##
      ####I      I#####I      I####
     ###############################
     """)
            print("HP " + str(guesses_remaining))

            if (guesses_remaining == 0):
                game_over = True
                player_won = False
    
            if (guessed_letter not in previously_guessed_letters):
                previously_guessed_letters.append(guessed_letter)
            if (guessed_letter in secret_word):
                all_letters_guessed = True
            for letter in secret_word:
                if (letter not in previously_guessed_letters):
                    all_letters_guessed = False

            if (all_letters_guessed == True):
                game_over = True
                player_won = True


            if (guessed_letter in secret_word):
                all_letters_guessed = True
            for letter in secret_word:
                if (letter not in previously_guessed_letters):
                    all_letters_guessed = False


        if (player_won == True):
            print("Conrgadulations You captured Dugtrio")
            print("""

            0000
          00000000
         0----o---0
          00000000
            0000
           Dugtrio Captured!!!!!
           """)
            print("Congradualtions, You are a Pokemon Master!")
            exit_game_3=True
            play_again_3=str(input("PLay again?"))
            if play_again_3==("yes"):
                exit_game_3=True
                exit_game_2=True
                exit_game_1=False
                level_one=True
                level_two=False
                level_three=False
        else:
            print("Try again next time.")
            exit_game_3=True
            play_again_3=str(input("PLay again?"))
            if exit_game_3==True:
                if play_again_3==("yes"):
                    exit_game_3=True
                    exit_game_2=True
                    exit_game_1=False
                    level_one=True
                    level_two=False
                    level_three=False
                else:
                    print("Good luck on your journy trainer")
            

