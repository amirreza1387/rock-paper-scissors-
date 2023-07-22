#_______variable_________#
import random

options = ["rock","paper","scissors"]


cmp=0

player=0


#_______function_______#
count = int(input("sar chanta??"))
while True :
    
    player_ch= input("""

    chose rock , paper or scissors : """)

    computer_ch= random.choice(options)

    print ("""you chose:""" , player_ch)
    print ("""opponet chose:""" , computer_ch)
 
   

    if player_ch==computer_ch :
      print("""
    
round raw!  """)
      print (f"{player}:{cmp}")
      

    elif player_ch==("rock") and computer_ch==("paper") or player_ch==("scissors") and computer_ch==("rock") or player_ch==("paper") and computer_ch==("scissors") :
      print("""
      
you lost the round ! """) 
      
      cmp  += 1
      print (f"{player}:{cmp}")


    elif computer_ch==("rock") and player_ch==("paper") or computer_ch==("scissors") and player_ch==("rock") or computer_ch==("paper") and player_ch==("scissors"):
        print ("""
 
you won the round !""")  
        player += 1
        print (f"{player}:{cmp}")
       

    else :
      print ("enter  vaild choise ")
    


    if player==count :
       print (f"""you won the mach {player}:{cmp}  
       
       
       
       
       
       
       
       """)
       break

    if cmp==count :
        print (f"""
        
        
        
        
        
        
        
        
        you lost the mach {player}:{cmp} """)
        break
