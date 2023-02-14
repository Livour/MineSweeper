from tkinter import Canvas

ZOOM_IN_AMOUNT = 1.10
ZOOM_OUT_AMOUNT = 0.90
MIN_ZOOM = 0.8
MAX_ZOOM = 5.0
current_zoom = 1.0


def zoom_out(event, canvas: Canvas):
    global current_zoom
    if current_zoom * ZOOM_OUT_AMOUNT > MIN_ZOOM:
        current_zoom *= ZOOM_OUT_AMOUNT
        canvas.scale("all", event.x, event.y, ZOOM_OUT_AMOUNT, ZOOM_OUT_AMOUNT)


def zoom_in(event, canvas):
    global current_zoom
    if current_zoom * ZOOM_IN_AMOUNT < MAX_ZOOM:
        current_zoom *= ZOOM_IN_AMOUNT
        canvas.scale("all", event.x, event.y, ZOOM_IN_AMOUNT, ZOOM_IN_AMOUNT)


def reset_zoom():
    global current_zoom
    current_zoom = 1.0


def zoom(event, canvas):
    if event.delta > 0:
        zoom_in(event, canvas)
    elif event.delta < 0:
        zoom_out(event, canvas)
