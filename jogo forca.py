import random
import os
import platform
from time import sleep

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

jogos=["hollow Knight", "little nightmares", "half-life", "red dead redemption", "inside", "limbo", "roblox", "minecraft", "portal", "doom", "team fortress", "left for dead", "call of duty", "counter-strike", "halo", "celeste", "superliminal", "grand theft auto", "arkham asylum", "geometry dash", "super mario bros", "sonic & knuckles", "pac-man", "just dance", "guitar hero", "arkanoid", "pong", "space invaders", "pitfall", "donkey kong"]
mangas=["my hero academia", "berserk", "vagabond", "assassination classroom", "oyasumi punpun", "tokyo ghoul", "hanako-kun", "spy x family", "saiki k", "death note", "monster", "vinland saga", "jujutsu kaisen", "sakamoto days", "dorohedoro", "naruto", "dragon ball", "pet shop of horrors", "hunter x hunter", "one piece", "black clover", "bleach", "haikyuu", "fullmetal alchemist", "one punch man", "pluto", "slam dunk", "akira", "jojo's bizzare adventure"]
lista=[]
listaerros=[]
hp=7
forca=0
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


def jogo(palavra, letra, homemforca):
    global hp
    global forca
    if letra not in palavra and letra!="1" and letra not in listaerros:
        listaerros.append(letra)
        hp-=1
        if forca<6:
            forca+=1
    print(homemforca[forca])

def imprimir(palavra, lista):
    resultado=""
    for letra in palavra:
        if letra in lista:
            resultado=resultado+letra
        elif letra == " ":
            resultado=resultado+" "
        elif letra == "&":
            resultado=resultado+"&"
        elif letra == "-":
            resultado=resultado+"-"
        elif letra == "'":
            resultado=resultado+"'"
        else:
            resultado=resultado+"_"
    print(resultado)
    return(resultado)    

def partida():
    global hp
    global forca
    while True:
        resultado=imprimir(palavra,lista)
        if resultado == palavra:
            print("você venceu!!!!")
            break
        print("letras erradas:", listaerros)
        letra=input("escolha uma letra: \nadivinhar palavra(1)")
        if letra=="1":
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
        if letra in listaerros:
            print("você já tentou acertar essa letra!")
            sleep(3)
        clear_console()

        lista.append(letra)
        jogo(palavra, letra, homemforca)
        #print("hp:", hp)
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
