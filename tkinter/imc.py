from tkinter import *
import math

tela1=Tk()
tela1.title("calculadora de imc")
tela1.geometry('350x200')
tela1.wm_resizable(width=False, height=False)

laltura=Label(tela1, text="altura", font='Time 10', anchor='w')
laltura.place(x=10, y=30, width=60, height=20)
input_altura=Entry(tela1, font='Time 10')
input_altura.place(x=50, y=30, width=250, height=20)

lpeso=Label(tela1, text="peso", font='Time 10', anchor='w')
lpeso.place(x=10, y=70, width=60, height=20)
input_peso=Entry(tela1, font='Time 10')
input_peso.place(x=50, y=70, width=250, height=20)

button1 = Button(tela1, text="calcular imc", command=lambda:calcular())
button1.place(x=50, y=100, width=70, height=40)

limc=Label(tela1, text="IMC=", font='Time 10', anchor='w')
limc.place(x=50, y=160, width=60, height=20)

limc0=Label(tela1, text="???", font='Time 10', anchor='w')
limc0.place(x=80, y=160, width=50, height=20)

def calcular():
    altura=int(input_altura.get())/100
    peso=int(input_peso.get())
    imc= peso/altura**2
    limc0.config(text=imc, fg='green')

    if imc<18 or imc>25:
        limc0.config(fg='red')

tela1.mainloop()
