import time
import tkinter as tk

class ClickSpeedGame: #classe
    def __init__(self, root):
        self.root=root  #self é um atributo vindo da classe
        root.title("jogo do clique rápido")

        self.score=0 #pontuação
        self.time_left=10 #tempo restante
        self.start=None
        
        self.timeleft=tk.Label(root, text=f"tempo restante: {self.time_left}s", font='Arial 14 bold')
        self.timeleft.pack()
        
        self.score=tk.Label(root, text=f"pontuação: {self.score}s", font='Arial 14 bold')
        self.score.pack()

        self.clickbutton=tk.Button(root, text='me clique!', font='Arial 14 bold', command=self.increase_score)
        self.score.pack()

        self.start_game()

    def increase_score(self):
        if self.time_left>0:
            self.score>=1