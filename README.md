# TicTacToe
Tic-tac-toe game. thats it :)

## How it works
First of all run main.py
For choosing your move in game you should enter row number then column number. Every rows will counted from 0 to demension up to down, columns will counted from 0 to demension left to right. Look at this example below:
    `
    --------------------\n
    | None | None | None |\n
    --------------------\n
    | None | None | None |      #empty game \n
    --------------------\n
    | None | None | None |\n
    --------------------\n
    x turn:11   #player x entered row1 column1   /n
    --------------------  /n
    | None | None | None |  /n
    --------------------  /n
    | None | x | None |         #after first move  /n
    --------------------  /n
    | None | None | None |  /n
    -------------------- /n
    o turn:02   #player x entered row0 column2  /n
    --------------------  /n
    | None | None | o |  /n
    -------------------- /n
    | None | x | None |         #after second move  /n
    --------------------  /n
    | None | None | None |  /n
    --------------------  /n
    `

## TODO
- [ ] simple GUI 
- [ ] show errors instead of crash
- [ ] more feature for player and game classes