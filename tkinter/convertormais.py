import requests 
from tkinter import *

url=requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
print(url)
conversao=url.json()
print(conversao)

tela1=Tk()
tela1.title("convertor")
tela1.geometry('350x200')
tela1.wm_resizable(width=False, height=False)

mensagem=Label(tela1, text="Qual moeda que você quer converter?", font='Time 15', anchor='w')
mensagem.place(x=5, y=10, width=500, height=20)

beuro = Button(tela1, text="euro", font='Time 15', command=lambda:criar_telaeuro())
beuro.place(x=10, y=40, width=100, height=60)

breal = Button(tela1, text="real", font='Time 15', command=lambda:criar_telareal())
breal.place(x=10, y=120, width=100, height=60)

bdolar = Button(tela1, text="dólar", font='Time 15', command=lambda:criar_telaeuro())
beuro.place(x=100, y=40, width=100, height=60)

def criar_telaeuro():
    return 

def criar_telareal():
    return 

tela1.mainloop()