import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk

mainWindow = tkinter.Tk()

# Configure geometry of mainWindow to show it at the centre of System screen
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
mainWindow_width = 450
mainWindow_height = 475
pad_x = (screen_width - mainWindow_width) // 2
pad_y = (screen_height - mainWindow_height) // 2
mainWindow_geometry = str(mainWindow_width) + 'x' + str(mainWindow_height) + '-' + str(pad_x) + '-' + str(pad_y)
mainWindow.geometry(mainWindow_geometry)
# ---------------------------------------------------
mainWindow.title("TicTacToe by urvisism")
mainWindow.resizable(False, False)

image_height = 100
image_width = 100
btn_bg_colour = 'white'

open_cross = Image.open(r'images/cross.png')
resize_cross = open_cross.resize((image_width, image_height))
cross = ImageTk.PhotoImage(resize_cross)

open_zero = Image.open(r'images/zero.png')
resize_zero = open_zero.resize((image_width, image_height))
zero = ImageTk.PhotoImage(resize_zero)

open_trans = Image.open(r'images/trans.jpg')
resize_trans = open_trans.resize((image_width, image_height))
trans = ImageTk.PhotoImage(resize_trans)

# Configure all rows
for i in range(7):
    mainWindow.rowconfigure(i, weight=10)

# Configure all columns
for i in range(6):
    mainWindow.columnconfigure(i, weight=10)

# Create buttons
btn1 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(1))
btn1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn2 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(2))
btn2.grid(row=0, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn3 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(3))
btn3.grid(row=0, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn4 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(4))
btn4.grid(row=2, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn5 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(5))
btn5.grid(row=2, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn6 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(6))
btn6.grid(row=2, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn7 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(7))
btn7.grid(row=4, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn8 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(8))
btn8.grid(row=4, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn9 = tkinter.Button(mainWindow, bg=btn_bg_colour, command=lambda: click(9))
btn9.grid(row=4, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)

# Create restart button
restart_btn = tkinter.Button(mainWindow, command=lambda: restart_game())
restart_btn.configure(text='RESTART', font='Abc 10 bold', bg='#008000')
restart_btn.grid(row=6, column=0, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)

# Create close button
close_btn = tkinter.Button(mainWindow, command=mainWindow.destroy)
close_btn.configure(text='CLOSE', font='Abc 10 bold', bg='#FF0000')
close_btn.grid(row=6, column=4, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)


# Create function
def click(n):
    global zero, cross, turn, clicked_btn, used_btn
    clicked_btn = n

    if clicked_btn not in used_btn:
        turn += 1
        used_btn.append(clicked_btn)
        assign_image()
        winner()


def assign_image():
    global turn, clicked_btn

    if turn % 2 != 0:
        button[clicked_btn].configure(image=zero, bg='#1ABDD5')
    else:
        button[clicked_btn].configure(image=cross, bg='#D8B9FA')


def winner():
    global turn, clicked_btn, odd_turn, even_turn

    if turn % 2 != 0:
        odd_turn.append(clicked_btn)
    else:
        even_turn.append(clicked_btn)

    check_rows()
    check_columns()
    check_diagonals()
    check_tie()


def check_rows():
    global odd_turn, even_turn, turn, message1, message2, message3, game_running
    row1 = False
    row2 = False
    row3 = False

    if (1 in odd_turn and 2 in odd_turn and 3 in odd_turn) or \
            (1 in even_turn and 2 in even_turn and 3 in even_turn):
        row1 = True
    elif (4 in odd_turn and 5 in odd_turn and 6 in odd_turn) or \
            (4 in even_turn and 5 in even_turn and 6 in even_turn):
        row2 = True
    elif (7 in odd_turn and 8 in odd_turn and 9 in odd_turn) or \
            (7 in even_turn and 8 in even_turn and 9 in even_turn):
        row3 = True

    if (row1 or row2 or row3) and (turn % 2 != 0):
        game_running = False
        message_box(message1)
    elif (row1 or row2 or row3) and (turn % 2 == 0):
        game_running = False
        message_box(message2)


def check_columns():
    global odd_turn, even_turn, turn, message1, message2, message3, game_running
    col1 = False
    col2 = False
    col3 = False

    if (1 in odd_turn and 4 in odd_turn and 7 in odd_turn) or \
            (1 in even_turn and 4 in even_turn and 7 in even_turn):
        col1 = True
    elif (2 in odd_turn and 5 in odd_turn and 8 in odd_turn) or \
            (2 in even_turn and 5 in even_turn and 8 in even_turn):
        col2 = True
    elif (3 in odd_turn and 6 in odd_turn and 9 in odd_turn) or \
            (3 in even_turn and 6 in even_turn and 9 in even_turn):
        col3 = True

    if (col1 or col2 or col3) and (turn % 2 != 0):
        game_running = False
        message_box(message1)
    elif (col1 or col2 or col3) and (turn % 2 == 0):
        game_running = False
        message_box(message2)


def check_diagonals():
    global odd_turn, even_turn, turn, message1, message2, message3, game_running
    dia1 = False
    dia2 = False

    if (1 in odd_turn and 5 in odd_turn and 9 in odd_turn) or \
            (1 in even_turn and 5 in even_turn and 9 in even_turn):
        dia1 = True
    elif (3 in odd_turn and 5 in odd_turn and 7 in odd_turn) or \
            (3 in even_turn and 5 in even_turn and 7 in even_turn):
        dia2 = True

    if (dia1 or dia2) and (turn % 2 != 0):
        game_running = False
        message_box(message1)
    elif (dia1 or dia2) and (turn % 2 == 0):
        game_running = False
        message_box(message2)


def check_tie():
    global turn, game_running
    if turn == 9 and game_running:
        message_box(message3)


def message_box(message):
    return_value = messagebox.askyesno('Winner', message)
    if return_value:
        restart_game()
    else:
        mainWindow.destroy()


def restart_game():
    global turn, clicked_btn, used_btn, odd_turn, even_turn, btn_bg_colour, game_running
    turn, clicked_btn, used_btn, odd_turn, even_turn, game_running = 0, 0, [], [], [], True
    for btn in button.values():
        btn.configure(image=trans, bg=btn_bg_colour)


if __name__ == '__main__':
    button = {1: btn1, 2: btn2, 3: btn3, 4: btn4, 5: btn5, 6: btn6, 7: btn7, 8: btn8, 9: btn9}
    turn, clicked_btn, used_btn, odd_turn, even_turn, game_running = 0, 0, [], [], [], True
    message1 = "Player 'O' Won.\n\nPlay Again?"
    message2 = "Player 'X' Won.\n\nPlay Again?"
    message3 = "It's a tie.\n\nPlay Again?"
    restart_game()

mainWindow.mainloop()