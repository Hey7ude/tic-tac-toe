


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

    def __str__(self):
        return f'demension:{self.demension}*{self.demension}, win on:{self.win_on}, player count:{self.player_count}'
    
    def add_player(self, player):
        self.players.append(player)
    def get_players(self):
        return self.players
        




game1 = Game(3,3,2)
player1 = Player('red', 0)
print(game1)
game1.add_player(player1)
player2 = Player('blue', 1)
game1.add_player(player2)

for player in game1.get_players():
    print(player)