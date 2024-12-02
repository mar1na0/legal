from time import sleep
sec=int(input("segundos "))
print("lançamento em: ")

while(sec>0):
    print(sec)
    sec-=1
    sleep(1) #faz o loop dormir por 1 sec

print("lançar...")

