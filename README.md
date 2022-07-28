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

The game is easily explained. Every Player has two rowes filled with stones. To win the game you have to take all stones from your opponents second row, the row facing the middle of the board. (opponent second row)
Your move can only start from your first row if you have more than on stone in the starting position. If you only have 0 or 1 stones in every field of your first row you lose. 
After choosing a starting position (1-8) you can choose in wich direction you want to distibute your stones (clockwise or counterclockwise; |1| or |2| ).
P1 and P2 indicate the total stones of each player on the board.
    
    1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 
    —————————————————————————————— 
    2   2   2   2   2   2   2   2           <- opponent first row
    2   2   2   2   2   2   2   2  P2 32    <- opponent second row
    ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑ 
    2   2   2   2   2   2   2   2           <- your second row
    2   2   2   2   2   2   2   2  P1 32    <- your first row
    —————————————————————————————— 
    ⟽  |1|   direction   |2|  ⟾   


    Possible moves : 
    ———————————————————————————————————————— 
    | 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 |

    Player 1, what is your next move? : 
    What direction do you want to go : 

Take all the stones from your chosen starting postion and start to drop one stone into each following field one by one. If the last stone from your hand is put into a field containing one or more stones, pick all stones from that field and continue the move
in the originally chosen direction. A special condition: if your last stone is put on a position on your second row, you are allowed to take all the stones from your opponents second row wich is facing your second row.
Your move ends if the last stone of your hand hits an empty position on your playboard.

e.g. if you decide to make the move [1,1] (first position, clockwise), the next two moves should look like this:

    Stones in Hand: 1
    —————————————————————————————— 
    2   2   2   2   2   2   2   2
    2   2   2   2   2   2   2   2  P2 32 
    ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑ 
    3   2   2   2   2   2   2   2
    0   2   2   2   2   2   2   2  P1 31  <- position 1 was taken empty, one stone is put into position 1 of the second row
    —————————————————————————————— 

after you put your next stone into position 2 of the second row, you will take all your stones and the stones from your opponents position

    Stones in Hand: 5
    —————————————————————————————— 
    2   2   2   2   2   2   2   2
    2   0   2   2   2   2   2   2  P2 30  <- take your opponents stones
    ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑ 
    3   0   2   2   2   2   2   2
    0   2   2   2   2   2   2   2  P1 29 
    —————————————————————————————— 

your turn will continue until you put your last stone into an empty position. After that its the opponents turn.

A possible ending-board would look like this:

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

If you dont have a virtual python env running create one and activate it

    python3 -m venv .easyAI
    source .easyAI/bin/activate

Download this rep and in terminal type
    
    sudo python setup.py install

numpy and time lib for manual install required

    pip install numpy
   
start by executing BaoeasyAI.py


Credits
------------
All credits for the easyAI Framework go to Zulko_ and easyAI.
