import time

class game:

    def board(playboard):
         return ('\n'.join(['  '.join(['{:2}'.format(item) for item in row])
                           for row in playboard]))
         
    def print_board(playboard) :
        tophalf = [[0 for j in range(8)] for x in range(2)]
        bothalf = [[0 for j in range(8)] for x in range(2)]
        for t in range(2):
            tophalf[t] = playboard[t]
        for u in range(2, 4):
            bothalf[u - 2] = playboard[u]

        p1 = (sum(playboard[2] + playboard[3]))
        p2 = (sum(playboard[0] + playboard[1]))
     
        print(30 * '—',
              '\n' + '\n'.join(['  '.join(['{:2}'.format(item) for item in row])
                                for row in tophalf]), ' P2', p2, '\n' + 32 * '‑',
              '\n' + '\n'.join(['  '.join(['{:2}'.format(item) for item in row])
                                for row in bothalf]), ' P1', p1, '\n', 30 * '—', '\n')
        return 
        
    def calculation(self, y, position, clockwise, playboard, baoprint):
        global hand
        global varp
        hand = playboard[y][position]
        playboard[y][position] = 0
        if position == 0:
            if y == 3 and clockwise == 1:
                varp = (-1)
                game.up(2, playboard, baoprint)
            if y == 0 and clockwise == 2:
                varp = (-1)
                game.up(1, playboard, baoprint)
        if position == 7:
            if y == 3 and clockwise == 2:
                varp = 8
                game.down(2, playboard, baoprint)
            if y == 0 and clockwise == 1:
                varp = 8
                game.down(1, playboard, baoprint)
        if y == 0:
            if clockwise == 1:
                clockwise = 2
            else:
                clockwise = 1
        if clockwise == 1:
            for varp in range(hand):
                hand = hand - 1
                if hand == 0 and playboard[y][position - varp - 1] == 0:
                    playboard[y][position - varp - 1] = playboard[y][position - varp - 1] + 1
                    if baoprint:
                        print("Stones in Hand: %d" % (hand))    
                        game.print_board(playboard)
                        time.sleep(1)
                    return
                playboard[y][position - varp - 1] = playboard[y][position - varp - 1] + 1
                if baoprint:
                    print("Stones in Hand: %d" % (hand))    
                    game.print_board(playboard)
                    time.sleep(1)
                if hand == 0:
                    hand = playboard[y][position - varp - 1]
                    playboard[y][position - varp - 1] = 0
                    varp = (position - varp - 1)
                    if baoprint:
                        print("Stones in Hand: %d" % (hand))    
                        game.print_board(playboard)
                        time.sleep(1)
                    if y == 0:
                        game.down(0, playboard, baoprint)
                    if y == 3:
                        game.down(3, playboard, baoprint)
                    else:
                        return
                if (position - varp - 1) == 0:
                    if y == 3:
                        varp = -1
                        game.up(2, playboard, baoprint)
                        return
                    if y == 0:
                        varp = -1
                        game.up(1, playboard, baoprint)
                        return
        if clockwise == 2:
            for varp in range(hand):
                hand = hand - 1
                if hand == 0 and playboard[y][position + varp + 1] == 0:
                    playboard[y][position + varp + 1] = playboard[y][position + varp + 1] + 1
                    if baoprint:
                        print("Stones in Hand: %d" % (hand))    
                        game.print_board(playboard)
                        time.sleep(1)
                    return
                playboard[y][position + varp + 1] = playboard[y][position + varp + 1] + 1
                if baoprint:
                    print("Stones in Hand: %d" % (hand))    
                    game.print_board(playboard)
                    time.sleep(1)
                if hand == 0:
                    hand = playboard[y][position + varp + 1]
                    playboard[y][position + varp + 1] = 0
                    varp = (position + varp + 1)
                    if baoprint:
                        print("Stones in Hand: %d" % (hand))    
                        game.print_board(playboard)
                        time.sleep(1)
                    if y == 0:
                        game.up(0, playboard, baoprint)
                    if y == 3:
                        game.up(3, playboard, baoprint)
                    else:
                        return
                if (position + varp + 1) == 7:
                    if y == 3:
                        varp = 8
                        game.down(2, playboard, baoprint)
                        return
                    if y == 0:
                        varp = 8
                        game.down(1, playboard, baoprint)
                        return


    def up(y, playboard, baoprint):
        global hand
        global varp
        for b in range(hand):
            if (varp + b + 1) >= 8:
                varp = (varp + b + 1)
                if y == 3:
                    game.down(2, playboard, baoprint)
                    return
                if y == 2:
                    game.down(3, playboard, baoprint)
                    return
                if y == 1:
                    game.down(0, playboard, baoprint)
                    return
                if y == 0:
                    game.down(1, playboard, baoprint)
                    return
            hand = hand - 1
            if hand == 0 and playboard[y][varp + b + 1] == 0:
                playboard[y][varp + b + 1] = playboard[y][varp + b + 1] + 1
                if baoprint:
                    print("Stones in Hand: %d" % (hand))    
                    game.print_board(playboard)
                    time.sleep(1)
                return
            playboard[y][varp + b + 1] = playboard[y][varp + b + 1] + 1
            if baoprint:
                print("Stones in Hand: %d" % (hand))    
                game.print_board(playboard)
                time.sleep(1)
            if hand == 0:
                hand = playboard[y][varp + b + 1]
                playboard[y][varp + b + 1] = 0
                if y == 1:
                    hand = hand + playboard[2][varp + b + 1]
                    playboard[2][varp + b + 1] = 0
                if y == 2:
                    hand = hand + playboard[1][varp + b + 1]
                    playboard[1][varp + b + 1] = 0
                varp = (varp + b + 1)
                if baoprint:
                    print("Stones in Hand: %d" % (hand))    
                    game.print_board(playboard)
                    time.sleep(1)
                if y == 3:
                    game.up(3, playboard, baoprint)
                if y == 2:
                    game.up(2, playboard, baoprint)
                if y == 1:
                    game.up(1, playboard, baoprint)
                if y == 0:
                    game.up(0, playboard, baoprint)
                return


    def down(y, playboard, baoprint):
        global hand
        global varp
        for b in range(hand):
            if (varp - b - 1) == (-1):
                varp = (varp - b - 1)
                if y == 3:
                    game.up(2, playboard, baoprint)
                    return
                if y == 2:
                    game.up(3, playboard, baoprint)
                    return
                if y == 1:
                    game.up(0, playboard, baoprint)
                    return
                if y == 0:
                    game.up(1, playboard, baoprint)
                    return
            hand = hand - 1
            if hand == 0 and playboard[y][varp - b - 1] == 0:
                playboard[y][varp - b - 1] = playboard[y][varp - b - 1] + 1
                if baoprint:
                    print("Stones in Hand: %d" % (hand))    
                    game.print_board(playboard)
                    time.sleep(1)
                return
            playboard[y][varp - b - 1] = playboard[y][varp - b - 1] + 1
            if baoprint:
                print("Stones in Hand: %d" % (hand))    
                game.print_board(playboard)
                time.sleep(1)
            if hand == 0:
                hand = playboard[y][varp - b - 1]
                playboard[y][varp - b - 1] = 0
                if y == 1:
                    hand = hand + playboard[2][varp - b - 1]
                    playboard[2][varp - b - 1] = 0
                if y == 2:
                    hand = hand + playboard[1][varp - b - 1]
                    playboard[1][varp - b - 1] = 0
                varp = (varp - b - 1)
                if baoprint:
                    print("Stones in Hand: %d" % (hand))    
                    game.print_board(playboard)
                    time.sleep(1)
                if y == 3:
                    game.down(3, playboard, baoprint)
                if y == 2:
                    game.down(2, playboard, baoprint)
                if y == 1:
                    game.down(1, playboard, baoprint)
                if y == 0:
                    game.down(0, playboard, baoprint)
                return