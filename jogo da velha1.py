import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
clicar=1

root.title('Jogo da Velha')
root.geometry('700x600+400+100')
root.wm_resizable(width=False, height=False)

def clicar0(botao):
    global clicar
    if botao["text"]=='':
        if clicar%2!=0:
            botao.config(text='X')

        else:
            botao.config(text='O')
        clicar+=1
    vencer_possibilidades()

def vencer(x, y, z):
    if x["text"]==y["text"] and x["text"]==z["text"] and x["text"]!='':
        if x["text"]=='X':
            messagebox.showinfo("", "X venceu!")
        else:
            messagebox.showinfo("", "O venceu!")

def vencer_possibilidades():
    #horizontais
    vencer(botao1, botao2, botao3)
    vencer(botao4, botao5, botao6)
    vencer(botao7, botao8, botao9)
    #verticais
    vencer(botao1, botao4, botao7)
    vencer(botao2, botao5, botao8)
    vencer(botao3, botao6, botao9)
    #diagonais
    vencer(botao1, botao5, botao9)
    vencer(botao3, botao5, botao7)
    
botao1 = tk.Button(root, text='', command=lambda: clicar0(botao1), font='Arial 14 bold')
botao1.pack(pady=10)
botao1.place(x=40, y=20, width=200, height=160)

botao2 = tk.Button(root, text='', command=lambda: clicar0(botao2), font='Arial 14 bold')
botao2.pack(pady=10)
botao2.place(x=260, y=20, width=200, height=160)

botao4 = tk.Button(root, text='', command=lambda: clicar0(botao4), font='Arial 14 bold')
botao4.pack(pady=10)
botao4.place(x=40, y=200, width=200, height=160)

botao5 = tk.Button(root, text='', command=lambda: clicar0(botao5), font='Arial 14 bold')
botao5.pack(pady=10)
botao5.place(x=260, y=200, width=200, height=160)

botao6 = tk.Button(root, text='', command=lambda: clicar0(botao6), font='Arial 14 bold')
botao6.pack(pady=10)
botao6.place(x=480, y=200, width=200, height=160)

botao3 = tk.Button(root, text='', command=lambda: clicar0(botao3), font='Arial 14 bold')
botao3.pack(pady=10)
botao3.place(x=480, y=20, width=200, height=160)

botao9 = tk.Button(root, text='', command=lambda: clicar0(botao9), font='Arial 14 bold')
botao9.pack(pady=10)
botao9.place(x=480, y=400, width=200, height=160)

botao8 = tk.Button(root, text='', command=lambda: clicar0(botao8), font='Arial 14 bold')
botao8.pack(pady=10)
botao8.place(x=260, y=400, width=200, height=160)

botao7 = tk.Button(root, text='', command=lambda: clicar0(botao7), font='Arial 14 bold')
botao7.pack(pady=10)
botao7.place(x=40, y=400, width=200, height=160)

root.mainloop()
