while True:
    print('Criando um Úsuario')
    usu = input('Digite seu Úsuario: ')
    senha = int(input('Digite sua senha: '))
    senha2 = int(input('Confirme sua senha: '))
    if senha != senha2:
        print('Senha Incorreta')
        senha2 = int(input('Confirme sua senha: '))

    print('-----'*20)

    print('Acessando a Conta')

    auten = input('Digite o Úsuario: ')
    if auten == usu:
            print('Úsuario Correto')
    else: print('Úsuario Incorreto')

    for tentativas in range(3):
        auten_senha = int(input('Digite a Senha: '))
        if auten_senha == senha:
            print('Login Efetuado')
        


        print('-----'*20)
        print('Conta Acessada Bem-Vindo', usu)
        alunos = ['','Aluno1','Aluno2','Aluno3']
        media_aluno1 = 0
        media_aluno2 = 0
        media_aluno3 = 0
        
        pergunta = input('Desejar Digitar nota dos alunos? ')
        while pergunta == "sim":
            aluno = int(input('Qual aluno deseja escolher Aluno1, Aluno2 ou Aluno3? '))
            if aluno == 1:
                nota1_aluno1 = float(input('Digite a primeira nota: '))
                nota2_aluno1 = float(input('Digite a segunda nota: '))
                nota3_aluno1 = float(input('Digite a terceira nota: '))
                media_aluno1 = (nota1_aluno1 + nota2_aluno1 + nota3_aluno1) / 3
                print(media_aluno1)
                pergunta = input('Desejar Digitar nota dos alunos? ')
                if pergunta != "sim":
                    breakpoint
                elif pergunta == 'sim': 
                    aluno = int(input('Qual aluno deseja escolher Aluno1, Aluno2 ou Aluno3? '))
                elif aluno == 2:
                    nota1_aluno2 = float(input('Digite a primeira nota: '))
                    nota2_aluno2 = float(input('Digite a segunda nota: '))
                    nota3_aluno2 = float(input('Digite a terceira nota: '))
                    media_aluno2 = (nota1_aluno2 + nota2_aluno2 + nota3_aluno2) / 3
                    print(media_aluno2)
                    pergunta = input('Desejar Digitar nota dos alunos? ')
                    if pergunta != "sim":
                            breakpoint
                    elif pergunta == 'sim': 
                            aluno = int(input('Qual aluno deseja escolher Aluno1, Aluno2 ou Aluno3? '))
                elif aluno == 3:
                        nota1_aluno3 = float(input('Digite a primeira nota: '))
                        nota2_aluno3 = float(input('Digite a segunda nota: '))
                        nota3_aluno3 = float(input('Digite a terceira nota: '))
                        media_aluno3 = (nota1_aluno3 + nota2_aluno3 + nota3_aluno3) / 3
                        print(media_aluno3)
            elif aluno == 2:
                nota1_aluno2 = float(input('Digite a primeira nota: '))
                nota2_aluno2 = float(input('Digite a segunda nota: '))
                nota3_aluno2 = float(input('Digite a terceira nota: '))
                media_aluno2 = (nota1_aluno2 + nota2_aluno2 + nota3_aluno2) / 3
                print(media_aluno2)
                pergunta = input('Desejar Digitar nota dos alunos? ')
                if pergunta != "sim":
                    breakpoint
                elif pergunta == 'sim': 
                    aluno = int(input('Qual aluno deseja escolher Aluno1, Aluno2 ou Aluno3? '))
            elif aluno == 3:
                nota1_aluno3 = float(input('Digite a primeira nota: '))
                nota2_aluno3 = float(input('Digite a segunda nota: '))
                nota3_aluno3 = float(input('Digite a terceira nota: '))
                media_aluno3 = (nota1_aluno3 + nota2_aluno3 + nota3_aluno3) / 3
                print(media_aluno3)

            print(f'''
            Média Aluno1: {media_aluno1}
            Média Aluno2: {media_aluno2}
            Média Aluno3: {media_aluno3}
''')



        sair = input('Deseja sair? ')
        if sair == 'sim':
            break


    else:print('Conta Bloqueada')
