ficheiro=input("nome do ficheiro: ")
texto=input("texto: ")

with open (ficheiro, 'w') as ficheiro4:
    ficheiro4.write(texto)