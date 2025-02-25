import tkinter as tk
root=tk.Tk()
clicar=1

root.title('Jogo da Velha')
root.geometry('700x800+400+100')
root.wm_resizable(width=False, height=False)

def clicar0():
    global clicar
    if botao1["text"]=='':
        if clicar%2!=0:
            botao1.config(text='X')

        else:
            botao1.config(text='O')
        clicar+=1

botao1 = tk.Button(root, text='', command=lambda: clicar0(), font='Arial 14 bold')
botao1.pack(pady=10)
botao1.place(x=40, y=20, width=200, height=160)

def clicar2():
    global clicar
    if botao2["text"]=='':
        if clicar%2!=0:
            botao2.config(text='X')

        else:
            botao2.config(text='O')
        clicar+=1

botao2 = tk.Button(root, text='', command=lambda: clicar2(), font='Arial 14 bold')
botao2.pack(pady=10)
botao2.place(x=260, y=20, width=200, height=160)

def clicar3():
    global clicar
    if botao3["text"]=='':
        if clicar%2!=0:
            botao3.config(text='X')

        else:
            botao3.config(text='O')
        clicar+=1

botao3 = tk.Button(root, text='', command=lambda: clicar3(), font='Arial 14 bold')
botao3.pack(pady=10)
botao3.place(x=40, y=200, width=200, height=160)

def clicar4():
    global clicar
    if botao4["text"]=='':
        if clicar%2!=0:
            botao4.config(text='X')

        else:
            botao4.config(text='O')
        clicar+=1

botao4 = tk.Button(root, text='', command=lambda: clicar4(), font='Arial 14 bold')
botao4.pack(pady=10)
botao4.place(x=260, y=200, width=200, height=160)

def clicar5():
    global clicar
    if botao5["text"]=='':
        if clicar%2!=0:
            botao5.config(text='X')

        else:
            botao5.config(text='O')
        clicar+=1

botao5 = tk.Button(root, text='', command=lambda: clicar5(), font='Arial 14 bold')
botao5.pack(pady=10)
botao5.place(x=480, y=200, width=200, height=160)

def clicar6():
    global clicar
    if botao6["text"]=='':
        if clicar%2!=0:
            botao6.config(text='X')

        else:
            botao6.config(text='O')
        clicar+=1

botao6 = tk.Button(root, text='', command=lambda: clicar6(), font='Arial 14 bold')
botao6.pack(pady=10)
botao6.place(x=480, y=20, width=200, height=160)

def clicar7():
    global clicar
    if botao7["text"]=='':
        if clicar%2!=0:
            botao7.config(text='X')

        else:
            botao7.config(text='O')
        clicar+=1

botao7 = tk.Button(root, text='', command=lambda: clicar7(), font='Arial 14 bold')
botao7.pack(pady=10)
botao7.place(x=480, y=400, width=200, height=160)

def clicar8():
    global clicar
    if botao8["text"]=='':
        if clicar%2!=0:
            botao8.config(text='X')

        else:
            botao8.config(text='O')
        clicar+=1

botao8 = tk.Button(root, text='', command=lambda: clicar8(), font='Arial 14 bold')
botao8.pack(pady=10)
botao8.place(x=260, y=400, width=200, height=160)

def clicar9():
    global clicar
    if botao9["text"]=='':
        if clicar%2!=0:
            botao9.config(text='X')

        else:
            botao9.config(text='O')
        clicar+=1

botao9 = tk.Button(root, text='', command=lambda: clicar9(), font='Arial 14 bold')
botao9.pack(pady=10)
botao9.place(x=40, y=400, width=200, height=160)

root.mainloop()
