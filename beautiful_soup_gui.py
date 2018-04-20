"""
Graphical Program that uses Beautiful Data module to display stock prices from Bloomberg
Christopher Calmes
4/18/2018
"""

# imports
from tkinter import *

try:
    from .beautiful_soup import BeautifulData
except SystemError:
    from beautiful_soup import BeautifulData

data = BeautifulData()


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # change title of windows
        self.master.title("Stock Prices")

        # allow widget to take the full space of the window
        self.pack(fill=BOTH, expand=1)

        prices_text = Text(root, height=10, width=40)

        # create a button
        get_data_button = Button(self, text="Get new prices", command=lambda: self.update_text(prices_text))

        # put button on spot on window
        get_data_button.pack(side="top", fill='x', expand=True, padx=10, pady=10)

    def update_text(self, text):
        prices = data.get_data
        # text delete expects a string representation of the floated value of the number of lines of text starting at 1
        text.delete('1.0', str(float(len(prices)) + 1))
        for price in prices:
            text.insert(END, str(price[0]) + ": " + str(price[1]) + "\n")
        text.pack(fill='x', padx=10, pady=10)

    def client_exit(self):
        exit()


root = Tk()

# size of the window
root.geometry("400x200")

app = Window(root)
root.mainloop()
