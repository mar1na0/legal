import random
jogos=["hollow Knight", "little nightmares", "half-life", "red dead redemption", "inside", "limbo", "roblox", "minecraft", "portal", "doom", "team fortress", "left for dead", "call of duty", "counter strike", "halo", "celeste", "superliminal", "grand theft auto", "arkham asylum", "geometry dash", "super mario bros", "sonic & knuckles", "pac-man", "just dance", "guitar hero", "arkanoid", "pong", "space invaders", "pitfall", "donkey kong"]
mangas=["my hero academia", "berserk", "vagabond", "assassination classroom", "oyasumi punpun", "tokyo ghoul", "hanako kun", "spy x family", "saiki k", "death note", "monster", "vinland saga", "jujutsu kaisen", "sakamoto days", "dorohedoro", "naruto", "dragon ball", "pet shop of horrors", "hunter x hunter", "one piece", "black clover", "bleach", "haikyuu", "fullmetal alchemist", "one punch man", "pluto", "slam dunk", "akira", "jojo's bizzare adventure"]
lista=[]
listaerros=[]
hp=5

def jogo(palavra, letra):
    global hp
    if letra not in palavra:
        listaerros.append(letra)
        hp-=1

def imprimir(palavra, lista):
    resultado=""
    for letra in palavra:
        if letra in lista:
            resultado=resultado+letra
        elif letra == " ":
            resultado=resultado+" "
        elif letra == "-":
            resultado=resultado+"-"
        else:
            resultado=resultado+"_"
    print(resultado)
    return(resultado)
    
def partida():
    while True:
        resultado=imprimir(palavra,lista)
        if resultado == palavra:
            print("você venceu!!!!")
            break
        print("letras erradas:", listaerros)
        letra=input("escolha uma letra: ")
        lista.append(letra)
    
        jogo(palavra, letra)
        print("hp:", hp)
        if hp == 0:
            print("você perdeu... :(")
            print(palavra)
            break

while True:
    lista=[]
    listaerros=[]
    hp=5
    jogador=int(input("escolha um tema: jogos(1) ou mangás(2):"))
    if jogador==1:
        palavra=random.choice(jogos)
    elif jogador==2:
        palavra=random.choice(mangas)
    else:
        print("inválido!")
    partida()
