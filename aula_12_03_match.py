numero = float(input('Digite um Número: '))
match numero:
    case x if x % 2 == 0:
        print('Número digitado é par')
    case _: print('Número digitado impar')

pos_neg = float(input('Digite um Número: '))
match pos_neg:
    case x if x > 0:
        print('Número Positivo')
    case x if x == 0:
        print('Número digitado é zero')
    case _: print('Número Negativo')

digito = input('Digite seu nome: ')

match digito:
    case "":
        print('String Vazia')
    case _: print(digito)

maior_ou_menor = float(input('Digite um Número: '))

match maior_ou_menor:
    case x if x > 10:
        print('Maior que 10')
    case x if x < 10:
        print('Menor que 10')
    case _:print('Número digitado = ', maior_ou_menor)

idade = int(input('Digite sua Idade: '))

match idade:
    case x if x <= 12:
        print('Criança')
    case x if x <= 17:
        print('Adolescente')
    case x if x <= 35:
        print('Jovem')
    case x if x > 35 < 64:
        print('Adulto')
    case _: print('Idoso')

