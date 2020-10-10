import tkinter as tk


def create_demo_widgets():
        # TODO: Fix packing (expand and fill).  Demos use fixed-size widgets.
        # TODO: Change style/theme (e.g. colors).
        win = tk.Toplevel()
        top = tk.Frame(win, bg='black')
        ColorsDemo(top).pack(side=tk.LEFT, padx=8)
        BordersDemo(top).pack(side=tk.LEFT, pady=8)
        CursorsDemo(top).pack(side=tk.LEFT, padx=8)
        top.pack(padx=8, pady=8)
        FontsDemo(win).pack(padx=8, pady=8)


class TestWidget(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets():
        pass


class ColorsDemo(TestWidget):
    def create_widgets(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        for color in colors:
            label = tk.Label(self)
            label['text'] = color.upper()
            label['bg'] = color
            if color != 'orange' and color != 'yellow':
                label['fg'] = 'white'
            label['font'] = ('TkDefaultFont', 12, 'bold')
            label.config(width=20, height=2)  # chars, lines
            label.pack()


class BordersDemo(TestWidget):
    def create_widgets(self):
        self['bg'] = 'dark gray'
        reliefs = [tk.FLAT, tk.RAISED, tk.SUNKEN, tk.GROOVE, tk.RIDGE, 
                   tk.SOLID]
        for relief in reliefs:
            btn = tk.Button(self)
            btn['text'] = relief.upper()
            btn['bd'] = 5
            btn['relief'] = relief
            btn.config(width=24, height=2)
            btn.pack(padx=4, pady=4)


class CursorsDemo(TestWidget):
    def create_widgets(self):
        self['bg'] = 'dark gray'
        cursors = ['watch', 'pencil', 'cross', 'hand2']
        for cursor in cursors:
            label = tk.Label(self)
            label['text'] = cursor.upper()
            label['cursor'] = cursor
            label.config(width=24, height=4)
            label.pack(padx=4, pady=4)


class FontsDemo(TestWidget):
    def create_widgets(self):
        self['bg'] = 'black'
        fonts = ['courier', 'times', 'helvetica', 'consolas']
        pangram = 'The quick brown fox jumps over the lazy dog.'
        for font in fonts:
            label = tk.Label(self)
            label['text'] = font.upper() + '\n' + pangram
            label['font'] = (font, 16)
            label.config(bg='black', fg='white')
            label.pack(padx=12, pady=8)
