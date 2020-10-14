import tkinter as tk
import tkinter.font

from todolist import ToDoList


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Notebook')
    root.geometry('360x640')

    # change the default font size
    tk.font.nametofont('TkDefaultFont').configure(size=10)

    todo = ToDoList(root)
    root.mainloop()
