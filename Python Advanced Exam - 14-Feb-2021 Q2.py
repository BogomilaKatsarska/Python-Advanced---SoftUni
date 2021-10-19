import math
rows = int(input())
matrix = []
player_coor = []
move_coor = []
coins = 0
path = []
moves = {}

end_flag = False
# moves = {"right" : [player_coor[0],player_coor[1]+1], "left": [player_coor[0], player_coor[1] - 1], "up": [player_coor[0] - 1, player_coor[1]], "down": [player_coor[0] + 1, player_coor[1]]}
for row in range(rows):
    matrix.append([])
    matrix[row] = input().split(" ")

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "P":
            matrix[row][col] = "0"
            player_coor.append(row)
            player_coor.append(col)
            break

command = input()
while not coins == 100:
    moves.clear()
    moves = {"right": [player_coor[0], player_coor[1] + 1], "left": [player_coor[0], player_coor[1] - 1],
             "up": [player_coor[0] - 1, player_coor[1]], "down": [player_coor[0] + 1, player_coor[1]]}

    move_coor.clear()
    move_coor = moves[command]
    if not 0 <= move_coor[0] < rows or not 0 <= move_coor[1] < rows:
        coins = math.floor(coins / 2)
        end_flag = True
        break
    elif matrix[move_coor[0]][move_coor[1]] == "X":
        end_flag = True
        coins = math.floor(coins / 2)
        break
    if matrix[move_coor[0]][move_coor[1]].isdigit():
        # coins += int(matrix[move_coor[0]][move_coor[1]])
        # matrix[player_coor[0]][player_coor[1]] = 0
        # path.append([move_coor[0], move_coor[1]])
        # matrix[move_coor[0]][move_coor[1]] = "P"
        # player_coor.clear()
        # player_coor.append(move_coor[0])
        # player_coor.append(move_coor[1])

        coins += int(matrix[move_coor[0]][move_coor[1]])
        path.append([move_coor[0], move_coor[1]])
        # matrix[move_coor[0]][move_coor[1]] = "P"
        player_coor.clear()
        player_coor.append(move_coor[0])
        player_coor.append(move_coor[1])

    if coins >= 100:
        break

    command = input()

if not end_flag:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")

for el in path:
    print(f"[{el[0]}, {el[1]}]")