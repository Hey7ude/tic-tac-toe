from models import Player, Game



games = []
while True:
    command = int(input('1-make a game\n2-add player\n3-show games\n'))
    if command == 1:
        demension = int(input('Enter demension:'))
        win_on = int(input('Enter win on:'))
        player_count = int(input('Enter number of players:'))
        game = Game(demension, win_on, player_count)
        game.make_id(games)
        games.append(game)
        while True:
            command = int(input('1-start game\n2-add player\n'))
            if command == 1:
                game.start_game()
            if command == 2:
                name = input('Enter name of player:\n')
                player = Player(name)
                game.add_player(player)
    if command == 3:
        for game in games:
            print(game)
    if command == 4:
        pass
