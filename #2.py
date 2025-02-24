#2
import tkinter as tk
from tkinter import messagebox

# Função chamada quando um botão é clicado
def clica_botao(index):
    global jogador_atual, board, buttons
    # Verifica se a posição no tabuleiro está vazia
    if board[index] == '':
        # Atualiza o tabuleiro com o jogador atual
        board[index] = jogador_atual
        # Atualiza o texto do botão
        buttons[index].config(text=jogador_atual)
        # Verifica se há um vencedor
        if verifica_vencedor():
            messagebox.showinfo("Fim de Jogo", f"Jogador {jogador_atual} venceu!")
            reset()
        # Verifica se há um empate
        elif '' not in board:
            messagebox.showinfo("Fim de Jogo", "Empate!")
            reset()
        else:
            # Alterna o jogador atual
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Função que verifica se há um vencedor
def verifica_vencedor():
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for comb in combinacoes:
        # Verifica se todos os três elementos da combinação são iguais e não vazios
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != '':
            return True
    return False

# Função que reseta o jogo
def reset():
    global board, buttons, jogador_atual
    # Reseta o tabuleiro para vazio
    board = ['' for _ in range(9)]
    # Limpa o texto de todos os botões
    for button in buttons:
        button.config(text='')
    # Reseta o jogador atual para 'X'
    jogador_atual = 'X'

if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal do Tkinter
    root.title("Jogo do Galo")  # Define o título da janela

    jogador_atual = 'X'  # Define o jogador inicial como 'X'
    board = ['' for _ in range(9)]  # Inicializa o tabuleiro vazio
    buttons = []  # Lista para armazenar os botões

    # Cria a grade de botões 3x3
    for i in range(9):
        button = tk.Button(root, text='', font=('normal', 40), width=5, height=2, command=lambda i=i: clica_botao(i))
        button.grid(row=i//3, column=i%3)  # Posiciona o botão na grade
        buttons.append(button)  # Adiciona o botão à lista de botões

    root.mainloop()  # Inicia o loop principal do Tkinter
