import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("TicTacToe by urvisism")
mainWindow.geometry('450x475')
mainWindow.resizable(False, False)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.columnconfigure(5, weight=1)

# Create a buttons

tkinter.Button(mainWindow).grid(row=0, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=0, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=0, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=2, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=2, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=2, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=4, column=0, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=4, column=2, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)
tkinter.Button(mainWindow).grid(row=4, column=4, rowspan=2, columnspan=2, sticky='news', padx=10, pady=10)

# Create restart button
tkinter.Button(mainWindow, text='RESTART').grid(row=6, column=0, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)

# Create close button
tkinter.Button(mainWindow, text='CLOSE').grid(row=6, column=4, rowspan=1, columnspan=2, sticky='news', padx=10, pady=10)



mainWindow.mainloop()