num = float(input('Digite um número: '))
if num > 0:
    print('Numero positivo')
elif num < 0:
    print('Numero negativo')
else: print('Numerero Zero')
print
idade = int(input('Digite sua Idade: '))
if idade >= 18:
    print('Pode votar')
else:
    print('Não Pode votar')

print('---'*15)

print('impar ou par')
imparoupar = 5
if imparoupar % 2 == 0:
    print('Par')
else:
    print('Impar')

print('---'*15)


num1 = int(input('Digite um Numero: '))
num2 = int(input('Digite outro Numero: '))
num3 = int(input('Digite o ultimo Numero: '))

if num1 == num2 == num3:
    print('Triangulo Equilatero')
elif num1 == num2 != num3:
    print('Triangulo isósceles')
elif num1 != num2 == num3:
    print('Triangulo isósceles')
else:
    print('Triangulo escaleno')

print('---'*15)

mult = int(input('Digite um número: '))
if mult % 5 == 0 and mult % 7 == 0:
    print('Número multiplo de 5 e 7')
else: print('Número não multiplo de 5 e 7')

print('---'*15)

num4 = int(input('Digite um Número: '))

if num4 > 0 and num4 < 10:
    print('Número positivo menor que 10')
elif num4 > 0 and num4 > 10:
    print('Número positivo maior que 10')
else:
    print('Número negativo')

print('---'*15)

div = int(input('Digite um número: '))
if div % 3 == 0 and mult % 5 == 0:
    print('Número divisível por 3 e 5')
elif div % 3 == 0 or mult % 5 == 0:
    print('Número divisível por 3 ou 5')
else: print('Número não divisível de 3 e 5')
