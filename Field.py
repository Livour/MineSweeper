from Cell import Cell
from field_util import generate_field


class Field:
    NUM_OF_MINES = 500

    def __init__(self, canvas, rows, columns, cell_size):
        logic_matrix = generate_field(rows, columns, self.NUM_OF_MINES)
        self.matrix = []
        for i in range(rows):
            self.matrix.append([])
            for j in range(columns):
                current_logic = logic_matrix[i][j]
                value_to_assign = "💣" if current_logic == -1 else current_logic
                cell = Cell(canvas, i, j, cell_size, value_to_assign, self, rows, columns)
                self.matrix[i].append(cell)
