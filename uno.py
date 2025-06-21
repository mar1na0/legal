from tkinter import *
import random
from time import sleep

font_size=300000

tela1=Tk()
tela1.title("UNO")
tela1.geometry('1500x700')
tela1.wm_resizable(width=True, height=False)

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
    def __init__(self, nome, ishuman):
        self.mao=[]
        self.nome=nome
        self.ishuman=ishuman 
        self.botoes=[]
        
    def comprar(self, carta):
        self.mao.append(carta)
        
    def criarbotao(self, valor, cor, cartamesa, bcartamesa, funcao=()):    #função parâmetro, () tá lá só p/ n precisar definir ele qnd n precisa
        if self.ishuman==True:
            bcarta=Button(voce_frame, text=valor, bg=cor, command=lambda:self.clicarb(valor, cor, cartamesa, bcartamesa, funcao), font=font_size)
            bcarta.pack(side=LEFT, ipadx=30, ipady=50, anchor=S)
            self.botoes.append(bcarta)
            return bcarta
        else:
            bcarta=Button(adversario_frame, bg="brown", font=font_size)
            bcarta.pack(side=LEFT, ipadx=30, ipady=50, anchor=N)
            self.botoes.append(bcarta)
            return bcarta
        
    def deletarbotao(self, pos):
        botao=self.botoes[pos]
        self.botoes.pop(pos)
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
            pass
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
    def __init__(self):
        self.cartamesa=Carta("c","v")
        self.voce=Jogador("Você", True)
        self.adversario=Jogador("Pc", False)
        self.baralho=Baralho()
        self.carta=Carta("c","v")
        self.botao=None
        self.bcartamesa=None
            
        self.bbaralho=Button(tela1, bg="brown", command=lambda:self.botao_baralho())
        self.bbaralho.place(x=1148, y=250, width=100, height=150)

    def botao_baralho(self):
        carta=self.baralho.escolhercarta()
        self.voce.comprar(carta)
        self.voce.criarbotao(carta.valor,carta.cor,self.cartamesa,self.bcartamesa,lambda:self.rodada(self.adversario))
        self.rodada(self.adversario)

    def rodada(self, jogador):
        if self.voce.checarcartas()==0:
            print("venceu")
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
            print("perdeu")
            return
            
    def comeco(self):
        self.voce=Jogador("Você", True) ##
        self.adversario=Jogador("Pc", False)
        self.cartamesa=None
        self.baralho=Baralho()
        self.carta=None
        
        self.baralho.embaralhar()

        self.cartamesa=self.baralho.escolhercarta()
        self.bcartamesa=Button(tela1, text=self.cartamesa.valor, bg=self.cartamesa.cor, font=font_size)
        self.bcartamesa.place(x=600, y=250, width=100, height=150)
        
        for i in range(9):            
            self.carta=self.baralho.escolhercarta()
            self.adversario.comprar(self.carta)
            self.adversario.criarbotao(self.carta.valor,self.carta.cor,self.cartamesa,self.bcartamesa)

            self.carta=self.baralho.escolhercarta()
            self.voce.comprar(self.carta)
            self.voce.criarbotao(self.carta.valor,self.carta.cor,self.cartamesa,self.bcartamesa,lambda:self.rodada(self.adversario))

jogo=Jogo()

voce_frame=Frame(tela1)
voce_frame.pack(side=BOTTOM,fill=X)
adversario_frame=Frame(tela1)
adversario_frame.pack(side=TOP,fill=X)

tela1.after(100, jogo.comeco)   #ajuda

tela1.mainloop()
