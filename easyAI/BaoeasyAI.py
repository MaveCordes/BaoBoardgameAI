import baofunctions as bck
from copy import deepcopy
import numpy as np
import random

class TwoPlayerGame:

    def play(self, nmoves=1000, verbose=True):

        history = []

        if verbose:
            self.show()

        for self.nmove in range(1, nmoves + 1):

            if self.is_over():
                break

            move = self.player.ask_move(self)
            history.append((deepcopy(self), move))
            self.make_move(move)

            if verbose:
                print("\nMove #%d: player %d plays %s :" % (
                      self.nmove, self.current_player, str(move)))
                self.show()

            self.switch_player()

        history.append(deepcopy(self))

        return history

    @property
    def nopponent(self):
        return 2 if (self.current_player == 1) else 1

    @property
    def player(self):
        return self.players[self.current_player - 1]

    def switch_player(self):
        self.current_player = self.nopponent

    def copy(self):
        return deepcopy(self)


class Bao(TwoPlayerGame):

    def __init__(self, players):
        self.players = players
        self.playboard = [[2 for j in range(8)] for x in range(4)]
        self.current_player = 1
        self.store = np.copy(self.playboard)

    def possible_moves(self):
        if self.current_player == 1:
            move = [[i, k] for i in range(1, 9)
                    for k in range(1, 3) if self.playboard[3][i - 1] >= 2]
        else:
            move = [[i, k] for i in range(1, 9)
                    for k in range(1, 3) if self.playboard[0][i - 1] >= 2]
        return move

    def make_move(self, move):
        #true the bottom "baoprint" variable to print all moves instead of only the endboard
        baoprint = True
        bck.game.calculation(self, self.playertoy(), move[0] - 1, move[1], self.playboard, baoprint)
        
    def make_move_AI(self, move):
        baoprint = False
        bck.game.calculation(self, self.playertoy(), move[0] - 1, move[1], self.playboard, baoprint)
        
    def show(self):
        """
        self.playboard = [[1, 2, 1, 3, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 5, 1, 1, 1, 1],
                          [2, 2, 2, 2, 2, 2, 8, 2]]
        """
        tophalf = [[0 for j in range(8)] for x in range(2)]
        bothalf = [[0 for j in range(8)] for x in range(2)]
        for t in range(2):
            tophalf[t] = self.playboard[t]
        for u in range(2, 4):
            bothalf[u - 2] = self.playboard[u]

        p1 = (sum(self.playboard[2] + self.playboard[3]))
        p2 = (sum(self.playboard[0] + self.playboard[1]))
    

        print('\n', ' | '.join(map(str, range(1, 9))), '\n', 30 * '—',
              '\n' + '\n'.join(['  '.join(['{:2}'.format(item) for item in row])
                                for row in tophalf]), ' P2', p2, '\n' + 32 * '‑',
              '\n' + '\n'.join(['  '.join(['{:2}'.format(item) for item in row])
                                for row in bothalf]), ' P1', p1, '\n', 30 * '—', '\n ⟽  |1|   direction   |2|  ⟾  ',
              '\n', '\n')

    def win(self):
        if self.current_player == 1:
            return all(x <= 1 for x in self.playboard[0]) or sum(self.playboard[1]) == 0
        if self.current_player == 2:
            return all(x <= 1 for x in self.playboard[3]) or sum(self.playboard[2]) == 0

    def lose(self):
        if self.current_player == 1:
            return self.possible_moves() == [] or all(x <= 1 for x in self.playboard[3]) or sum(self.playboard[2]) == 0
        if self.current_player == 2:
            return self.possible_moves() == [] or all(x <= 1 for x in self.playboard[0]) or sum(self.playboard[1]) == 0

    def is_over(self):
        return self.win() or self.lose()

    def scoring(self):   
        if rnd == False :   
            if self.current_player == 1 :
                value = sum(self.playboard[2] + self.playboard[3]) - sum(self.playboard[0] + self.playboard[1])
                return value
            if self.current_player == 2 : 
                value = sum(self.playboard[0] + self.playboard[1]) - sum(self.playboard[2] + self.playboard[3])
                return value
            if self.win():
                return 100
            if self.lose():
                return -100   
        if rnd == True:
            rnd_num = random.randrange(-100, 100, 1)
            return rnd_num

    def playertoy(self):
        if self.current_player == 1:
            y = 3
            return y
        if self.current_player == 2:
            y = 0
            return y

class ask:

    def ask(self):
        global varplayer, easy, rnd
        rnd = False
        while True:
            try:
                player = int(input(
                    '\n'"Do you want to play against an Human or an AI Player? \n(1) Human Player \n(2) AI Player : "))
            except ValueError:
                print("Enter '1' to play against an Human, enter '2' to play against an AI Player")
                continue
            if 0 < player < 3:
                if player == 1:
                    varplayer = Human_Player()
                    return varplayer
                if player == 2:
                    while True:
                        try:
                            diffint = int(input(
                                '\n'"Please choose the difficulty \n(1) easy \n(2) medium \n(3) hard \n(4) impossible: "))
                        except ValueError:
                            print(
                                "Please choose the difficulty, type '1' for easy, '2' for medium, '3' for hard, '4' for impossible")
                            continue
                        if 0 < diffint < 5:
                            if diffint == 1:
                                difficult = SSS(1)
                                rnd = True
                                easy = 1
                                print("You chose easy")
                            if diffint == 2:
                                difficult = SSS(1)
                                easy = 2
                                print("You chose medium")
                            if diffint == 3:
                                difficult = Negamax(2)
                                easy = 3
                                print("You chose hard")
                            if diffint == 4:
                                difficult = Negamax(3)
                                easy = 3
                                print("You chose impossible")
                            varplayer = AI_Player(difficult)
                            return varplayer, easy, rnd


if __name__ == "__main__":
    
    from AI import Negamax, SSS
    from Player import Human_Player, AI_Player
    
    ask.ask(self=None)    
    
    game = Bao([Human_Player(), varplayer])
    game.play()

    if game.win():
        print("Player %d wins after %d turns" % (game.current_player, game.nmove))
    if game.lose():
        print("Player %d wins after %d turns" % (game.nopponent, game.nmove))
        
