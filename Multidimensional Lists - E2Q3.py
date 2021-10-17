def is_valid_position_and_is_a_knight(chess_board, r, c):
    chess_board_size = len(chess_board)
    if r < 0 or c < 0 or r >= chess_board_size or c >= chess_board_size:
        return False
    return chess_board[r][c] == 'K'


def count_attacked_knights(chess_board, r, c):
    result = 0
    if is_valid_position_and_is_a_knight(chess_board, r - 2, c - 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r - 2, c + 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 2, c - 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 2, c + 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r - 1, c - 2):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r - 1, c + 2):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 1, c - 2):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 1, c + 2):
        result += 1
    return result


board_size = int(input())

matrix = []

for _ in range(board_size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    max_count, knight_row, knight_col = 0, 0, 0

    for r in range(board_size):
        for c in range(board_size):
            if matrix[r][c] == '0':
                continue
            count = count_attacked_knights(matrix, r, c)
            if count > max_count:
                max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)