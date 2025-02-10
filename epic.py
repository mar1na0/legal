import tkinter as tk
import random

root=tk.Tk()

root.title("cool")

def andar(input):
    input= inputtxt.get("1.0", "end-1c")
    print(input)
    if(input== "w"):
        button1.place(x=0, y=1)

button1 = tk.Button(root, text="0________________0", command=andar)
button1.pack(pady=20)
button1.place(x=100, y=100, width=150, height=150)

inputtxt = tk.Text(root, height=5, width=20)
inputtxt.place(x=0, y=0)

root.mainloop()

#>:((((((((((((((((((((((((