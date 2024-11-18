import random

escolhas=[1, 2, 3]
jogador=(input("papel-1 tesoura-2 pedra-3 sair-4; sua escolha: "))
pc=random.choice(escolhas)

def vencer (jogador, pc):
    if jogador == pc:
        print("pc: ", pc)
        return("empate")
    elif jogador==3 and pc==2:
        print("pc: ", pc)
        return("você ganhou!!!1")
    elif jogador==1 and pc==3:
        print("pc: ", pc)
        return("você ganhou!!1")
    elif jogador==2 and pc==1:
        print("pc: ", pc)
        return("você ganhou!1")
    else:
        print("pc: ", pc)
        return("você perdeu:(...))")
    
while True:
    jogador=(input("papel-1 tesoura-2 pedra-3; sua escolha: "))
    if jogador<1 and jogador>4:
        print("inválido")
    if jogador==4:
        print("saiu do jogo...")
