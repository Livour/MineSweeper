from tkinter import Canvas
from tkinter.font import Font

from field_util import is_valid


class Cell:
    FLAG = "🏴"
    MINE = "X"

    def __init__(self, canvas: Canvas, row, column, cell_size, value, matrix, rows, columns):
        self.clicked = False
        self.is_flagged = False
        self.value = value
        self.canvas = canvas
        self.field = matrix
        self.rows = rows
        self.columns = columns
        self.checked = False
        x1 = column * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        self.rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        self.text = canvas.create_text(x1 + cell_size / 2, y1 + cell_size / 2, text='', fill='white',
                                       font=Font(None, f"Helvetica {cell_size - 2}"))
        left_click_handler = lambda event, i=row, j=column: self.on_click(event, i, j)
        right_click_handler = lambda event: self.on_right_click(event)

        canvas.tag_bind(self.rectangle, "<Button-3>", right_click_handler)
        canvas.tag_bind(self.text, "<Button-3>", right_click_handler)
        canvas.tag_bind(self.rectangle, "<Button-1>", left_click_handler)
        canvas.tag_bind(self.text, "<Button-1>", left_click_handler)

    def on_click(self, event, i, j):
        if self.clicked or self.is_flagged:
            return

        if self.value == 0:
            self.click_adjacent_zeros(i, j)
            return

        self.canvas_right_click()
        if self.value == self.MINE:
            self.field.game_over()

    def canvas_right_click(self):
        if self.is_flagged:
            return

        if self.value == self.MINE:
            self.canvas.itemconfigure(self.rectangle, fill="red")
            self.canvas.itemconfigure(self.text, fill="black", text=self.value)
        else:
            self.canvas.itemconfigure(self.rectangle, fill="grey")
            self.canvas.itemconfigure(self.text, fill="white", text="" if self.value == 0 else self.value)
        self.clicked = True

    def on_right_click(self, event):
        if self.clicked:
            return
        if self.is_flagged:
            self.is_flagged = False
            self.canvas.itemconfigure(self.text, fill="white", text=" ")
        else:
            self.is_flagged = True
            self.canvas.itemconfigure(self.text, fill="red", text=self.FLAG)

    def click_adjacent_zeros(self, i, j):
        adjacent = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1),
                    (i + 1, j - 1)]

        if self.checked:
            return

        self.canvas_right_click()
        self.checked = True

        # Recursively click adjacent zeroes until their values isn't 0
        if self.value != 0:
            return
        for neighbor_i, neighbor_j in adjacent:
            if is_valid(neighbor_i, neighbor_j, self.rows, self.columns):
                self.field.matrix[neighbor_i][neighbor_j].click_adjacent_zeros(neighbor_i, neighbor_j)
