from models import Player, Game
from tk import main as start_gui



def input_to_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print('Incorrect command!!!')
            


while True:
    command = input_to_int('1-make a game\n2-make a game(gui)\nenter 0 for exit\n')
    if command == 0:
        break
    elif command == 1:
        demension = input_to_int('Enter demension:')
        win_on = input_to_int('Enter win on:')
        player_count = input_to_int('Enter number of players:')
        game = Game(demension, win_on, player_count)
        while True:
            command = input_to_int('1-start game\n2-add player\n3-add players automaticly\nenter 0 to go back\n')
            if command == 0:
                break
            elif command == 1:
                game.elements = game.create_elements(game.demension, game.demension)
                winner = game.start_game()
                if winner != None:
                    winner.add_score()
            elif command == 2:
                if len(game.players) == game.player_count:
                    print(f'You can add more than {game.player_count} players in this game.')
                else:
                    name = input('Enter name of player:\n')
                    player = Player(name)
                    game.add_player(player)
            elif command == 3:
                game.add_players()
            else:
                print('Incorrect command!!!')
    elif command == 2:
        start_gui()
    else:
        print('Incorrect command!!!')

