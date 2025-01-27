import tkinter as tk
root=tk.Tk() #aqui que começamos a usar o tkinter

root.title("amazing") #root é a janela, nome da janela

label1=tk.Label(root, text="epic") #o root informa que o textino faz parte da root(janela), nome do textinho
label1.pack(pady=10) #tamanho da label

label2=tk.Label(root, text="awesome")
label2.pack(pady=10)

label3=tk.Label(root, text="cool")
label3.pack(pady=10)

root.mainloop() #fica aberta até eu fechar (loop)