from tkinter import *
from tkinter import messagebox

Br='#affffff'
Az='#364a85'
Ve='#b53128'
AM='#ffef08'

tela1=Tk()
tela1.title("awesome")
tela1.geometry('380x500+500+100')
tela1.wm_resizable(width=False, height=False)

##parte de cima
partecima=Label(tela1, text="agenda", bg=Ve, fg=AM, font='Time 20 bold', anchor='w') #anchor coloca pro lado
partecima.place(x=0, y=0, width=380, height=50)

#nome
lnome=Label(tela1, text="nome", font='Time 10', anchor='w') #anchor coloca pro lado
lnome.place(x=10, y=70, width=60, height=20)
input_nome=Entry(tela1, font='Time 10')
input_nome.place(x=100, y=70, width=250, height=20)

#celular
lcelular=Label(tela1, text="celular", font='Time 10', anchor='w')
lcelular.place(x=10, y=110, width=60, height=20)
input_celular=Entry(tela1, font='Time 10')
input_celular.place(x=100, y=110, width=250, height=20)

#endereço
lendereco=Label(tela1, text="endereço", font='Time 10', anchor='w')
lendereco.place(x=10, y=150, width=60, height=20)
input_endereco=Entry(tela1, font='Time 10')
input_endereco.place(x=100, y=150, width=250, height=20)

#estado
lestado=Label(tela1, text="estado", font='Time 10', anchor='w')
lestado.place(x=10, y=190, width=60, height=20)
input_estado=Entry(tela1, font='Time 10')
input_estado.place(x=100, y=190, width=250, height=20)

#país
lpais=Label(tela1, text="país", font='Time 10', anchor='w')
lpais.place(x=10, y=230, width=60, height=20)
input_pais=Entry(tela1, font='Time 10')
input_pais.place(x=100, y=230, width=250, height=20)

#email
lemail=Label(tela1, text="email", font='Time 10', anchor='w')
lemail.place(x=10, y=270, width=60, height=20)
input_email=Entry(tela1, font='Time 10')
input_email.place(x=100, y=270, width=250, height=20)

def add():
    nome=input_nome.get
    celular=input_celular.get
    endereco=input_endereco.get
    estado=input_estado.get
    pais=input_pais.get
    email=input_email.get

    with open ('agenda.txt', 'a') as ficheiro:
        ficheiro.write('nome= '+nome, '\ncelular= '+celular, '\nendereco= '+endereco, '\nestado= '+estado, '\npais= '+pais, '\nemail'+email)

    messagebox.showinfo('Tela 1', 'escrito com sucesso')

    input_nome.delete('0', 'end') #0- é clicado p/ apagar, end é p/ loop
    input_celular.delete('0', 'end')
    input_endereco.delete('0', 'end')
    input_estado.delete('0', 'end')
    input_pais.delete('0', 'end')
    input_email.delete('0', 'end')

def procurar():
    nome=input_nome.get()

    #with open('agenda.txt', 'r') as arquivo:
       # for linha in arquivo:
            #if nome in linha:
               # a_celu

tela1.mainloop()
