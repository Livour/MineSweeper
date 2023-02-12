from random import randint as rng

from Cell import Cell


def generate_field(rows, columns, num_of_mines):
    matrix = [[0 for j in range(columns)] for i in range(rows)]
    for mine in range(num_of_mines):
        # could already have a mine
        i, j = random_point(rows, columns)
        matrix[i][j] = -1

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == -1:
                continue
            matrix[i][j] = count_adjacent_mines(i, j, rows, columns, matrix)

    return matrix


def random_point(rows, columns):
    return rng(0, rows - 1), rng(0, columns - 1)


def count_adjacent_mines(i, j, rows, columns, grid):
    adjacent = [(i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1),
                (i - 1, j - 1)]
    counter = 0

    for i, j in adjacent:
        if is_valid(i, j, rows, columns) and grid[i][j] == -1:
            counter += 1

    return counter


def is_valid(i, j, rows, columns):
    return 0 <= i < rows and 0 <= j < columns


class Field:
    NUM_OF_MINES = 550

    def __init__(self, canvas, rows, columns, cell_size):
        logic_matrix = generate_field(rows, columns, self.NUM_OF_MINES)
        self.matrix = []
        for i in range(rows):
            self.matrix.append([])
            for j in range(columns):
                current_logic = logic_matrix[i][j]
                value_to_assign = "🔥" if current_logic == -1 else current_logic
                cell = Cell(canvas, i, j, cell_size, value_to_assign)
                self.matrix[i].append(cell)
