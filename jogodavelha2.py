import tkinter as tk
from tkinter import messagebox

def clica_botao(index):
    global jogador_atual, board, buttons
    if board[index]=='':
        board[index]=jogador_atual
        buttons[index].config(text=jogador_atual)

        if verifica_vencedor():
            messagebox.showinfo("fim do jogo", f"jogador {jogador_atual} venceu")
            reset()
        elif ''not in board:
            messagebox.showinfo("fim do jogo", "empate")
            reset()
        else:
            jogador_atual='O'if jogador_atual == 'X' else 'X'

def verifica_vencedor():
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for comb in combinacoes:
        if board[comb[0]]==board[comb[1]]==board[comb[2]]!='':
            return True
        return False
    
def reset():
    global board, buttons, jogador_atual
    board=[''for _ in range(9)]
    for button in buttons:
        button.config(text=' ')
    jogador_atual='X'

if __name__=="__main__":
    root=tk.Tk()
    root.title("jogo da velha")

    jogador_atual='X'
    board=['' for _ in range(9)]
    buttons=[]

    for i in range(9):
        button=tk.Button(root, text='', font=('normal', 40), width=5, height=2, command=lambda i=i: clica_botao(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

root.mainloop()
