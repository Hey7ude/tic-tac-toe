from models import Player, Game
        


def start_game_commandline(game):
    elements = game.elements
    flag = 0
    for turn in range(game.demension * game.demension):
        print(f'{game.players[0].get_color()}: x     {game.players[1].get_color()}: o')
        print('----------')
        for row in range(game.demension):
            test = '| '
            for col in range(game.demension):
                test = test + f'{game.elements[row][col]} | '
            print(test)
            print('----------')
        if flag == 0:
            a = input(f'{game.players[0].get_color()} turn:')
            game.elements[int(a[0])][int(a[1])] = 'x'
            flag = 1
        else:
            a = input(f'{game.players[1].get_color()} turn:')
            game.elements[int(a[0])][int(a[1])] = 'o'
            flag = 0

        if game.win_check(a):
            print(f'{elements[int(a[0])][int(a[1])]} won')





def start_game_gui(game):
    import tkinter as tk


    window = tk.Tk()
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(master=window, relief = tk.RAISED, borderwidth=5)
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f'{game.elements[i][j]}')
            label.pack()
    window.mainloop()



game1 = Game(3,3,2)
player1 = Player('red', 0)
game1.add_player(player1)
player2 = Player('blue', 1)
game1.add_player(player2)
start_game_commandline(game1)
start_game_gui(game1)

