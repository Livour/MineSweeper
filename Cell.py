from tkinter import Canvas


class Cell:
    FLAG = "🏴"

    def __init__(self, canvas: Canvas, row, column, cell_size, value):
        self.clicked = False
        self.is_flagged = False
        self.value = value
        self.canvas = canvas
        x1 = column * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        self.rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        self.text = canvas.create_text(x1 + cell_size / 2, y1 + cell_size / 2, text='', fill='white')
        canvas.tag_bind(self.rectangle, "<Button-3>", lambda event: self.on_right_click(event))
        canvas.tag_bind(self.text, "<Button-3>", lambda event: self.on_right_click(event))
        canvas.tag_bind(self.rectangle, "<Button-1>", lambda event: self.on_click(event))
        canvas.tag_bind(self.text, "<Button-1>", lambda event: self.on_click(event))

    def on_click(self, event):
        if self.clicked:
            return

        if self.value == "🔥":
            self.canvas.itemconfigure(self.rectangle, fill="red")
        else:
            self.canvas.itemconfigure(self.rectangle, fill="grey")
        self.canvas.itemconfigure(self.text, fill="white", text=self.value)
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
