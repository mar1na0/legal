def criar_ficheiro():
    global ficheiro
    ficheiro=input("nome do ficheiro: ")
    texto=input("texto: ")

    try:
        with open (ficheiro, 'w') as ficheiro4:
            ficheiro4.write(texto)
            print("ficheiro criado com sucesso")
    except Exception as e:
    	print("erro ao criar ficheiro {e}")

def adicionar_texto():
    global ficheiro
    add=input("adicionar ao ficheiro: ")
    with open (ficheiro, 'a') as ficheiro4:
        ficheiro4.write('\n'+add)
        print("frase adicionada com succeso")

criar_ficheiro()
adicionar_texto()


