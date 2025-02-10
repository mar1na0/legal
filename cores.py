import tkinter as tk
root=tk.Tk()

root.title('Color change')
root.geometry('500x600+400+100')
root.wm_resizable(width=False, height=False)

def change_toblue():
    bluebutton.config(bg='blue', fg='white')
    root.configure(bg='blue')
    nomecor.config(text='azul', bg='blue', fg='white')
bluebutton = tk.Button(root, text='azul', command=change_toblue, font='Arial 14 bold')
bluebutton.pack(pady=10)
bluebutton.place(x=40, y=20, width=200, height=160)

def change_tored():
    redbutton.config(bg='red', fg='white')
    root.configure(bg='red')
    nomecor.config(text='vermelho', bg='red', fg='white')
redbutton = tk.Button(root, text='vermelho', command=change_tored, font='Arial 14 bold')
redbutton.pack(pady=10)
redbutton.place(x=260, y=20, width=200, height=160)

def change_toyellow():
    yellowbutton.config(bg='yellow', fg='grey')
    root.configure(bg='yellow')
    nomecor.config(text='amarelo', bg='yellow', fg='grey')
yellowbutton = tk.Button(root, text='amarelo', command=change_toyellow, font='Arial 14 bold')
yellowbutton.pack(pady=10)
yellowbutton.place(x=40, y=200, width=200, height=160)

def change_togreen():
    greenbutton.config(bg='green', fg='white')
    root.configure(bg='green')
    nomecor.config(text='verde', bg='green', fg='white')
greenbutton = tk.Button(root, text='verde', command=change_togreen, font='Arial 14 bold')
greenbutton.pack(pady=10)
greenbutton.place(x=260, y=200, width=200, height=160)

nomecor=tk.Label(root, text='olá mundo!', fg='black', bg='white', font='Arial 14 bold')
nomecor.pack(pady=10)
nomecor.place(x=150, y=400, width=200, height=160)

root.mainloop()