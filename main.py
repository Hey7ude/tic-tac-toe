from models import Player, Game



def input_to_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print('Incorrect command!!!')
            


while True:
    command = input_to_int('1-make a game\n2-show games\nenter 0 for exit\n')
    if command == 0:
        break
    if command == 1:
        demension = input_to_int('Enter demension:')
        win_on = input_to_int('Enter win on:')
        player_count = input_to_int('Enter number of players:')
        game = Game(demension, win_on, player_count)
        while True:
            command = input_to_int('1-start game\n2-add player\nenter 0 to go back\n')
            if command == 0:
                break
            if command == 1:
                game.start_game()
            if command == 2:
                name = input('Enter name of player:\n')
                player = Player(name)
                game.add_player(player)
            else:
                print('Incorrect command!!!')
    if command == 2:
        for game in Game.objects:
            print(game)
    else:
        print('Incorrect command!!!')

