import tkinter as tk
import random

root=tk.Tk()
#positionx= random.randint(0, 500)
#positiony= random.randint(0, 500)

root.title("awesome")

def mudar_posicao(positionx, positiony, button1):
    button1.config(text="parabéns!")
    button1.place(x=positionx, y=positiony)

button1 = tk.Button(root, text="me clique!", command=lambda: mudar_posicao(random.randint(0, 500), random.randint(0, 500), button1))
button1.pack(pady=20)
button1.place(x=50, y=10, width=150, height=150)

def mudar_cor():
    button2.config(text='wow!', bg="black", fg="white", font="Time 50 bold")
    print("wow")

button2 = tk.Button(root, text="clique aqui!", command=mudar_cor)
button2.pack(pady=20)
button2.place(x=550, y=10)

label1 = tk.Label(root, text="eae")
label1.place(x=500, y=200, width=80, height=30)


root.mainloop()