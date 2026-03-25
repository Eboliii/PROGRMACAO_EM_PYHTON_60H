print('Exerc 1:')
print('--->')
def exerc1(num1):
    if num1 % 2 == 0:
        print("par") 
    else: print("ímpar")

num1 = int(input('Digite um Número: '))
exerc1(num1)
print('-----'*15)
print('Exerc 2:')
print('--->')

def multi(n1,n2,n3,multiplicando):
    multiplicando = n1 * n2 * n3
    print(multiplicando)
    
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
multi(n1,n2,n3,multiplicando=0)

print('-----'*15)
print('Exerc 3:')
print('--->')

def elevar_numero(base, expoente):
    """Calcula a potência de um número."""
    return base ** expoente

resultado = elevar_numero(2, 3)
print(f"O resultado é: {resultado}")

print('-----'*15)
print('Exerc 4:')
print('--->')

def verificar_idade():
    entrada = input("Digite sua idade: ")

    try:
        idade = int(entrada)
        if idade >= 18:
            print('Você é maior de idade')
        else: print('Menor de idade')
    except ValueError:
        print("Por favor, digite um número válido.")

verificar_idade()

print('-----'*15)
print('Exerc 5:')
print('--->')

def idade_verify():
    ano_nasc = int(input('Digite ano que você nasceu: '))
    ano_atual = 2026
    idade = ano_atual - ano_nasc
    print(idade)

idade_verify()
