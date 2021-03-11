# TicTacToe
Tic-tac-toe game. thats it :)

## How it works
First of all run main.py
For choosing your move in game you should enter row number then column number. Every rows will counted from 0 to demension up to down, columns will counted from 0 to demension left to right. Look at this example below:
    `
    --------------------
    | None | None | None |
    --------------------
    | None | None | None |      #empty game
    --------------------
    | None | None | None |
    --------------------
    x turn:11   #player x entered row1 column1
    --------------------
    | None | None | None |
    --------------------
    | None | x | None |         #after first move
    --------------------
    | None | None | None |
    --------------------
    o turn:02   #player x entered row0 column2
    --------------------
    | None | None | o |
    --------------------
    | None | x | None |         #after second move
    --------------------
    | None | None | None |
    --------------------
    `

## TODO
- [ ] simple GUI 
- [ ] show errors instead of crash
- [ ] more feature for player and game classes