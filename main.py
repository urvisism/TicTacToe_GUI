import tkinter
from PIL import Image, ImageTk

mainWindow = tkinter.Tk()
mainWindow.title("TicTacToe by urvisism")
mainWindow.geometry('450x475')
mainWindow.resizable(False, False)

image_height = 100
image_width = 100

open_cross = Image.open(r'images/cross.png')
resize_cross = open_cross.resize((image_width, image_height))
cross = ImageTk.PhotoImage(resize_cross)

open_zero = Image.open(r'images/zero.png')
resize_zero = open_zero.resize((image_width, image_height))
zero = ImageTk.PhotoImage(resize_zero)

open_trans = Image.open(r'images/trans.png')
resize_trans = open_trans.resize((image_width, image_height))
trans = ImageTk.PhotoImage(resize_trans)

mainWindow.rowconfigure(0, weight=10)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=10)
mainWindow.rowconfigure(3, weight=10)
mainWindow.rowconfigure(4, weight=10)
mainWindow.rowconfigure(5, weight=10)
mainWindow.rowconfigure(6, weight=10)

mainWindow.columnconfigure(0, weight=10)
mainWindow.columnconfigure(1, weight=10)
mainWindow.columnconfigure(2, weight=10)
mainWindow.columnconfigure(3, weight=10)
mainWindow.columnconfigure(4, weight=10)
mainWindow.columnconfigure(5, weight=10)

# Create a buttons
btn1 = tkinter.Button(mainWindow, command=lambda: click(1))
btn1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn2 = tkinter.Button(mainWindow, command=lambda: click(2))
btn2.grid(row=0, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn3 = tkinter.Button(mainWindow, command=lambda: click(3))
btn3.grid(row=0, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn4 = tkinter.Button(mainWindow, command=lambda: click(4))
btn4.grid(row=2, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn5 = tkinter.Button(mainWindow, command=lambda: click(5))
btn5.grid(row=2, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn6 = tkinter.Button(mainWindow, command=lambda: click(6))
btn6.grid(row=2, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn7 = tkinter.Button(mainWindow, command=lambda: click(7))
btn7.grid(row=4, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn8 = tkinter.Button(mainWindow, command=lambda: click(8))
btn8.grid(row=4, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
btn9 = tkinter.Button(mainWindow, command=lambda: click(9))
btn9.grid(row=4, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)

# Create restart button
restart_btn = tkinter.Button(mainWindow, text='RESTART', font='Abc 10 bold', command=lambda: restart_game())
restart_btn.grid(row=6, column=0, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)

# Create close button
close_btn = tkinter.Button(mainWindow, text='CLOSE', font='Abc 10 bold', command=mainWindow.destroy)
close_btn.grid(row=6, column=4, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)

# Create function


def click(n):
    global zero, cross, turn, clicked_btn, used_btn
    clicked_btn = n

    if clicked_btn not in used_btn:
        turn += 1
        used_btn.append(clicked_btn)
        return assign_image(clicked_btn, turn)


def assign_image(clicked_btn_, turn_):
    if turn_ % 2 != 0:
        button[clicked_btn_].configure(image=zero)
    else:
        button[clicked_btn_].configure(image=cross)


def restart_game():
    for btn in button.values():
        btn.configure(image=trans)


if __name__ == '__main__':
    turn = 0
    clicked_btn = 0
    button = {1: btn1, 2: btn2, 3: btn3, 4: btn4, 5: btn5, 6: btn6, 7: btn7, 8: btn8, 9: btn9}
    used_btn = []
    restart_game()


mainWindow.mainloop()