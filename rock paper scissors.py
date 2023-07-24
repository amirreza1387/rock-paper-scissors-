 countlog = 0
countlog2=0
couantall=0
save=open("userpass.txt","+a")
while couantall<=0 :
    #_______variable_________#
    import random

    options = ["rock","paper","scissors"]

    countlog=0
    countlog2=0
    cmp=0

    player=0
    
    countreg = 0

    user= ("1")
    passw=("2")
    #_________define______#
    quastion=input("do you have an account? yes/no : ")
    while countlog <= 2 :
        if quastion == ("yes"):
            print ('''
            -----------
           [ login page ]
            -----------
           ''' )
            userr= input("username :")
            passrr= input("password :")
            if userr==user and passrr==passw:
                print("login succesful")
        
                count= int(input("sar chanta????"))
                
                while countlog >= 0 :
                                
                    player_ch= input("""

                    chose rock , paper or scissors : """)

                    computer_ch= random.choice(options)

                    print ("""
                    
                    you chose:""" , player_ch)
                    print ("""opponet chose:""" , computer_ch)
                            
                            
                    if player_ch==computer_ch :
                     print("round raw!  ")
                     print (f"{player}:{cmp}")
                                

                    elif player_ch==("rock") and computer_ch==("paper") or player_ch==("scissors") and computer_ch==("rock") or player_ch==("paper") and computer_ch==("scissors") :
                        print(" you lost the round ! ") 
                                
                        cmp  += 1
                        print (f"{player}:{cmp}")


                    elif computer_ch==("rock") and player_ch==("paper") or computer_ch==("scissors") and player_ch==("rock") or computer_ch==("paper") and player_ch==("scissors"):
                        print (" you won the round !")  
                        player += 1
                        print (f"{player}:{cmp}")
                                

                    else :
                        print ("enter  vaild choise ")
                                

                            #_______if2________#
                    if player==count :
                     print (f"""
                     
                     
                     you won the mach {player}:{cmp} """) 
                     couantall+=1
                     countlog+=3
                     break
                        
                    
                

                    elif cmp==count :
                     print (f"""
                                
                                           
                     you lost the mach {player}:{cmp} """)
                     countlog+= 3
                     couantall+= 1
                     break
             
            if  userr!=user and passrr!=passw: 
                    print("login unsuccesfull")  
                    countlog += 1 
            
                    print (f"{countlog}/ 3")
                    if countlog >= 3:
                         print("you tried many times")
                         couantall += 1      
               
                        
                
                
                  
                    
                         
         
        elif quastion == ("no"):
             while countlog2 <= 2 : 
                    print ("""
                  ------------
                [ register page ]
                  -------------
                            """)
                    print ("create an account")
                    user1= input("create username :")
                    passw1= input("create password :")
                    passw11= input("enter password again :")
                    if user1 == "hacker" or passw1=="hacker" :
                        print ("you are a hacker ? suck my d.ck [: ")
                        couantall += 1      
                        break
                    elif user1==passw1:
                        print("""
                        your username and password are the same!!
                        """)
                        couantall += 1
                        break

                    if passw1 != passw11 :
                    
                        countlog2+=1
                        print (f"""passwords are not the same ! 
{countlog2} / 3""")
                        if countlog2 == 3:
                            print("you tried many times")
                            couantall +=10
                        break

                    elif passw1 == passw11:
                        print ( f"""--------------------------
[ account succesfuly created ]
[ username : {user1}                ]
[ password : {passw1}              ]
--------------------------""")
                    
                        print("""
                         -----------
                        [game started]
                         -----------
                        """)
                        count= int(input("sar chanta????"))
                    while countlog >= 0 :
                            
                         player_ch= input("""

                         chose rock , paper or scissors : """)

                         computer_ch= random.choice(options)

                         print ("""you chose:""" , player_ch)
                         print ("""opponet chose:""" , computer_ch)
                                
                                
                         if player_ch==computer_ch :
                            print("round raw!  ")
                            print (f"{player}:{cmp}")
                                    

                         elif player_ch==("rock") and computer_ch==("paper") or player_ch==("scissors") and computer_ch==("rock") or player_ch==("paper") and computer_ch==("scissors") :
                            print(" you lost the round ! ") 
                                    
                            cmp  += 1
                            print (f"{player}:{cmp}")


                         elif computer_ch==("rock") and player_ch==("paper") or computer_ch==("scissors") and player_ch==("rock") or computer_ch==("paper") and player_ch==("scissors"):
                            print (" you won the round !")  
                            player += 1
                            print (f"{player}:{cmp}")
                                    

                         else :
                            print ("enter  vaild choise ")
                                    

                                #_______if2________#
                         if player==count :

                            print (f"""
                            
                            
                            you won the mach {player}:{cmp} """) 
                            couantall += 1
                            countlog2 += 20
                            break
                                
                            
                        

                         elif cmp==count :
                            print (f"""
                                        
                                     
                            you lost the mach {player}:{cmp} """)
                            couantall+=1
                            countlog2 += 2
                            break
   
   
                    
            
   
        else :
                print ("""
    answer me with yes or no !
                """)
                break  
