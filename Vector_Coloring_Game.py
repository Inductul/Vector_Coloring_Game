import tkinter as tk

## ---Global Variables---

adjacency_matrix_0 = ([0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                      [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                      [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                      [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                      [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                      [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 1, 1, 0, 0])

adjacency_matrix_1=([0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                    [1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0])

adjacency_matrix_2 = ([0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                      [1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                      [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                      [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                      [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                      [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                      [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
                      [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
                      [0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

adjacency_matrix_3=([0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                    [1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0])

level_lst = (adjacency_matrix_0, adjacency_matrix_1,adjacency_matrix_2,adjacency_matrix_3)

level = 0

vertices = ['vertex_0', 'vertex_1', 'vertex_2', 'vertex_3', 'vertex_4', 'vertex_5', 'vertex_6', 'vertex_7', 'vertex_8', 'vertex_9']

vertex_cords = ([750, 50], [1083, 292], [956, 683], [544, 683], [417, 292],
                [750, 225], [916, 346], [853, 542], [647, 542], [584, 346])

vertex_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', ]

color = 'black'


## ---Functions---

def color_buttons():
    red_btn = tk.Button(root, text="", bg='red', fg='red', height=4, width=8, command=lambda: set_color('red'))
    red_btn.place(x=4, y=200)

    blue_btn = tk.Button(root, text="", bg='blue', fg='blue', height=4, width=8, command=lambda: set_color('blue'))
    blue_btn.place(x=4, y=300)

    green_btn = tk.Button(root, text="", bg='green', fg='green', height=4, width=8, command=lambda: set_color('green'))
    green_btn.place(x=4, y=500)

    yellow_btn = tk.Button(root, text="", bg='#FFFC5A', fg='#FFFC5A', height=4, width=8,command=lambda: set_color('#FFFC5A'))
    yellow_btn.place(x=4, y=400)
    return


# Sets what color you can change the vertices to.
def set_color(clr):
    global color
    color = clr
    return


# Changes the vertex to the set color.
def vertex_button_function(index):
    vertices[index].configure(bg=color)
    return


# Draws lines between vertices based on the adjacency_matrix and vertex_cords.
def draw_edges():
    for i in range(len(level_lst[level])):
        for j in range(len(level_lst[level][i])):

            if level_lst[level][i][j] == 1:
                canvas.create_line(vertex_cords[i][0], vertex_cords[i][1],
                                   vertex_cords[j][0], vertex_cords[j][1], width=3)

    return


def reset_button():
    reset = tk.Button(root, bg='grey', height=2, width=6, text="RESET", command=lambda: reset_borad())
    reset.place(x=1400, y=675, anchor='center')
    return


# Changes all vertices to black then clears and redraws canvas.
def reset_borad():
    for i in range(len(vertices)):
        vertices[i].configure(bg='black')
    canvas.delete("all")
    draw_edges()
    directions()
    return


def check_graph_button():
    check = tk.Button(root, bg='grey', height=2, width=6, text="CHECK", command=lambda: check_graph())
    check.place(x=1400, y=600, anchor='center')
    return


# Checks if graph is colored correct and displays result
def check_graph():
    win = True

    for i in range(len(level_lst[level])):
        for j in range(len(level_lst[level][i])):
            if level_lst[level][i][j] == 1:
                if vertices[i].cget('bg') == 'black' or vertices[j].cget('bg') == 'black':
                    canvas.delete("all")
                    draw_edges()
                    directions()
                    canvas.create_text(750, 400, font="Times 15", text="Incomplete", fill='grey')
                    return
                if vertices[i].cget('bg') == vertices[j].cget('bg'):
                    win = False

    if win == False:
        canvas.delete("all")
        draw_edges()
        directions()
        canvas.create_text(750, 400, font="Times 19", text="You Lose", fill='red')
    else:
        canvas.delete("all")
        draw_edges()
        directions()
        canvas.create_text(750, 400, font="Times 19", text="You Win", fill='green')
    return


def directions():
    canvas.create_text(10, 10, width=650, font="Times 15", anchor='nw',
                       text="Directions: Color all the squares so that "
                            "squares that are connected by a line "
                            "don't have the same color. Use the three buttons on "
                            "the left to select the colors. ")
    return


def next_button():
    nxt_btn = tk.Button(root, text="Next Level", bg='grey', height=2, width=11, command=lambda: next_level())
    nxt_btn.place(x=1400, y=750, anchor='center')
    return


# Increases level by 1 and redraws board.
def next_level():
    global level
    if level != len(level_lst)-1:
        level += 1
        reset_borad()
    if level > 2:
        yellow_btn.configure(state = 'normal', bg='#FFFC5A',bd=2)
    return


def previous_button():
    nxt_btn = tk.Button(root, text="Previous Level", bg='grey', height=2, width=11, command=lambda: previous_level())
    nxt_btn.place(x=1300, y=750, anchor='center')
    return


# Decreases level by 1 and redraws board.
def previous_level():
    global level
    if level > 0:
        level -= 1
        reset_borad()
    if level < 3:
        yellow_btn.configure(state='disabled',bg='#d9d9d9',bd=0)
    return


## ---Create Window---
root = tk.Tk()
canvas = tk.Canvas(root, width=1500, height=800, bg='#d9d9d9')
canvas.pack()
root.resizable(False, False)


##----Color Buttons----
red_btn = tk.Button(root, text="", bg='red', height=4, width=8, command=lambda: set_color('red'))
red_btn.place(x=4, y=200)

blue_btn = tk.Button(root, text="", bg='blue', height=4, width=8, command=lambda: set_color('blue'))
blue_btn.place(x=4, y=300)

green_btn = tk.Button(root, text="", bg='green', height=4, width=8, command=lambda: set_color('green'))
green_btn.place(x=4, y=400)

yellow_btn = tk.Button(root, text="", bg='#d9d9d9', height=4, width=8,bd=0, state = 'disabled' ,command=lambda: set_color('#FFFC5A'))
yellow_btn.place(x=4, y=500)


##----Draws Veritces----

# outer pentagon, center=(750,400), raddius= 350
vertices[0] = tk.Button(root, bg=vertex_color[0], height=2, width=4, command=lambda: vertex_button_function(0))
vertices[0].place(x=vertex_cords[0][0], y=vertex_cords[0][1], anchor='center')

vertices[1] = tk.Button(root, bg=vertex_color[1], height=2, width=4, command=lambda: vertex_button_function(1))
vertices[1].place(x=vertex_cords[1][0], y=vertex_cords[1][1], anchor='center')

vertices[2] = tk.Button(root, bg=vertex_color[2], height=2, width=4, command=lambda: vertex_button_function(2))
vertices[2].place(x=vertex_cords[2][0], y=vertex_cords[2][1], anchor='center')

vertices[3] = tk.Button(root, bg=vertex_color[3], height=2, width=4, command=lambda: vertex_button_function(3))
vertices[3].place(x=vertex_cords[3][0], y=vertex_cords[3][1], anchor='center')

vertices[4] = tk.Button(root, bg=vertex_color[4], height=2, width=4, command=lambda: vertex_button_function(4))
vertices[4].place(x=vertex_cords[4][0], y=vertex_cords[4][1], anchor='center')

# inner pentagon, center=(750,400), raddius= 175
vertices[5] = tk.Button(root, bg=vertex_color[5], height=2, width=4, command=lambda: vertex_button_function(5))
vertices[5].place(x=vertex_cords[5][0], y=vertex_cords[5][1], anchor='center')

vertices[6] = tk.Button(root, bg=vertex_color[6], height=2, width=4, command=lambda: vertex_button_function(6))
vertices[6].place(x=vertex_cords[6][0], y=vertex_cords[6][1], anchor='center')

vertices[7] = tk.Button(root, bg=vertex_color[7], height=2, width=4, command=lambda: vertex_button_function(7))
vertices[7].place(x=vertex_cords[7][0], y=vertex_cords[7][1], anchor='center')

vertices[8] = tk.Button(root, bg=vertex_color[8], height=2, width=4, command=lambda: vertex_button_function(8))
vertices[8].place(x=vertex_cords[8][0], y=vertex_cords[8][1], anchor='center')

vertices[9] = tk.Button(root, bg=vertex_color[9], height=2, width=4, command=lambda: vertex_button_function(9))
vertices[9].place(x=vertex_cords[9][0], y=vertex_cords[9][1], anchor='center')


"""
for i in range(len(vertex_cords)):
    vertices[i] = tk.Button(root, bg=vertex_color[i], fg='black', height=2, width=4, command= lambda: vertex_button_function(i))
    vertices[i].place(x=vertex_cords[i][0], y=vertex_cords[i][1], anchor='center')
"""


## ---Run functions---
check_graph_button()
reset_button()
next_button()
previous_button()
draw_edges()
directions()

root.mainloop()
