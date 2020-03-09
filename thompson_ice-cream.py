import tkinter as tk
from tkinter import *

root = tk.Tk()

c = Canvas(root, width = 300, height = 300)
c.grid()


c.create_oval(100,100,200,200, fill = 'red')







root.mainloop()