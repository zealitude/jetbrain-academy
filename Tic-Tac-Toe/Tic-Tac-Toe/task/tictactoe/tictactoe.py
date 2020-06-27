import string
game_matrix = [
    ['_', '_' , '_'],
    ['_', '_' , '_'],
    ['_', '_' , '_'],
]

step = 0

def print_game_matrix():
    print("---------")
    print("|", *game_matrix[0], "|")
    print("|", *game_matrix[1], "|")
    print("|", *game_matrix[2], "|")
    print("---------")

def count_X_O():
    count_X = 0
    count_O = 0

    for index in range(3):
        row = game_matrix[index]
        for index2 in range(3):
            if row[index2] == 'X':
                count_X += 1
            elif row[index2] == 'O':
                count_O += 1
    return count_X, count_O

def check_result():
    check_row = []
    check_col = []

    for index in range(3):
        row = game_matrix[index]
        if row[0] != '_' and row[0] == row[1] and row[1] == row[2]:
            check_row.append(row[0])

        col = [game_matrix[0][index], game_matrix[1][index], game_matrix[2][index]]
        if col[0] != '_' and col[0] == col[1] and col[1] == col[2]:
            check_col.append(col[0])

    # print(check_row)
    # print(check_col)
    # count_X, count_O = count_X_O()
    # if abs(count_O - count_X) > 1:
    #     print("Impossible")
    # elif 'X' in check_row and 'O' in check_row:
    #     print("Impossible")
    # elif 'X' in check_col and 'O' in check_col:
    #     print("Impossible")
    if 'X' in check_row or 'O' in check_row:
        print(f'{check_row[0]} wins')
        return True
    elif 'X' in check_col or 'O' in check_col:
        print(f'{check_col[0]} wins')
        return True
    elif game_matrix[0][0] != '_' and game_matrix[0][0] == game_matrix[1][1] and game_matrix[1][1] == game_matrix[2][2]:
        print(f'{game_matrix[0][0]} wins')
        return True
    elif game_matrix[2][0] != '_' and game_matrix[2][0] == game_matrix[1][1] and game_matrix[1][1] == game_matrix[0][2]:
        print(f'{game_matrix[2][0]} wins')
        return True
    elif step == 9:
        print("Draw")
        return True

    return False

def update_matrix():
    global game_matrix

    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)
    while True:
        x, y = input("Enter the coordinates:").split()
        if x not in string.digits or y not in string.digits:
            print("You should enter numbers!")
            continue

        colIdx, rowIdx = int(x) - 1, 3 - int(y)
        if not (colIdx >= 0 and colIdx < 3 and rowIdx >= 0 and rowIdx < 3):
            print("Coordinates should be from 1 to 3!")
            continue

        if game_matrix[rowIdx][colIdx] == '_':
            game_matrix[rowIdx][colIdx] = 'X' if step % 2  == 0 else 'O'
            break
        else:
            print("This cell is occupied! Choose another one!")

print_game_matrix()

is_win = False
while step < 9 and not is_win:
    update_matrix()
    step += 1
    print_game_matrix()
    is_win = check_result()
