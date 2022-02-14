import tkinter as tk

FONT = ("Arial", 20, "bold")
# from now onwards, I will start learning gui programming by using tkinter module in python.

window = tk.Tk()  # defined a window which will create a window screen.

window.title("First GUI Program")  # title of the window
window.minsize(width=600, height=400)  # initialize minimum size to the window.

# initializing my label object of tk module.
my_label = tk.Label(text="This is my first GUI program.", font=FONT)
# my_label.pack()  # without writing this cmd we will not be able to see any output.
# my_label.pack(side="top")  # we can define side => left or right or bottom or top.
my_label.pack(expand=True)  # expend = True => will take whole window as a label.


window.mainloop()   # by using this method we will take window object running forever.

