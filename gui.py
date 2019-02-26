import csp as solver
from tkinter import *
import copy
import sys
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board
darktheme = {"3x3":"deep sky blue", "9x9":"steel blue", "solved":"gainsboro", "initial":"spring green"}
litetheme = {"3x3":"brown4", "9x9":"orange", "solved":"dark slate gray", "initial":"forest green"}
theme = {}
row = -1
col = -1
puzzle=[[0 for i in range(9)] for j in range(9)]
start_puzzle=copy.deepcopy(puzzle)
    
def draw_grid():
    for i in range(10):
        color = theme["3x3"] if i % 3 == 0 else theme["9x9"]
        x0 = MARGIN + i * SIDE
        y0 = MARGIN
        x1 = MARGIN + i * SIDE
        y1 = HEIGHT - MARGIN
        canvas.create_line(x0, y0, x1, y1, fill=color)

        x0 = MARGIN
        y0 = MARGIN + i * SIDE
        x1 = WIDTH - MARGIN
        y1 = MARGIN + i * SIDE
        canvas.create_line(x0, y0, x1, y1, fill=color)

def update_puzzle():
    canvas.delete("numbers")
    for i in range(9):
        for j in range(9):
            value = puzzle[i][j]
            if value != 0:
                x = MARGIN + j * SIDE + SIDE / 2
                y = MARGIN + i * SIDE + SIDE / 2
                original = start_puzzle[i][j]
                color = theme["solved"] if value != original else theme["initial"]
                canvas.create_text(x, y, font=("Helvetica", 16), text=value, tags="numbers", fill=color)

def draw_cursor():
    canvas.delete("cursor")
    if row >= 0 and col >= 0:
        x0 = MARGIN + col * SIDE + 1
        y0 = MARGIN + row * SIDE + 1
        x1 = MARGIN + (col + 1) * SIDE - 1
        y1 = MARGIN + (row + 1) * SIDE - 1
        canvas.create_rectangle(x0, y0, x1, y1, outline="red", tags="cursor")

def cell_clicked(event):
    global row
    global col
    x, y = event.x, event.y
    #print (x,y)
    if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
        canvas.focus_set()
        row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE
    draw_cursor()

def key_pressed(event):
    global row
    global col
    if row >= 0 and col >= 0 and event.char in "1234567890":
        puzzle[row][col] = int(event.char)
        col, row = -1, -1
        update_puzzle()
        draw_cursor()

def clear():
    global puzzle
    global start_puzzle
    puzzle=[[0 for i in range(9)] for j in range(9)]
    start_puzzle=[[0 for i in range(9)] for j in range(9)]
    canvas.delete("numbers")

def solve():
    global puzzle
    global start_puzzle
    start_puzzle=copy.deepcopy(puzzle)
    puzzle = solver.solveSudoku(puzzle)
    update_puzzle()

try:
    if(sys.argv[1]=='light'):
        theme = litetheme
    else:
        theme = darktheme
except:
    theme = darktheme
root = Tk()
root.title("Sudoku")
#root.configure(background = theme["background"])
#Frame.init(root)
row, col = -1, -1
#root.pack(fill=BOTH)
canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas.pack(fill=BOTH, side=TOP)
clear_button = Button(text="Clear", command=clear)
clear_button.pack(fill=BOTH, side=BOTTOM)
clear_button = Button(text="Solve", command=solve)
clear_button.pack(fill=BOTH, side=BOTTOM)
draw_grid()
update_puzzle()

canvas.bind("<Button-1>", cell_clicked)
canvas.bind("<Key>", key_pressed)

root.geometry("%dx%d" % (WIDTH, HEIGHT + 100))
root.mainloop()
