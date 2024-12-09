from random import randint
lutadorA_hp=10
lutadorB_hp=10

def attack(lutadorA_hp, lutadorB_hp, attackA, attackB):
    attackA=randint(0,5)
    attackB=randint(0,5)
    
    lutadorB_hp-=(attackA)
    print("lutador_B perdeu ", attackA, "hp")
    
    lutadorA_hp-=(attackB)
    print("lutador_A perdeu ", attackB, "hp")
    return lutadorA_hp, lutadorB_hp

while True:
    attackA=randint(0,5)
    attackB=randint(0,5)
    lutadorA_hp, lutadorB_hp= attack(lutadorA_hp, lutadorB_hp, attackA, attackB)
    
    if lutadorA_hp <= 0 and lutadorB_hp>0:
        print("lutador A perdeu!")
        break
    elif lutadorB_hp <= 0 and lutadorA_hp>0:
        print("lutador B perdeu!")
        break
    elif lutadorA_hp <= 0 and lutadorB_hp<=0:
        print("empate!")
        break