def is_invalid_position(size, row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False

END_COMMAND = 'END'

size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == END_COMMAND:
        break

    data = line.split()
    command = data[0]
    row, col, value = [int(x) for x in data[1:]]
    if is_invalid_position(size, row, col):
        print("Invalid coordinates")
        continue
    if command == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for elements in matrix:
    print(" ".join([str(el) for el in elements]))