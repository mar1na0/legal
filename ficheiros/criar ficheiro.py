def criar_ficheiro():
    ficheiro=input("nome do ficheiro: ")
    texto=input("texto: ")

    try:
        with open (ficheiro, 'w') as ficheiro4:
            ficheiro4.write(texto)
            print("ficheiro criado com sucesso")
    except Exception as e:
    	print("erro ao criar ficheirp")

criar_ficheiro()