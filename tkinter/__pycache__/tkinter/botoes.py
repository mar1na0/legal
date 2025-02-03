import tkinter as tk
root=tk.Tk()

root.title("awesome")

def mudar_texto():
    button1.config(text="parabéns!")

button1 = tk.Button(root, text="me clique!", command=mudar_texto)
button1.pack(pady=10)

def mudar_cor():
    button2.config(text="wow!", bg="red", fg="white")

button2 = tk.Button(root, text="mudar cor", command=mudar_cor)
button2.pack(pady=10)

def mudar_botao4():
    button4.config(text="olá!", bg="black", fg="white")

button3 = tk.Button(root, text="olá", command=mudar_botao4)
button3.pack(pady=10)

def mudar_botao3():
    button3.config(text="oi", bg="black", fg="white")

button4 = tk.Button(root, text="oi", command=mudar_botao3)
button4.pack(pady=10)

root.mainloop()