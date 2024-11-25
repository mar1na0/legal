from math import pi
numero=int(input("raio do círculo: "))
resultado=1

def area(numero, resultado):
    resultado=pi*numero**2
    return(resultado)

print("área do círculo: ", area(numero, resultado))