from Cell import Cell
from field_util import generate_field
from tkinter import Canvas, DISABLED

from zoom_util import reset_zoom


class Field:
    NUM_OF_MINES = 500

    def __init__(self, canvas: Canvas, rows, columns, cell_size):
        self.matrix = None
        self.canvas = canvas
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.new_game()

    def new_game(self):
        reset_zoom()
        self.canvas.delete("all")
        logic_matrix = generate_field(self.rows, self.columns, self.NUM_OF_MINES)
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.columns):
                current_logic = logic_matrix[i][j]
                value_to_assign = Cell.MINE if current_logic == -1 else current_logic
                cell = Cell(self.canvas, i, j, self.cell_size, value_to_assign, self, self.rows, self.columns)
                self.matrix[i].append(cell)

    def game_over(self):
        middle_x = self.canvas.winfo_width() / 2
        middle_y = self.canvas.winfo_height() / 3
        self.canvas.create_text(middle_x, middle_y, text="GAME OVER!", font=("Helvetica", 70), fill="red")
        self.canvas.create_text(middle_x, middle_y + middle_y / 2, text="PRESS ENTER TO RETRY", font=("Helvetica", 30),
                                fill="red")

        for item in self.canvas.find_all():
            self.canvas.itemconfigure(item, state=DISABLED)

        self.canvas.unbind_all("<Button-1>")
        self.canvas.unbind_all("<Button-3>")
