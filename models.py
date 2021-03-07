
def create_elements(row, column):
    a = []
    for i in range(row):
        a.append([])
        for j in range(column):
            a[i].append(None)
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