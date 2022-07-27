BaoeasyAI
---------
Simple boardgame called BAO implemented in easyAI provided by Zulko_ (zulko.github.io/easyai/)
Play against another player or the AI

How to play
-----------
Start by selecting if you want to play against a Human Player or the AI.

    Do you want to play against an Human or an AI Player? 
    (1) Human Player 
    (2) AI Player : 

If you decided to play against the AI you can choose the difficulty

    Please choose the difficulty
    (1) easy 
    (2) medium 
    (3) hard 
    (4) impossible: 

The game is easily explained. Every Player has two rowes filled with stones. To win the game you have to win all stones from your opponent from the row facing the middle of the board. (Opponent second row)
Your moves can only start from your first row if you have more than on stone in your field. If you only have 0 or 1 stones in every field of the last row you lose. 
After choosing a starting position (1-8) you can choose in wich direction you want to distibute your stones (clockwise or counterclockwise).
P1 and P2 indicate the total stones of each player on the board.
    
    1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 
    —————————————————————————————— 
    2   2   2   2   2   2   2   2           <- Opponent first row
    2   2   2   2   2   2   2   2  P2 32    <- Opponent second row
    ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑ 
    2   2   2   2   2   2   2   2           <- Your second row
    2   2   2   2   2   2   2   2  P1 32    <- Your first row
    —————————————————————————————— 
    ⟽  |1|   direction   |2|  ⟾   


    Possible moves : 
    ———————————————————————————————————————— 
    | 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 |

    Player 1, what is your next move? : 
    What direction do you want to go : 

Take all the stones from your chosen starting postion and start to drop one stone into each following field one by one. If the last stone from your hand is put into a field containing one or more stones, pick all stones from that field and continue the move
in the originally chosen direction. A special condition: if your last stone is put into a field in the row of the inner circle, you are allowed to take all the stones from your opponent.
Your move ends if the last stone of your hand hits an empty field on your playboard.

e.g. if you decide to make to move [1,1] (first position, clockwise), the next two moves would look like this:

    Stones in Hand: 1
    —————————————————————————————— 
    2   2   2   2   2   2   2   2
    2   2   2   2   2   2   2   2  P2 32 
    ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑ 
    3   2   2   2   2   2   2   2
    0   2   2   2   2   2   2   2  P1 31  <- position 1 is empty, one stone is put into position 1 of the inner row adding up to 3.
    —————————————————————————————— 

after you put your next stone into position 2 of the inner row, you will take all your stones and the stones from your opponent

    Stones in Hand: 5
    —————————————————————————————— 
    2   2   2   2   2   2   2   2
    2   0   2   2   2   2   2   2  P2 30 
    ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑ 
    3   0   2   2   2   2   2   2
    0   2   2   2   2   2   2   2  P1 29 
    —————————————————————————————— 

your turn will continue until you put your last stone into an empty field. After that its the opponents turn.

as possible ending-board would look like this:

    1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 
    —————————————————————————————— 
    6   7   5   1   0   7   4   2
    1   5   1   1   2   0   4   5  P2 51 
    ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑ 
    0   0   0   0   0   0   0   0         <- Whole row is 0
    1   2   1   0   1   4   4   0  P1 13 
    —————————————————————————————— 
    ⟽  |1|   direction   |2|  ⟾   
    

    Player 2 wins after 21 turns

I lost against the AI! Enjoy playing!

Installation
------------
Download this rep and in terminal type
    
    sudo python setup.py install

numpy and time lib for manual install required

    pip install numpy
    pip install time


Credits
------------
All credits for the easyAI Framework go to Zulko_ and easyAI.
