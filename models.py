
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