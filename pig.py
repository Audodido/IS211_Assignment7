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


    def message(self, player):
        self.player = player
        # randomly varies message players sees after each roll
        msg_bank = {1 : f'Ok player {self.players[player].name}, you\'ve got {self.players[player].turn_total} on this turn so far.',
                    2 : f'Current turn-total for player {self.players[player].name}: {self.players[player].turn_total}',
                    3 : f'player {self.players[player].name}\'s total this turn: {self.players[player].turn_total}'}

        return msg_bank[random.randint(1,3)]


    def turn(self, player): 
        self.player = player
        self.players[player].turn_total = 0 #reset player's turn_total to zero        
        roll_prompt = 'Enter "r" to roll. Enter "h" to hold.'
        
        turn = True

        if not self.is_game_over():
            while turn:
                print('-' * 50)
                #player is shown their score
                print(f'Player {self.players[player].name} — current game total: {self.players[player].overall_total}')

                #player gets roll_prompt - makes choice
                choice = input(roll_prompt)
                #if roll: roll 
                if choice == 'r':
                    roll = self.die.roll()
                    if roll != 1:
                        self.players[player].turn_total += roll
                        if not self.is_game_over(): #check if anyone has 100
                            print(f'Die rolls: {roll}')
                            print(self.message(player))
                        else: # else hold: becomes next players turn.
                            print(f'We have a winner: Player {self.players[player].name}') #refactor to method?
                    else:
                        print(f'Snake eye! player {self.players[player].name} loses their turn and receives no points')
                        print(f'Your game total is STILL {self.players[player].overall_total}. Next up!')
                        turn = False
                
                elif choice == 'h':
                    self.players[player].overall_total += self.players[player].turn_total

                    if not self.is_game_over():
                        print(f'Ok then player {self.players[player].name}. Your game total is now {self.players[player].overall_total}. Next up!')
                        turn = False
                    else:
                        # self.players[player].overall_total += self.players[player].turn_total
                        print(f'Ok then player {self.players[player].name}. Your game total is now {self.players[player].overall_total}. That means...')
                        print(f'We have a winner: Player {self.players[player].name}') #refactor to method?            
                        turn = False
                        break
                
                else:
                    print('Must enter an \'r\' or \'h\'. Try again')



    def play(self):

        while not self.is_game_over():
            for p in range(len(self.players)):
                self.turn(p)



if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument("--players", help="Number of players", type=int, required=False)
    args = parser.parse_args()

    print("Welcome to Pig")
    players = []
    die = Die()

    if args.players != None:
        for p in range(args.players):
            p += 1
            players.append(Player(str(p))) #create an instance of a Player() for each player specified by argument

    else:
        players = [Player('1'), Player('2')] #else default to two players
    

    game = Game(die, players)
    game.play() 

