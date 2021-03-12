import tkinter as tk
from models import Game, Player


def add_players(game):
#add players to game by player_count automaticly
    for i in range(game.player_count):
        player = Player(f'player{i+1}')
        game.add_player(player)


def lock_all_buttons(buttons):
    for row in buttons:
        for button in row:
            button.configure(state='disabled')


def make_and_get_object(root, object):
#make label and entry in a frame and pack it in root
    frame = tk.Frame(master=root)
    label = tk.Label(master=frame, text=f'Enter {object}:')
    label.grid(row=0, column=0)
    entry = tk.Entry(master=frame, textvariable=f'{object}')
    entry.grid(row=0, column=1)
    frame.pack()
    return entry


def clicked(pos, game, buttons, label):
    game.elements[int(pos[0])][int(pos[1])] = check_turn(game).name
    label.config(text=f'{who_is_turn(game)} turn:')
    buttons[int(pos[0])][int(pos[1])].configure(text=game.elements[int(pos[0])][int(pos[1])], state='disabled')
    if game.win_check(pos) == True:
        label.config(text=f'{game.elements[int(pos[0])][int(pos[1])]} won')
        lock_all_buttons(buttons)


def create_game_start(root, demension, win_on, player_count):
    #create and start game
    buttons = []
    game = Game(demension, win_on, player_count)
    elements = game.elements
    add_players(game)
    game.players[0].status = True
    top = tk.Toplevel(root)
    label = tk.Label(top, text=f'{who_is_turn(game)} turn:')
    label.grid(row=0,column=0)
    frame = tk.Frame(top)
    for i in range(len(elements)):
        buttons.append([])
        for j in range(len(elements[i])):
            button = tk.Button(frame, relief = tk.RAISED, borderwidth=5, text=f'{elements[i][j]}')
            button.config(command=lambda current_pos=f'{i}{j}': clicked(current_pos, game, buttons,label))
            button.grid(row=i,column=j)
            buttons[i].append(button)
    frame.grid(row=1, column=0)
    top.mainloop()


def who_is_turn(game):
    for player in game.players:
        if player.status == True:
            return player


def check_turn(game):
    for i in range(len(game.players)):
        if game.players[i].status == True:
            game.players[i].status = False
            if i == len(game.players)-1:
                game.players[0].status = True
            else:
                game.players[i+1].status = True
            return game.players[i]


def main():
    #main window
    root = tk.Tk()
    demension = make_and_get_object(root, 'demension')
    win_on = make_and_get_object(root, 'win on')
    player_count = make_and_get_object(root, 'player count')
    frame = tk.Frame(master=root)
    frame.pack()
    button = tk.Button(master=frame, command=lambda: create_game_start(root,int(demension.get()),int(win_on.get()),int(player_count.get())), text='start')
    button.pack(side=tk.LEFT)
    root.mainloop()




main()
