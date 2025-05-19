from tkinter import *
import random
from time import sleep

tela1=Tk()
tela1.title("UNO")
tela1.geometry('1400x750')
tela1.wm_resizable(width=False, height=False)

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
        
    def comprar(self, carta):
        self.mao.append(carta)
    
    def checarcartas(self):
        return len(self.mao)
    
    def baixarc(self, cartamesa):
        if self.ishuman==True: 
            pass	#termina na aula
        else:
            for carta in self.mao:
                
                if cartamesa.valor==carta.valor or cartamesa.cor==carta.cor:
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
        self.voce=Jogador("Você", False) ##
        self.adversario=Jogador("Pc", False)
        self.baralho=Baralho()
    
    def rodada(self, jogador):
        print(jogador)
        print("")
        carta=jogador.baixarc(self.cartamesa)
        if carta==None:
            jogador.comprar(self.baralho.escolhercarta())
        else:
            self.cartamesa=carta
            
    def comeco(self):
        self.voce=Jogador("Você", False) ##
        self.adversario=Jogador("Pc", False)
        self.cartamesa=None
        self.baralho=Baralho()
        
        self.baralho.embaralhar()
        
        for i in range(9):
            self.voce.comprar(self.baralho.escolhercarta())
            self.adversario.comprar(self.baralho.escolhercarta())
        self.cartamesa=self.baralho.escolhercarta()
        
        print(self.baralho)
        print(self.cartamesa)
        #print(self.voce)
        #print(self.adversario)
        
        while True:
            self.rodada(self.voce)
            if self.voce.checarcartas()==0:
                print(self.voce.nome)
                break
            self.rodada(self.adversario)
            if self.adversario.checarcartas()==0:
                print(self.adversario.nome)
                break
    
jogo=Jogo()
jogo.comeco()
#cartamesa=jogo.cartamesa

#########   UI  ######### 

bcartamesa=Button(tela1, text=jogo.cartamesa.valor, bg=jogo.cartamesa.cor)
bcartamesa.place(x=40, y=20, width=200, height=160)

bbaralho=Button(tela1, bg="brown")
bbaralho.place(x=240, y=20, width=200, height=160)

tela1.mainloop()
