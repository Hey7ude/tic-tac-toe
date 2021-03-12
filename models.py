

def create_id(model):

    flag = 0

    if len(model.objects) == 0:
        return 0
    
    for i in range(len(model.objects)):
        for obj in model.objects:
            if obj.id == i:
                flag = 1
                break
        if flag == 0:
            return i
        if i+1 == len(model.objects):
            return i+1


class Player:

    objects = []

    def __init__(self, name):
        self.id = create_id(Player)
        self.name = name
        self.score = 0
        self.objects.append(self)
        self.status = False
    

    def add_score(self):
        self.score += 1

    
    def disable(self):
        self.status = False


    def enable(self):
        self.status = True


    def __str__(self):
        return self.name


class Game:

    objects = []

    def __init__(self, demension, win_on, player_count):
        self.id = create_id(Game)
        self.demension = demension
        self.win_on = win_on
        self.player_count = player_count
        self.players = []
        self.elements = self.create_elements(demension, demension)
        self.objects.append(self)
        self.win_pattern = self.get_win_pattern()


    def __str__(self):
        return f'demension:{self.demension}*{self.demension}, win on:{self.win_on}, player count:{self.player_count}'

    def create_elements(self, row, column):
        a = []
        for i in range(row):
            a.append([])
            for j in range(column):
                a[i].append('')
        return a


    def add_players(self):
    #add players to game by player_count automaticly
        for i in range(self.player_count):
            player = Player(f'player{i+1}')
            self.add_player(player)
            if len(self.players) == self.player_count:
                return
        


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
        win_patt = self.win_pattern
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

    
    def check_turn(self):
        for player in self.players:
            if player.status == True:
                return player


    def next_turn(self):
        for i in range(len(self.players)):
            if self.players[i].status == True:
                self.players[i].status = False
                if i == len(self.players)-1:
                    self.players[0].status = True
                else:
                    self.players[i+1].status = True
                return self.players[i]


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
            self.show_board()
            given_position = input(f'{self.players[flag]} turn:')
            self.elements[int(given_position[0])][int(given_position[1])] = self.players[flag].name
            if self.win_check(given_position):
                self.show_board()
                print((f'{self.elements[int(given_position[0])][int(given_position[1])]} won'))
                return self.players[flag]
            flag += 1
            if flag == self.player_count:
                flag = 0
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
