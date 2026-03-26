import random

def ativ1():
    print('Atividade 1')
    nrandom = random.randint(5, 10)
    return nrandom



def ativ2():
    print('Atividade 2')
    x  =  random.randint(1,10)
    y  =  random.randint(1,10)
    z  =  random.randint(1,10)
    return x, y, z




def ativ3():
    print('Atividade 3')
    nrandom3 = [random.randint(10, 30) for _ in range(5)]
    return nrandom3 


def ativ4():
    print('Atividade 4')
    for i in range(10, 0, -1):
        return(i)
    return("Fogo!")


def ativ5():
    print('Atividade 5')
    numero = int(input("Digite um número inteiro positivo: "))
    soma = 0
    for i in range(2, numero + 1, 2):
        print(i)
        soma += i
    return('A soma dos números pares até ',numero,' é: ', soma)

