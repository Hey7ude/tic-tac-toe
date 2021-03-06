
def create_elements(row, column):
    a = []
    for i in range(row):
        a.append([])
        for j in range(column):
            a[i].append('')
    return a


class Player:
    def __init__(self, color, id):
        self.id = id
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return str(self.id)    

class Game:
    def __init__(self, demension, win_on, player_count):
        self.demension = demension
        self.win_on = win_on
        self.player_count = player_count
        self.players = []
        self.elements = create_elements(demension, demension)

    def __str__(self):
        return f'demension:{self.demension}*{self.demension}, win on:{self.win_on}, player count:{self.player_count}'
    
    def add_player(self, player):
        self.players.append(player)
    def get_players(self):
        return self.players
        

def win_pattern(demension=int, win_on=int):
    a = []
    for i in range(demension):
        for j in range(demension):
            if i+win_on <= demension:
                b = []
                for k in range(win_on):
                    b.append(f'{i+k}*{j}')
                a.append(b)
            if j+win_on <= demension:
                b = []
                for k in range(win_on):
                    b.append(f'{i}*{j+k}')
                a.append(b)
            if i+win_on <= demension:
                if j+win_on <= demension:
                    b = []
                    for k in range(win_on):
                        b.append(f'{i+k}*{j+k}')                
                    a.append(b)
                if j+1-win_on >=0:
                    b = []
                    for k in range(win_on):
                        b.append(f'{i+k}*{j-k}')
                    a.append(b)
    return a    


def start_game_commandline(game):
    elements = game.elements
    # elements = [['o', 'x', 'x'], ['o', 'x', 'o'], ['x', 'x', 'x']]
    win_pattern = []



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

    for i in range(3):
        if elements[i][0] == elements[i][1] and elements[i][0] == elements[i][2]:
            print(f'{elements[i][0]} won')
        if elements[0][i] == elements[1][i] and elements[0][i] == elements[2][i]:
                print(f'{elements[0][i]} won')
    if elements[0][0] == elements[1][1] and elements[0][0] == [elements][2][2]:
        print(f'{elements[0][0]} won')
    if elements[0][2] == elements[1][1] and elements[1][1] == elements[2][0]:
        print(f'{elements[1][1]} won')
            




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

