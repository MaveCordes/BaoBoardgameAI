
#try:
 #   input = raw_input
#except NameError:
 #   pass


class Human_Player:

    def __init__(self, name = 'Human'):
        self.name = name

    def ask_move(self, game):
        possible_moves = game.possible_moves()
        possible_moves_str = list(map(str, game.possible_moves()))
        move = [0,0]
        print('\n'+'Possible moves : '+'\n' + 40*'—','\n'+ "".join(["| %d |" % possible_moves[t][0] for t in range(0,len(possible_moves),2)]))
        while True:
            try:
                pos = int(input("Player %s, what is your next move? : " % (game.current_player)))
                dir = int(input("What direction do you want to go : "))
                if dir not in (1,2):
                    print("You can only move in two directions with your stones. Type (1) to move clockwiese or (2) to move counter-clockwise")
                    continue

            except ValueError:
                print("You can only enter numbers")
                continue

            move[0],move[1] = pos, dir
            #if pos == 99:
            #    raise KeyboardInterrupt

            if str(move) in possible_moves_str:
                move = possible_moves[possible_moves_str.index(str(move))]
                return move

            print('\n'+'You cant start from this position.''\n'+'Remeber that you need at least two stones in the last row to start a move.''\n'+'Here are all possible starting positions again''\n' + "".join(
                ["| %d |" % possible_moves[t][0] for t in range(0, len(possible_moves), 2)]))


class AI_Player:

    def __init__(self, AI_algo, name = 'AI'):
        self.AI_algo = AI_algo
        self.name = name
        self.move = {}

    def ask_move(self, game):
        return self.AI_algo(game)
