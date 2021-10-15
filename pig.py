# ask player1 to roll
# they receive a random# from the die
# the number is added to player1 turn_total
# present turn_total and overall_total and ask player1 if they want to roll or hold
# if roll: they receive a random# from the die, the number is added to player1 turn_total
# elif hold: ask player2 to roll
# answer: 'hold'

# player2 receive a random# from the die
# the number is added to player1 turn_total
# present turn_total and overall_total and ask player2 if they want to roll or hold
# if roll: they receive a random# from the die, the number is added to player1 turn_total
# elif hold: add turn_total to overall_total, set turn_total=0 and then ask player2 to roll

#this all repeats while player1 overall_total < 100 OR player2 overall_total < 100 


#main entry area:

# create player obects and die object
# create game object 
# game.play()

# while player1 overall_total < 100 OR player2 overall_total < 100:
#   ask player whose turn it is (turn==True) to roll or hold
#   if hold: turn=False
#   elif roll: call die_object.roll_method
#   add number to player_turn_total
#   show player their totals and ask if they want to roll or hold
#   call die_object.roll_method
#   if hold: turn=False
# HOLD
#   ask player to roll or hold
#   if hold: turn=False
#   elif roll: call die_object.roll_method
#   add number to player_turn_total
#   show player their totals and ask if they want to roll or hold

#psuedo
##############################################
import argparse
import random

class Player:

    def __init__(self, name):
        self.name = name
        self.overall_total = 0
        self.turn_total = 0


class Die:
    
    def __init__(self, sides=6):
        self.sides = sides 

    def roll(self):
        dots = random.randint(1,6)
        return dots


class Game:
    
    def __init__(self, die, players):
        self.players = players
        self.die = die

    def is_game_over(self):
        for player in self.players:
            if player.overall_total >= 100:
                return True
        else:
            return False
        

    def turn(self, player): #call this with player == p
        self.player = player
        self.players[player].turn_total = 0 #reset player's turn_total to zero        
        roll_prompt = 'Enter "r" to roll. Enter "h" to hold.'

        #player is shown their score
        print(f'Player {self.players[player].name} — current game total: {self.players[player].overall_total}')
        
        turn = True

        while turn:
            #player gets roll_prompt - makes choice
            choice = input(roll_prompt)
            #if roll: roll 
            if choice == 'r':
                roll = self.die.roll()
                if roll != 1:
                    self.players[player].turn_total += roll
                    if not self.is_game_over(): #check if anyone has 100
                        print(roll)
                        print(f'Ok player {self.players[player].name}, you\'ve got {self.players[player].turn_total} on this turn so far.')
                        print(f'And your game total is {self.players[player].overall_total}')       
                    else: # else hold: becomes next players turn.
                        print(f'We have a winner: Player {self.players[player].name}') #refactor to method?
                else:
                    print(f'Snake eye! player {self.players[player].name} loses their turn and receives no points')
                    print(f'Your game total is STILL {self.players[player].overall_total}. Next up!')
                    turn = False
            
            elif choice == 'h':
                if not self.is_game_over():
                    self.players[player].overall_total += self.players[player].turn_total
                    print(f'Ok then player {self.players[player].name}. Your game total is now {self.players[player].overall_total}. Next up!')
                    turn = False
                else:
                    print(f'We have a winner: Player {self.players[player].name}') #refactor to method?


    def play(self):

        while not self.is_game_over():
            for p in range(len(self.players)):
                self.turn(p)
                

                # while turn:
                    # choice = input(roll_prompt)

                    # if choice == 'r':
                    #     roll = die.roll()
                        
                    #     if roll != 1:
                    #         self.players[p].turn_total += roll
                    #         print(roll)
                    #         print(f'Ok player {self.players[p].name}, you\'ve got {self.players[p].turn_total} on this turn so far.')
                    #         print(f'And your game total is {self.players[p].overall_total}')
                        # else:
                            # print(f'Snake eye! player {self.players[p].name} loses their turn and receives no points')
                            # print(f'Your game total is now {self.players[p].overall_total}. Next up!')
                            # turn = False

                    # elif choice == 'h':
                    #     self.players[p].overall_total += self.players[p].turn_total
                    #     print(f'Ok then player {self.players[p].name}. Your game total is now {self.players[p].overall_total}. Next up!')
                    #     turn = False

        # print(f'We have a winner: Player {self.players[p].name}')




if __name__ == "__main__":

###############################################
    ##**For extra credit**
    #Ask: how many players? 
    #for i in range(# of players input):
    #   create an instance of player


    print("Welcome to Pig")
    die = Die()
    #players = input('How many players?: ')
    players = [Player('one'), Player('two')]
    game = Game(die, players)
    game.play() 

