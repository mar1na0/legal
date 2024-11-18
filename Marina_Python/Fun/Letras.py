frase=input("frase: ")
letra=input("letra :")

def Num_letras(frase):
    n = 0
    for letra_atual in frase:
        if letra==letra_atual:
            n+=1 #ou c = c+1
    print(n)

Num_letras(frase)