from models import Player, Game




game1 = Game(3,3,2)
player1 = Player('red', 0)
game1.add_player(player1)
player2 = Player('blue', 1)
game1.add_player(player2)
game1.start_game()
