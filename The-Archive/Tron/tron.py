from random import randrange
from time import time

def sand(bLST):
    for b in bLST:
        if not b: return False
    return True

def get_move_from(player):
    return

def make_grid():
    arr = []
    for i in range(20):
        arr.append([])
        for j in range(30):
            arr[i].append(0)
    return arr

def init_locations(number_of_players, grid):
    arr = []
    Ys = list(range(20))
    Xs = list(range(30))
    for i in range(number_of_players):
        ry = Ys[randrange(len(Ys))]
        rx = Xs[randrange(len(Xs))]
        grid[ry][rx] = i + 1
        arr.append([rx,ry])
        del(Ys[ry])
        del(Xs[rx])
    return arr

def clear_player(grid, player, player_locations,active_player_list):
    for i in range(20):
        for j in range(30):
            if grid[i][j] == player+1:
                grid[i][j] == 0
    player_locations[player] = [-1,-1]
    del(active_player_list[active_player_list.index(player)])
    return

def update_grid(grid, player, player_locations, active_player_list, move):
    x = player_locations[player][0]
    y = player_locations[player][1]
    x_move = 0
    y_move = 0
    if move == "LEFT":
        x_move = -1
    elif move == "RIGHT":
        x_move = 1
    elif move == "UP":
        y_move = -1
    elif move == "DOWN":
        y_move = 1
    else:
        clear_player(grid,player,player_locations,active_player_list)
        return

    if sand([x+x_move >= 0, x+x_move < 30, y+y_move >= 0, y+y_move < 20]):
        if grid[y+y_move][x+x_move] != 0:
            clear_player(grid,player,player_locations,active_player_list)
        else:
            grid[y+y_move][x+x_move] = player+1
            player_locations[player] = [x+x_move,y+y_move]
    else:
        clear_player(grid,player,player_locations,active_player_list)
    return
#update_grid(grid,1,player_locations,active_player_list,'RIGHT')
#prnt_grid(grid,player_locations,active_player_list,player_symbols)
def prnt_grid(grid, player_locations, active_player_list, player_symbols):
    gTop = list(range(10)) + list(map(lambda x: chr(x+65),list(range(20))))
    print("  ", end="")
    for i in range(len(gTop)):
        print(gTop[i], end="")
    print()
    for i in range(len(grid)):
        print(gTop[i], end=" ")
        for j in range(len(grid[i])):
            press = grid[i][j]
            for player in active_player_list:
                if [j,i] == player_locations[player]:
                    press = player_symbols[player]
            print(press,end="")
        print()
    return

number_of_players = randrange(2,5)
active_player_list = list(range(number_of_players))

grid = make_grid()
player_locations = init_locations(number_of_players, grid)

number_of_active_players = len(active_player_list)
player_symbols = ['A','B','C','D'][:number_of_active_players]

while number_of_active_players > 1:
    break
    for player in active_player_list:
        update_grid(grid, player, player_locations, active_player_list,
                    get_move_from_(player, grid, player_locations))
        
    number_of_active_players = len(active_player_list)
