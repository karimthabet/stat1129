#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import random
# Import  module for text-to-speech conversion (bonus)
import gtts
from playsound import playsound
# This module is imported so that we can play the converted audio
import os
import time

#Exception handling 

class AgeNotInRangeError(Exception):
    
    def _exception_(self, age, message="Invalid age!"):
        self.age=age
        self.message=message
        super()._exception_(self.message)

age=int(input("Enter your age: "))
if not int:
    raise AgeNotInRangeError(age)
    
class RPS:
    """
    Rock-Paper-Scissors class 
    """

    def __init__(self):
        self.n=3
        self.ties = 0
        self.wins = 0
        self.losses = 0 
        self.choice = {'rock': 0, 'paper': 1, 'scissors': 2} #insert key as a value 
        self.player_name=" "

    def rand_choice(self): #computer chooses a key     
        return random.choice(list(self.choice.keys()))

    def who_wins(self, player, comp):    
        result = (player - comp) % 3
        if result == 0:
            self.ties += 1
            print("It's is a tie! ")
        elif result == 1:
            self.wins += 1
            print(self.player_name + ' wins!')  
        elif result == 2:
            self.losses += 1
            print("Computer wins the game!")


    def welcome(self):
        self.player_name=input("Enter your name:\n")
        print('Hello  ' + self.player_name)
        print(self.player_name + ' is playing against the computer')
        
        

       #This creates randomized names for the mp3 file (using the same name produces an error)
    
        r1 = random.randint(1,10000000)
        r2 = random.randint(1,10000000)

        randfile = str(r2)+"randomtext"+str(r1) +".mp3" #improves of chance of non repetition 
        tts = gtts.gTTS(text='Hello' + self.player_name, lang='en', slow=True)
        tts.save(randfile)
        
        #Playing the converted file (sound)
        
        playsound(randfile)
        os.remove(randfile)

        
        
    def print_score(self):
        print("\n")
        print(f"Final Score is: ")
        print(self.player_name + f" won {self.wins} wins, Computer won {self.losses} wins, and " f" there is/are {self.ties} ties.")
        if self.wins>self.losses:
            print(self.player_name + ' ' + 'WINS')
        elif self.wins<self.losses:
            print( 'Computer WINS')
        elif self.wins== self.losses:
            print ("It's a tie, no winner yet")
    
    def valid(self):               
        for self.n in range(1,4):
             while True:
                 playerchoice = input("Choose one option: 'rock', 'paper', or 'scissors'.\n"
                               ).lower()
                 if playerchoice not in self.choice.keys():
                     print("Invalid choice, try again!")
                 else:
                    break
             comp_choice = self.rand_choice()
             print(self.player_name + f" selected {playerchoice}, Computer selected {comp_choice}.")
             self.who_wins(self.choice[playerchoice], self.choice[comp_choice])
     
    
    # Extending the game when there is a tie 
    
    def repeat(self):
         while ( {self.wins}=={self.losses}):
             playerchoice = input("Choose one option: 'rock', 'paper', or 'scissors'.\n"
                               ).lower()
             if playerchoice not in self.choice.keys():
                     print("Invalid choice, try again!")
             else:
                    
                 comp_choice = self.rand_choice()
                 print("You selected {playerchoice}, Computer selected {comp_choice}.")
                 self.who_wins(self.choice[playerchoice], self.choice[comp_choice])
                 
                     

if __name__ == "__main__":
  start=time.time()
  while True:
    game = RPS()
    game.welcome()
    game.valid()
    game.print_score()
    game.repeat()
    

    reply = input('\nDo you wish to play again? (y/n): ').lower()
    if reply == 'n':
        print("Game over!")
        d2 = random.randint(1,10000000)

        randfile = str(d2)+"randomtext" +".mp3"
        tts = gtts.gTTS(text='Game over, Goodbye!', lang='en', slow=True)
        tts.save(randfile)
    # Playing the converted file
        playsound(randfile)
        os.remove(randfile) 
        break
    
 #This tells us the time taken to play the game (in sec)
 
end=time.time()
print("The game ended after", (end-start), "sec")


# In[ ]:




