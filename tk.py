import tkinter as tk
from models import Game, Player



def lock_all_buttons(buttons):
    for row in buttons:
        for button in row:
            button.configure(state='disabled')


def unlock_buttons(buttons):
    for row in buttons:
        for button in row:
            button.config(state='normal')


def make_and_get_object(root, object):
#make label and entry in a frame and pack it in root
    frame = tk.Frame(master=root)
    label = tk.Label(master=frame, text=f'Enter {object}:')
    label.grid(row=0, column=0)
    entry = tk.Entry(master=frame, textvariable=f'{object}')
    entry.grid(row=0, column=1)
    frame.pack()
    return entry


def clicked(but, pos, game, buttons, label):
    game.elements[int(pos[0])][int(pos[1])] = game.check_turn().name
    game.next_turn()
    label.config(text=f'{game.check_turn().name} turn:')
    buttons[int(pos[0])][int(pos[1])].configure(text=game.elements[int(pos[0])][int(pos[1])], state='disabled')
    if game.win_check(pos) == True:
        label.config(text=f'{game.elements[int(pos[0])][int(pos[1])]} won')
        lock_all_buttons(buttons)
        but.grid(row=0,column=1)


def reset_game(game, buttons, label):
    game.elements = game.create_elements(game.demension,game.demension)
    for i in range(len(game.elements)):
        for j in range(len(game.elements[i])):
            buttons[i][j]['text'] = game.elements[i][j]
    label.config(text=f'{game.check_turn().name} turn:')
    unlock_buttons(buttons)


def create_game_start(root, demension, win_on, player_count):
    #create and start game
    buttons = []
    game = Game(demension, win_on, player_count)
    elements = game.elements
    game.add_players()
    game.players[0].status = True
    top = tk.Toplevel(root)
    top.title(f'TicTacToe - game{game.id}')
    frame = tk.Frame(top)
    label = tk.Label(frame, text=f'{game.check_turn().name} turn:')
    but = tk.Button(frame, text='reset game', command=lambda: reset_game(game, buttons, label))
    label.grid(row=0, column=0)
    but.grid_forget()
    frame.pack()
    frame = tk.Frame(top)
    for i in range(len(elements)):
        buttons.append([])
        for j in range(len(elements[i])):
            button = tk.Button(frame, relief = tk.RAISED, borderwidth=5, text=f'{elements[i][j]}')
            button.config(command=lambda current_pos=f'{i}{j}': clicked(but, current_pos, game, buttons,label))
            button.grid(row=i,column=j)
            buttons[i].append(button)
    frame.pack()
    top.mainloop()


def main():
    #main window
    root = tk.Tk()
    root.title('Tic Tac Toe')
    demension = make_and_get_object(root, 'demension')
    win_on = make_and_get_object(root, 'win on')
    player_count = make_and_get_object(root, 'player count')
    frame = tk.Frame(master=root)
    frame.pack()
    button = tk.Button(master=frame, command=lambda: create_game_start(root,int(demension.get()),int(win_on.get()),int(player_count.get())), text='start')
    button.pack(side=tk.LEFT)
    root.mainloop()




main()
