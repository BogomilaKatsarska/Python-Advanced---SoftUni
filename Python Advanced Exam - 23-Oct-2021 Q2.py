def fill_matrix(n):
    matrix_filled = []
    for _ in range(n):
        matrix_filled.append([x for x in input().split()])
    return matrix_filled


def find_bucket(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "B":
                return r, c


def is_valid_movement(r, c, field):
    if 0 <= r < len(field) and 0 <= c < len(field):
        return True
    return False


matrix = fill_matrix(6)
scored_points = 0

for _ in range(3):
    data = input()
    data_to_unpack = data[1:-1]
    row, col = int(data_to_unpack.split(", ")[0]), int(data_to_unpack.split(", ")[1])

    if is_valid_movement(row, col, matrix):
        value = matrix[row][col]
        if value == "B":
            matrix[row][col] = '0'

            for r in range(len(matrix)):
                points = matrix[r][col]
                if points.isdigit():
                    scored_points += int(points)

if scored_points < 100:
    print(f"Sorry! You need {(100 - scored_points)} points more to win a prize.")
else:
    if 100 <= scored_points <= 199:
        print(f"Good job! You scored {scored_points} points, and you've won Football.")
    elif 200 <= scored_points <= 299:
        print(f"Good job! You scored {scored_points} points, and you've won Teddy Bear.")
    else:
        print(f"Good job! You scored {scored_points} points, and you've won Lego Construction Set.")