n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split()])

result = 0
for row in range(n):
    for col in range(n):
        if row == col:
            result += matrix[row][col]

print(result)