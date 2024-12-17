import random
jogos=["hollow Knight", "little nightmares", "half life", "red dead redemption", "inside", "limbo", "roblox", "minecraft", "portal", "doom", "team fortress", "left for dead", "call of duty", "counter strike", "halo"]
mangas=["my hero academia", "berserk", "vagabond", "assassination classroom", "oyasumi punpun", "tokyo ghoul", "hanako kun", "spy x family", "saiki k", "death note", "monster", "viland saga", "jujutsu kaisen", "sakamoto days"]

hp=10
def jogo(palavra, letra):
    global hp
    if letra in palavra: #complicar depois
        print("correto")
    else:
        print("errado")
        hp-=1

    
jogador=int(input("escolha um tema: jogos(1) ou mangás(2):"))
if jogador==1:
    palavra=random.choice(jogos)
elif jogador==2:
    palavra=random.choice(mangas)
else:
    print("inválido!")

while True:
    print(palavra) #tirar depois
    print("número de caractéres: ", len(palavra))
    letra=input("escolha uma letra: ")
    
    jogo(palavra, letra)
    print("hp:", hp)
