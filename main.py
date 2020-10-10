import tkinter as tk


class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title('Notebook')
        root.geometry('360x640')
        self.create_widgets()
        self.pack(expand=tk.YES, fill=tk.BOTH, padx=8, pady=8)
    
    def create_widgets(self):
        # build the task entry form
        form = tk.Frame(self)
        form.pack(side=tk.BOTTOM, fill=tk.BOTH)

        row = tk.Frame(form)  # top row
        row.pack(fill=tk.X, pady=4)
        label = tk.Label(row, text='New task:', width=8)
        label.pack(side=tk.LEFT)
        self.entry = tk.Entry(row)
        self.entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

        row = tk.Frame(form)  # bottom row
        row.pack(fill=tk.X)
        btn = tk.Button(row, text='Add task', command=self.add_task)
        btn.pack(side=tk.RIGHT)

        # bind the enter key to the entry widget
        self.entry.bind('<Return>', lambda event: self.add_task())
        self.entry.focus()

    def add_task(self):
        print(self.entry.get())


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
