try:
    numero = int(input('Digite um número'))
except ValueError:
    print('Dado digitado não é um número')

print('-----'*15)

try:
    dado1 = float(input('Digite o Primeiro número: '))
    dado2 = float(input('Por quanto deseja dividir ? '))
    resultado = dado1/dado2
    print(resultado)
except ZeroDivisionError as erro:
    print(erro)

print('-----'*15)

try:
    l = ['','SILVIA S13', 'SILVIA S14', 'SILVIA S15']
    visualizer = int(input('Qual indice deseja ver? '))
    print(l[visualizer])
except IndexError:
    print('Indice Digitado não existe')