import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
clicar=1
venceu=False
botoescheios=False

root.title('Jogo da Velha')
root.geometry('600x600')
root.wm_resizable(width=False, height=False)

def clicar0(botao):
    global clicar, venceu, botoes
    while venceu==False:
        if botao["text"]=='':
            if clicar%2!=0:
                botao.config(text='X')
            else:
                botao.config(text='O')
            clicar+=1
        vencer_possibilidades()
        break

def acabar_jogo(x, y, z,):
    global venceu, botoes
    empate(botoes)
    if x["text"]==y["text"] and x["text"]==z["text"] and x["text"]!='':
        venceu=True
        if x["text"]=='X':
            messagebox.showinfo("", "X venceu!")
        else:
            messagebox.showinfo("", "O venceu!")
        reiniciar(botoes)
    
    if botoescheios==True:
        messagebox.showinfo("", "empate...")
        reiniciar(botoes)

def reiniciar(botoes):
    global venceu, botoescheios
    for reiniciou in botoes:
        reiniciou["text"]='' #chatgpt me ajudou nessa única linha, mas eu tava quase lá (for loop é dificil)
    venceu=False
    botoescheios=False

def empate(botoes):
    global venceu, botoescheios
    if  all(botao["text"]!='' for botao in botoes): #chat gpt me ajudou nessa, mas eu não sabia usar o all(), então é justo
            botoescheios=True
    
def vencer_possibilidades():
    global botoescheios, botoes
    #horizontais
    acabar_jogo(botao1, botao2, botao3)
    acabar_jogo(botao4, botao5, botao6)
    acabar_jogo(botao7, botao8, botao9)
    #verticais
    acabar_jogo(botao1, botao4, botao7)
    acabar_jogo(botao2, botao5, botao8)
    acabar_jogo(botao3, botao6, botao9)
    #diagonais
    acabar_jogo(botao1, botao5, botao9)
    acabar_jogo(botao3, botao5, botao7)
    
botao1 = tk.Button(root, text='', command=lambda: clicar0(botao1), font='Arial 150')
botao1.place(x=0, y=0, width=200, height=200)

botao2 = tk.Button(root, text='', command=lambda: clicar0(botao2), font='Arial 150')
botao2.place(x=200, y=0, width=200, height=200)

botao3 = tk.Button(root, text='', command=lambda: clicar0(botao3), font='Arial 150')
botao3.place(x=400, y=0, width=200, height=200)

botao4 = tk.Button(root, text='', command=lambda: clicar0(botao4), font='Arial 150')
botao4.place(x=0, y=200, width=200, height=200)

botao5 = tk.Button(root, text='', command=lambda: clicar0(botao5), font='Arial 150')
botao5.place(x=200, y=200, width=200, height=200)

botao6 = tk.Button(root, text='', command=lambda: clicar0(botao6), font='Arial 150')
botao6.place(x=400, y=200, width=200, height=200)

botao7 = tk.Button(root, text='', command=lambda: clicar0(botao7), font='Arial 150')
botao7.place(x=0, y=400, width=200, height=200)

botao8 = tk.Button(root, text='', command=lambda: clicar0(botao8), font='Arial 150')
botao8.place(x=200, y=400, width=200, height=200)

botao9 = tk.Button(root, text='', command=lambda: clicar0(botao9), font='Arial 150')
botao9.place(x=400, y=400, width=200, height=200)

botoes=[botao1, botao2, botao3, botao4, botao5, botao6, botao7, botao8, botao9]

root.mainloop()
