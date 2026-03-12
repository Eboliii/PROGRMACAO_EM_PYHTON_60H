quantidade_pessoas = int(input('Quantas pessoas?(máximo 3) '))
reserva = 0

if quantidade_pessoas == 1:
    reserva = [input('Digite o nome do titular: ') , int(input('Digite a idade do titular: '))]
elif quantidade_pessoas == 2:
    reserva = [input('Digite o nome do titular: ') , int(input('Digite a idade do titular: ')) , input('Digite o nome do primeiro dependende ') , int(input('Digite a idade do primeiro dependente: '))]
else: 
    reserva = [input('Digite o nome do titular: ') , int(input('Digite a idade do titular: ')) , input('Digite o nome do primeiro dependende ') , int(input('Digite a idade do primeiro dependente: ')) , input('Digite o nome do segundo dependende ') , int(input('Digite a idade do segundo dependente: '))]
    



quarto = [print('Simples R$', 100.00,' - 0') , print('Duplo R$',150.00,' - 1') , print('Luxo R$,',250.00,' - 2')]
escolha_quarto = int(input('Escolha um Quarto(0-1-2): '))



dias = int(input('Escolha a quantidade de dias: '))

valor_da_reserva = 0


if escolha_quarto == 0:
    valor_da_reserva = dias*(100.00*quantidade_pessoas)
    print('O Valor total da reserva ficou R$',valor_da_reserva,' Como deseja pagar?')
elif escolha_quarto == 1:
    valor_da_reserva = dias*(150.00*quantidade_pessoas)
    print('O Valor total da reserva ficou R$',valor_da_reserva,' Como deseja pagar?')
else: valor_da_reserva = dias*(250.00*quantidade_pessoas)
print('O Valor total da reserva ficou R$',valor_da_reserva,' Como deseja pagar?')
