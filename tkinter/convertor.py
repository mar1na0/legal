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

leuro=Label(tela1, text="Euro", font='Time 10', anchor='w')
leuro.place(x=10, y=30, width=60, height=20)
input_euro=Entry(tela1, font='Time 10')
input_euro.place(x=50, y=30, width=250, height=20)

lreal=Label(tela1, text="Real:", font='Time 10', anchor='w')
lreal.place(x=10, y=70, width=60, height=20)

lresultado=Label(tela1, text="???", font='Time 10', anchor='w')
lresultado.place(x=50, y=70, width=60, height=20)

button1 = Button(tela1, text="converter", command=lambda:calcular())
button1.place(x=50, y=100, width=70, height=40)


def calcular():
    euro=int(input_euro.get())
    real=float(conversao['EURBRL']['bid'])

    resultado=euro*real

    lresultado.config(text=resultado)

tela1.mainloop()