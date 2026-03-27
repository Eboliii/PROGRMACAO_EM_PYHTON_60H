import os
import shutil

with open('atividade.txt','r') as conteudo:
    c = conteudo.read()

    print(c)

os.mkdir('novo_diretório')
    

os.rename('teste.txt' , 'teste_rename.txt')
    
with os.scandir('diretorio') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')

arquivo_origem = 'texto.txt'
arquivo_destino = 'texto_copia.txt'

shutil.copy(arquivo_origem, arquivo_destino)
print('Arquivo ',arquivo_origem,' copiado com sucesso!')

arquivo_delete = 'delete.txt'

os.remove(arquivo_delete)
print('O arquivo ',arquivo_delete,' foi removido com sucesso.')
