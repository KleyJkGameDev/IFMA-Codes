from time import sleep
from random import randint

print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

lp = ["banana", "abacaxi", "acerola", "kiwi", "laranja", "limao", "tangerina", "morango", "uva", "pera", "maça"]
tp = randint(0, len(lp)-1) # recebe um numero (posição)
print(tp, len(lp))
palavra_secreta = lp[tp]
p = [" _ "*len(palavra_secreta)]
print(p)
print(palavra_secreta)
print(len(palavra_secreta))
    
vida = 6
print(f"Você tem {vida} vidas")
ps = list(palavra_secreta)

posi = 0
cond = True
acertou = False

while (not acertou and vida >= 0):
    chute = str(input("Digite um letra: "))

    for letra in palavra_secreta:
        #print(f"posi: {posi} e letra: {letra}")
        if(letra == chute):
            p[posi] = letra
            if(p == ps):
                print("Você ganhou")
                print(f"--> {p}")
                acertou = not acertou
        if(letra != chute):
            print(f"Você errou, {vida} vidas restantes")
            if(posi > 5):
                posi = 0
            vida = vida - 1
        if(posi > 5):
            posi = 0
        posi += 1
        

    print(f"--> {palavra_secreta}")
