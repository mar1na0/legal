import random
escolhas=[1, 2, 3]

def vencer (jogador, pc):
    #print("pc: ", pc)
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
    pc=random.choice(escolhas)
    jogador= int(input("papel-1 tesoura-2 pedra-3 sair-4; sua escolha: "))
    if jogador<1 or jogador>4:
        print("inválido")
    if jogador==4:
        print("saiu do jogo...")
    else:
        print(vencer(jogador, pc))

vencer(pc,jogador)