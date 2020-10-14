import tkinter as tk
import datetime


def get_daily_log_topic():
    today = datetime.date.today()
    topic = str(today.month) + '.' + str(today.day) + '.'
    weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    topic += weekdays[today.weekday()]
    return topic


class ToDoList(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=tk.YES, fill=tk.BOTH, padx=8, pady=8)
        self.create_widgets()

    def create_widgets(self):
        # build the task entry form
        form = tk.Frame(self)
        form.pack(side=tk.BOTTOM, fill=tk.BOTH)

        row = tk.Frame(form)  # top row
        row.pack(fill=tk.X, pady=4)
        label = tk.Label(row, text='New task:', width=10)
        label.pack(side=tk.LEFT)
        self.entry = tk.Entry(row, font=(None, 10))
        self.entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

        row = tk.Frame(form)  # bottom row
        row.pack(fill=tk.X)
        btn = tk.Button(row, text='Add task', command=self.add_task)
        btn.pack(side=tk.RIGHT)

        # bind the enter key to the entry widget
        self.entry.bind('<Return>', lambda event: self.add_task())
        self.entry.focus()

        # build the title bar (collection.topic)
        frame = tk.Frame(self)
        frame.pack(side=tk.TOP, fill=tk.X)
        collection = 'Daily Log'
        label = tk.Label(self, text=collection)
        label.pack()
        topic = get_daily_log_topic()
        label = tk.Label(self, text=topic, font=(None, 12, 'bold'))
        label.pack()

    def add_task(self):
        # fetch the new task and clear the entry widget
        bullet = '\u2022'
        task = bullet + ' ' + str(self.entry.get())
        self.entry.delete(0, tk.END)

        # add the new task to the current collection
        row = tk.Frame(self)
        row.pack(fill=tk.X, padx=16)
        label = tk.Label(row, text=task)
        label.pack(side=tk.LEFT)
