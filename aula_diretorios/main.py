import os
import shutil

with open('aula_diretorios/atividade.txt','r') as conteudo:
    c = conteudo.read()

    print(c)

os.mkdir('novo_diretório')
    

os.rename('aula_diretorios/diretorio' , 'aula_diretorios/cleiton')
    
with os.scandir('aula_diretorios/cleiton') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')

arquivo_origem = 'aula_diretorios/texto.txt'
arquivo_destino = 'aula_diretorios/texto_copia.txt'

shutil.copy(arquivo_origem, arquivo_destino)
print('Arquivo ',arquivo_origem,' copiado com sucesso!')

arquivo_delete = 'aula_diretorios/delete.txt'

os.remove(arquivo_delete)
print('O arquivo ',arquivo_delete,' foi removido com sucesso.')
