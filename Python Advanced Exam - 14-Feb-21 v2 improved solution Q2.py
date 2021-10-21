import math


def player_location(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "P":
                return r, c


def player_movement(r, c, command):
    if command == "up":
        return r-1, c
    elif command == "down":
        return r+1, c
    elif command == "left":
        return r, c-1
    elif command == "right":
        return r, c+1
    else:
        return None


def fill_matrix(n):
    matrix_filled = []
    for _ in range(n):
        matrix_filled.append([x for x in input().split()])
    return matrix_filled


def is_valid_movement(r, c, field):
    if 0 <= r < len(field) and 0 <= c < len(field):
        return True
    return False


matrix_size = int(input())
coins_collected = 0
path = []
matrix = fill_matrix(matrix_size)

player_row, player_col = player_location(matrix)
win = True
while coins_collected < 100:
    current_command = input()
    new_row, new_col = player_movement(player_row, player_col, current_command)

    if new_row is None and new_col is None:
        continue

    if is_valid_movement(new_row, new_col, matrix):
        coins = matrix[new_row][new_col]
        if not coins == "X":
            coins_collected += int(coins)
            a = [new_row, new_col]
            path.append(a)
            player_row, player_col = new_row, new_col
        else:
            win = False
            break
    else:
        win = False
        break

if win:
    print(f"You won! You've collected {coins_collected} coins.")
else:
    coins_collected = math.floor(coins_collected / 2)
    print(f"Game over! You've collected {coins_collected} coins.")

print(f"Your path:")

while path:
    b = path.pop(0)
    print(b)
