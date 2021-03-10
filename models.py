

class Player:
    total = 0
    
    def __init__(self, name):
        self.name = name
        Player.total += 1


    def __str__(self):
        return self.name


class Game:
    objects = []
    def __init__(self, demension, win_on, player_count):
        self.id = self.create_id()
        self.demension = demension
        self.win_on = win_on
        self.player_count = player_count
        self.players = []
        self.elements = self.create_elements(demension, demension)
        self.objects.append(self)


    def __str__(self):
        return f'demension:{self.demension}*{self.demension}, win on:{self.win_on}, player count:{self.player_count}'

    def create_elements(self, row, column):
        a = []
        for i in range(row):
            a.append([])
            for j in range(column):
                a[i].append(None)
        return a


    def create_id(self):
        flag = 0
        if len(Game.objects) == 0:
            return 0
        
        for i in range(len(Game.objects)):
            for game in Game.objects:
                if game.id == i:
                    flag = 1
                    break
            if flag == 0:
                return i
            if i+1 == len(Game.objects):
                return i+1
        


    def add_player(self, player):
        self.players.append(player)
        


    def get_win_pattern(self):
        pattern_list = []
        for i in range(self.demension):
            for j in range(self.demension):
                if i+self.win_on <= self.demension:
                    b = []
                    for k in range(self.win_on):
                        b.append((f'{i+k}{j}'))
                    pattern_list.append(b)
                if j+self.win_on <= self.demension:
                    b = []
                    for k in range(self.win_on):
                        b.append((f'{i}{j+k}'))
                    pattern_list.append(b)
                if i+self.win_on <= self.demension:
                    if j+self.win_on <= self.demension:
                        b = []
                        for k in range(self.win_on):
                            b.append((f'{i+k}{j+k}'))                
                        pattern_list.append(b)
                    if j+1-self.win_on >=0:
                        b = []
                        for k in range(self.win_on):
                            b.append((f'{i+k}{j-k}'))
                        pattern_list.append(b)
        return pattern_list   


    def win_check(self, current_pos):
        win_patt = self.get_win_pattern()
        for pattern in range(len(win_patt)):
            if current_pos in win_patt[pattern]:
                for item in range(len(win_patt[pattern])):
                    b = str(win_patt[pattern][item])
                    if self.elements[int(current_pos[0])][int(current_pos[1])] != self.elements[int(b[0])][int(b[1])]:
                        flag = 0
                        break
                    flag = 1
                if flag == 1:
                    return True
        return False


    def show_board(self):
        print('--------------------')
        for row in range(self.demension):
            a = '|'
            for column in range(self.demension):
                a = a + f' {self.elements[row][column]} |'
            print(a)
            print('--------------------')


    def start_game(self):
        if len(self.players) != self.player_count:
            return print('not enough players')
        flag = 0
        for turn in range(self.demension * self.demension):
            print(f'{self.players[0]}: x     {self.players[1]}: o')
            self.show_board()
            given_position = input(f'{self.players[flag]} turn:')
            self.elements[int(given_position[0])][int(given_position[1])] = flag
            flag += 1
            if flag == self.player_count:
                flag = 0
            if self.win_check(given_position):
                self.show_board()
                return print((f'{self.elements[int(given_position[0])][int(given_position[1])]} won'))
        return print('Tie!')

        
    def start_game_gui(self):
        import tkinter as tk

        window = tk.Tk()
        for i in range(self.demension):
            for j in range(self.demension):
                frame = tk.Frame(master=window, relief = tk.RAISED, borderwidth=5)
                frame.grid(row=i, column=j)
                label = tk.Label(master=frame, text=f'{self.elements[i][j]}')
                label.pack()
        window.mainloop()
