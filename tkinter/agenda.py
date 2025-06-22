from tkinter import *
from tkinter import messagebox 
import random
from time import sleep

font_size=300000
screen_size='1500x700'

menu=Tk()
menu.title("UNO")
menu.geometry(screen_size)
menu.wm_resizable(width=False, height=False)

bcomecar=Button(menu, text="Começar", command=lambda:abrirtela())
bcomecar.place(width=100, height=100)
bcomecar.pack(anchor=CENTER, ipadx=50, ipady=30)

bfechar=Button(menu, text="Sair", command=lambda:fechar())
bfechar.place(width=100, height=100)
bfechar.pack(anchor=CENTER, ipadx=50, ipady=30)

def fechar():
    menu.destroy()

def abrirtela():
    menu.attributes("-alpha", 0.0)
    telauno=Tk()
    telauno.title("UNO")
    telauno.geometry(screen_size)
    telauno.wm_resizable(width=True, height=False)

    voce_frame=Frame(telauno)
    voce_frame.pack(side=BOTTOM, fill=X)

    adversario_frame=Frame(telauno)
    adversario_frame.pack(side=TOP, fill=X)

    jogo=Jogo(telauno, voce_frame, adversario_frame)
    telauno.after(100, jogo.comeco)

class Carta:
    def __init__(self, valor, cor):
        self.valor=valor
        self.cor=cor

    def __str__(self):	#ajuda
        return f"{self.valor} {self.cor}"

class Baralho:
    def __init__(self):
        self.baralho=[]
    
    def embaralhar(self):
        valores=["1", "2", "3", "4","5", "6", "7", "8", "9"]
        cores=["blue","red","yellow","green"]
        
        for i in range(100):
            for valor in valores:
                for cor in cores:
                    cartas=Carta(valor, cor)
                    self.baralho.append(cartas)
        
        random.shuffle(self.baralho)            
        
    def escolhercarta(self):
        primcarta=self.baralho[0]
        self.baralho.remove(primcarta)
        return primcarta
                
    def __str__(self):		#ajuda
        result = ""
        for carta in self.baralho:
            result = result + "|" + str(carta)
        return result
            
class Jogador:
    def __init__(self, ishuman, frame):
        self.mao=[]
        self.ishuman=ishuman 
        self.botoes=[]
        self.frame=frame

    def historico(self, texto):
        lhistorico=Label(self.frame, text=texto)
        lhistorico.place(width=60, height=20)
        lhistorico.pack(anchor=E, ipadx=100, ipady=30)

    def comprar(self, carta):
        self.mao.append(carta)
        
    def criarbotao(self, valor, cor, cartamesa, bcartamesa, funcao=()):    #função parâmetro, () tá lá só p/ n precisar definir ele qnd n precisa
        if self.ishuman==True:
            bcarta=Button(self.frame, text=valor, bg=cor, command=lambda:self.clicarb(valor, cor, cartamesa, bcartamesa, funcao), font=font_size)
            bcarta.pack(side=LEFT, ipadx=30, ipady=50, anchor=S)
            self.botoes.append(bcarta)
            return bcarta
        else:
            bcarta=Button(self.frame, bg="brown", font=font_size)
            bcarta.pack(side=LEFT, ipadx=30, ipady=50, anchor=N)
            self.botoes.append(bcarta)
            return bcarta
        
    def deletarbotao(self, pos):
        botao=self.botoes.pop(pos)
        botao.destroy()
    
    def checarcartas(self):
        return len(self.mao)
    
    def checarpos(self, pos):
        return self.mao[pos]
    
    def clicarb(self, valor, cor, cartamesa, bcartamesa, funcao):
        #print("valor=",valor," cor=",cor," mesa=",cartamesa, " ", hex(id(cartamesa)))
        for carta in self.mao:
            if carta.valor==valor and carta.cor==cor:
                if cartamesa.valor==carta.valor or cartamesa.cor==carta.cor:
                    self.deletarbotao(self.mao.index(carta))
                    self.mao.remove(carta)
                    
                    cartamesa.valor=carta.valor
                    cartamesa.cor=carta.cor
                    bcartamesa.config(text=cartamesa.valor, bg=cartamesa.cor)
                    funcao()
                    break
    
    def baixarc(self, cartamesa):
        if self.ishuman==True: 
            pass    #
        else:
            for carta in self.mao:
                if cartamesa.valor==carta.valor or cartamesa.cor==carta.cor:
                    self.deletarbotao(self.mao.index(carta))
                    self.mao.remove(carta)
                    return carta
            return None
    
    def __str__(self):
        result = ""
        for carta in self.mao:
            result = result + "|" + str(carta)
        return result

class Jogo:
    def __init__(self, root, voce_frame, adversario_frame):
        self.root=root
        self.voce_frame=voce_frame
        self.adversario_frame=adversario_frame

        self.cartamesa=Carta("c","v")
        self.voce=Jogador(True, voce_frame)
        self.adversario=Jogador(False, adversario_frame)
        self.baralho=Baralho()
        self.carta=Carta("c","v")
        self.botao=None
        self.bcartamesa=None
        self.texto=""
            
        self.bbaralho=Button(self.root, bg="brown", command=lambda:self.botao_baralho())
        self.bbaralho.place(x=1148, y=250, width=100, height=150)

    def botao_baralho(self):
        carta=self.baralho.escolhercarta()
        self.voce.comprar(carta)
        self.voce.criarbotao(carta.valor,carta.cor,self.cartamesa,self.bcartamesa,lambda:self.rodada(self.adversario))
        self.rodada(self.adversario)

    def rodada(self, jogador):
        if self.voce.checarcartas()==0:
            x=self.root.winfo_x() #pega a posição da tela
            y=self.root.winfo_y()
            
            telatrans=Toplevel(self.root)
            telatrans.geometry(f"{screen_size}+{x}+{y}") 
            telatrans.wm_resizable(width=True, height=False)
            telatrans.overrideredirect(True)  #remove as coisas de cima
            telatrans.attributes("-alpha", 0.7)
            telatrans.grab_set() #n deixa mais interagir

            messagebox.showinfo("Parabéns!", "Você venceu!", parent=telatrans)
            telatrans.destroy()
            self.root.destroy()

            menu.attributes("-alpha", 1)
            return

        carta=jogador.baixarc(self.cartamesa)
        
        if carta==None:
            carta=self.baralho.escolhercarta()
            jogador.comprar(carta)
            jogador.criarbotao(carta.valor,carta.cor,self.cartamesa,self.bcartamesa)
        else:
            self.cartamesa.valor=carta.valor
            self.cartamesa.cor=carta.cor
            self.bcartamesa.config(text=self.cartamesa.valor, bg=self.cartamesa.cor)

        if self.adversario.checarcartas()==0:
            x=self.root.winfo_x()
            y=self.root.winfo_y()
            
            telatrans=Toplevel(self.root)
            telatrans.geometry(f"{screen_size}+{x}+{y}") 
            telatrans.wm_resizable(width=True, height=False)
            telatrans.overrideredirect(True)
            telatrans.attributes("-alpha", 0.7)
            telatrans.grab_set()

            messagebox.showinfo(":(", "Você perdeu...", parent=telatrans)
            telatrans.destroy()
            self.root.destroy()

            menu.attributes("-alpha", 1)
            return
            
    def comeco(self):
        self.voce=Jogador(True, self.voce_frame)
        self.adversario=Jogador(False, self.adversario_frame)
        self.cartamesa=None
        self.baralho=Baralho()
        self.carta=None
        
        self.baralho.embaralhar()

        self.cartamesa=self.baralho.escolhercarta()
        self.bcartamesa=Button(self.root, text=self.cartamesa.valor, bg=self.cartamesa.cor, font=font_size)
        self.bcartamesa.place(x=600, y=250, width=100, height=150)
        
        for i in range(9):            
            self.carta=self.baralho.escolhercarta()
            self.adversario.comprar(self.carta)
            self.adversario.criarbotao(self.carta.valor,self.carta.cor,self.cartamesa,self.bcartamesa)

            self.carta=self.baralho.escolhercarta()
            self.voce.comprar(self.carta)
            self.voce.criarbotao(self.carta.valor,self.carta.cor,self.cartamesa,self.bcartamesa,lambda:self.rodada(self.adversario))

menu.mainloop()
