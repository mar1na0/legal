import random
import os
import platform
from time import sleep

jogos=["hollow Knight", "little nightmares", "half-life", "red dead redemption", "inside", "limbo", "roblox", "minecraft", "portal", "doom", "team fortress", "left for dead", "call of duty", "counter-strike", "halo", "celeste", "superliminal", "grand theft auto", "arkham asylum", "geometry dash", "super mario bros", "sonic & knuckles", "pac-man", "just dance", "guitar hero", "arkanoid", "pong", "space invaders", "pitfall", "donkey kong"]
mangas=["my hero academia", "berserk", "vagabond", "assassination classroom", "oyasumi punpun", "tokyo ghoul", "hanako-kun", "spy x family", "saiki k", "death note", "monster", "vinland saga", "jujutsu kaisen", "sakamoto days", "dorohedoro", "naruto", "dragon ball", "pet shop of horrors", "hunter x hunter", "one piece", "black clover", "bleach", "haikyuu", "fullmetal alchemist", "one punch man", "pluto", "slam dunk", "akira", "jojo's bizzare adventure"]
lista=[]
listaerros=[]
hp=7
forca=0
maxcaracteres=1
homemforca=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def capstonormal(letra):
    return letra.lower()

def checar_erro(palavra, letra, homemforca):
    global hp
    global forca
    global maxcaracteres
    if letra not in palavra and letra!="1" and letra not in listaerros and len(letra)==maxcaracteres:
        listaerros.append(letra)
        hp-=1
        if forca<6:
            forca+=1
    print(homemforca[forca])

def imprimir(palavra, lista):
    resultado=""
    for letra in palavra:
        if letra in lista or letra in {" ", "&", "-", "'"}:
            resultado=resultado+letra
        else:
            resultado=resultado+"_"
    print(resultado)
    return(resultado)    

def partida():
    global hp
    global maxcaracteres
    while True:
        resultado=imprimir(palavra,lista)
        if resultado == palavra:
            print("você venceu!!!!")
            break
        print("letras erradas:", listaerros)
        letra=input("escolha uma letra: \nadivinhar palavra(1)")
        letra=capstonormal(letra)
        if len(letra)>maxcaracteres:
            print("você só pode acertar uma letra de cada vez!")
            sleep(3)
        elif letra=="1":
            adivinha=input("adivinhar palavra: ")
            if adivinha==palavra:
                print("você venceu!! :)")
                print()
                sleep(3)
                break
            else:
                print("errado!")
                hp-=1
                forca+=1
                sleep(3)
        elif letra in listaerros:
            print("você já tentou acertar essa letra!")
            sleep(3)
        
        clear_console()
        checar_erro(palavra, letra, homemforca)
        lista.append(letra)
        if hp == 0:
            print("você perdeu... :(")
            print("a palavra era", palavra)
            print("")
            sleep(3)
            break

while True:
    lista=[]
    listaerros=[]
    hp=7
    forca=0
    print("Jogo da Forca")
    jogador=int(input("escolha um tema: jogos(1) ou mangás(2):"))
    print(homemforca[0])
    if jogador==1:
        palavra=random.choice(jogos)
    elif jogador==2:
        palavra=random.choice(mangas)
    else:
        print("inválido!")
    partida()
