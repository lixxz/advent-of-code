puzzle_input = [0,13,16,17,1,10,6]
game_setup = {k: v + 1 for k,v in zip(puzzle_input, range(len(puzzle_input)))}

turn = len(game_setup.keys()) + 2
last_spoken = 0

for t in range(turn, 30000001):
    if last_spoken in game_setup:
        temp = (t - 1) - game_setup[last_spoken]
        game_setup[last_spoken] = t - 1
        last_spoken = temp
    
    elif last_spoken not in game_setup:
        game_setup[last_spoken] = t - 1
        last_spoken = 0

print(last_spoken)