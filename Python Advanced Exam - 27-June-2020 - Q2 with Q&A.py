def is_valid(r, c, field): #защо на is_valid аргументите са 3, а на find_snake - 1, при условие, че и в 2та случая обхождаме матрицата? -
    #Защото тук имаме if, и то изисква предварително да сме подали r,c в аргументите
    if r not in range(len(field)) or c not in range(len(field[r])):
        return False
    return True #Защо ни е това return True? => все 1: else: // return True


def find_snake(field):
    for r in range(len(field)): #локална променлива(създава се само за текущия scope/част от програмата; в случая - for цикъла) за for цикъл
        for c in range(len(field[r])):
            if field[r][c] == "S":
                return r,c #Тук защо не слагаме Return True/False, като горе? - Иначе получаваме None, но в задачата се приема, че "S" ще е на валидна позиция в матрицата
    #return -1,-1 (invalid values) - иначе можем да го напишем така и после долу да опишем, че в този случай трябва да даде output "Invalid input"

def find_burrow(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "B":
                return r, c


def possible_moves(r, c, direction, field):
    if direction == "up":
        return r-1, c
    if direction == "down":
        return r+1, c
    if direction == "left":
        return r, c-1
    if direction == "right":
        return r, c+1


territory = [list(input()) for _ in range(int(input()))] #Защо е int(input(), като можем да имаме и букви - "S", "B"? # The next n lines holds the values for every row.
snake_row, snake_col = find_snake(territory)

eaten_food = 0
won = True
while eaten_food < 10:
    command = input()
    territory[snake_row][snake_col] = "."
    snake_row, snake_col = possible_moves(snake_row, snake_col, command, territory)
    if not is_valid(snake_row,snake_col,territory):
        print("Game over!")
        print(f"Food eaten: {eaten_food}")
        print('\n'.join([''.join(territory[r]) for r in range(len(territory))])) #Какво е "\n"? - форматиране на нов ред
        won = False
        break
    if territory[snake_row][snake_col] == "*":
        eaten_food +=1
    elif territory[snake_row][snake_col] == ".":
        snake_row, snake_col = find_burrow(territory)
    territory[snake_row][snake_col] = find_burrow(territory)

if won:
    print("You won! You fed the snake.")
    print(f"Food eaten: {eaten_food}")
    print('\n'.join([''.join(territory[r]) for r in range(len(territory))]))