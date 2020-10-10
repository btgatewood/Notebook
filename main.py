import tkinter as tk


class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(expand=tk.YES, fill=tk.BOTH)
    
    def create_widgets(self):
        # build the task entry form
        row = tk.Frame(self)
        label = tk.Label(row, text='New task:', width=10)
        label.pack(side=tk.LEFT)
        self.entry = tk.Entry(row)
        self.entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        row.pack(side=tk.TOP, fill=tk.X)
        btn = tk.Button(self, text='Add task', command=self.add_task)
        btn.pack(side=tk.RIGHT)  # TODO: anchor button to form
        # TODO: bind enter key to add task

    def add_task(self):
        print(self.entry.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Notebook')
    app = App(root)
    root.mainloop()
