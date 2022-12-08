directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def part_one(board):
    result = 0
    rows = len(board)
    column = len(board[0])

    def invisible(i, j):
        for direction_row, direction_column in directions:
            inner_row, inner_column = i+direction_row, j+direction_column

            while 0 <= inner_row < rows and 0 <= inner_column < column and board[inner_row][inner_column] < board[i][j]:
                inner_row += direction_row
                inner_column += direction_column

            if not (0 <= inner_row < rows and 0 <= inner_column < column):
                return True

        return False

    for i in range(rows):
        for j in range(column):
            if invisible(i, j):
                result += 1

    return result


def part_two(board):
    result = 0
    rows = len(board)
    column = len(board[0])

    def getScore(i, j):
        string = 1
        for direction_row, direction_column in directions:
            current = 0
            inner_row, inner_column = i+direction_row, j+direction_column

            while 0 <= inner_row < rows and 0 <= inner_column < column:
                current += 1
                if board[inner_row][inner_column] >= board[i][j]:
                    break

                inner_row += direction_row
                inner_column += direction_column

            string *= current

        return string

    for i in range(rows):
        for j in range(column):
            result = max(result, getScore(i, j))

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        board = []
        for row in f.readlines():
            board.append(list(map(int, row.strip())))

    print(part_one(board))
    print(part_two(board))