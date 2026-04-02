import sqlite3

conn = sqlite3.connect('agencia.db')


cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS dados (
    nome TEXT,
    idade INTEGER,
    email TEXT,
    endereco TEXT,
    trabalho TEXT,
    graduacao TEXT
)
''')

print('--- ADICIONAR NOVO DADO---')



cursor.executemany('''
INSERT INTO dados (nome, idade, email, endereco, trabalho, graduacao) 
VALUES (?, ?, ?, ?, ?, ?)
''')


conn.commit()

print("--- Dados cadastrados com sucesso! ---\n")


print("Lista de Dados Cadastrados:")
cursor.execute('SELECT * FROM dados')


for linha in cursor.fetchall():
    print('Nome: ',linha[0],' | Idade: ',linha[1],' | Email: ',linha[2])
    print('Endereço: ',linha[3],' | Trabalho: ',linha[4],' | Graduação: ',linha[5])
    print("-----" * 15)


cursor.close()
conn.close()