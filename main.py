
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
        


def start_game_commandline(game1):
    print('----------')
    for row in range(game1.demension):
        test = '| '
        for col in range(game1.demension):
            test = test + f'{game1.elements[row][col]} | '
        print(test)
        print('----------')




def start_game_gui(game1):
    import tkinter as tk


    window = tk.Tk()
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(master=window, relief = tk.RAISED, borderwidth=5)
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f'{game1.elements[i][j]}')
            label.pack()
    window.mainloop()



game1 = Game(3,3,2)
player1 = Player('red', 0)
game1.add_player(player1)
player2 = Player('blue', 1)
game1.add_player(player2)
start_game_commandline(game1)
start_game_gui(game1)


