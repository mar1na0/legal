import tkinter as tk
root=tk.Tk() #aqui que começamos a usar o tkinter

root.title("amazing") #root é a janela, nome da janela

label1=tk.Label(root, text="epic", fg="white", bg="black") #o root informa que o textino faz parte da root(janela), nome do textinho
label1.pack(pady=10) #tamanho da label

label2=tk.Label(root, text="awesome", fg="yellow", bg="red")
label2.pack(pady=10)

label3=tk.Label(root, text="cool", fg="pink", bg="green")
label3.pack(pady=10)

def mudar_texto():
    button.config(text="parabéns!")

button = tk.Button(root, text="me clique!", command=mudar_texto)
button.pack(pady=10)

def mudar_cor():
    button2.config(text="wow!", bg="black", fg="red")

button2 = tk.Button(root, text="mudar cor", command=mudar_cor)
button2.pack(pady=10)

root.mainloop() #fica aberta até eu fechar (loop)