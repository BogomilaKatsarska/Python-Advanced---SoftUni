class Player:
    def __init__(self, name: str, flag: bool):
        self.name = name
        self.score = 501
        self.throws = 0
        self.flag = flag

    def throw(self, matrix , *args):
        row, col = args
        row = int(row)
        col = int(col)
        self.throws += 1
        if 0 <= row < 7 and 0 <= col < 7:
            el = matrix[row][col]
            if el == "B":
                print(f"{self.name} won the game with {self.throws} throws!")
                exit(0)
            elif el == "D":
                sum = (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])) * 2
                self.score -= sum
            elif el == "T":
                sum = (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])) * 3
                self.score -= sum
            else:
                self.score -= int(el)

        if self.score <= 0:
            print(f"{self.name} won the game with {self.throws} throws!")
            exit(0)


names = input().split(", ")
player1 = Player(names[0], True)
player2 = Player(names[1], False)
matrix = []
for row in range(7):
    matrix.append(input().split())
while True:
    coor = input().lstrip("(").rstrip(")").split(", ")
    if player1.flag:
        player1.throw(matrix, coor[0], coor[1])
        player1.flag = False
        player2.flag = True
    else:
        player2.throw(matrix, coor[0], coor[1])
        player2.flag = False
        player1.flag = True