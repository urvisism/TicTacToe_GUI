import tkinter
from PIL import Image, ImageTk

mainWindow = tkinter.Tk()
mainWindow.title("TicTacToe by urvisism")
mainWindow.geometry('450x475')
mainWindow.resizable(False, False)

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
image_height = 100
image_width = 100

open_cross = Image.open(r'images/cross.png')
resize_cross = open_cross.resize((image_width, image_height))
cross = ImageTk.PhotoImage(resize_cross)

open_zero = Image.open(r'images/zero.png')
resize_zero = open_zero.resize((image_width, image_height))
zero = ImageTk.PhotoImage(resize_zero)

tkinter.Button(mainWindow, image=cross).grid(row=0, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=zero).grid(row=0, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=cross).grid(row=0, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=zero).grid(row=2, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=cross).grid(row=2, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=zero).grid(row=2, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=cross).grid(row=4, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=zero).grid(row=4, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow, image=cross).grid(row=4, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)

# Create restart button
tkinter.Button(mainWindow, text='RESTART').grid(row=6, column=0, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)

# Create close button
tkinter.Button(mainWindow, text='CLOSE', command=mainWindow.destroy).grid(row=6, column=4, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)



mainWindow.mainloop()