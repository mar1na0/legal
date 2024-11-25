min= 999
max= -999 #pode ser 0 nesse caso

for i in range(5):
    peso = int(input("peso: "))
    
    if peso > max:
        max = peso
    
    if peso < min:
        min = peso
    
print(max)
print(min)