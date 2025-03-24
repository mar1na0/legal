import tkinter as tk
from tkinter import Entry
root=tk.Tk()

root.title("awesome")

input_senha= Entry(root, font='Time 10', show='*')
input_senha.place(width=250,height=20,x=100,y=110)

root.mainloop()