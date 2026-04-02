import tkinter as tk

def enviar_dados():
    print("----- Informações do Cliente -----")
    print('Nome: ',entry_nome.get())
    print('Idade: ',entry_idade.get())
    print('E-mail: ',entry_email.get())
    print('Endereço: ',entry_endereco.get())
    print('Celular: ',entry_celular.get())
    print('CEP: ',entry_cep.get())
    print('Cidade: ',entry_cidade.get())
    print('Cursos: ',entry_cursos.get())
    print('-----' * 15)

janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry('1700x750')
janela.iconbitmap('pesgo.ico')


container = tk.Frame(janela)
container.pack(expand=True)


tk.Label(container, text='Nome:').pack()
entry_nome = tk.Entry(container, width=50)
entry_nome.pack(pady=5)

tk.Label(container, text='Idade:').pack()
entry_idade = tk.Entry(container, width=50)
entry_idade.pack(pady=5)

tk.Label(container, text='E-mail:').pack()
entry_email = tk.Entry(container, width=50)
entry_email.pack(pady=5)

tk.Label(container, text='Endereço:').pack()
entry_endereco = tk.Entry(container, width=50)
entry_endereco.pack(pady=5)

tk.Label(container, text='Celular:').pack()
entry_celular = tk.Entry(container, width=50)
entry_celular.pack(pady=5)

tk.Label(container, text='Cep:').pack()
entry_cep = tk.Entry(container, width=50)
entry_cep.pack(pady=5)

tk.Label(container, text='Cidade:').pack()
entry_cidade = tk.Entry(container, width=50)
entry_cidade.pack(pady=5)

tk.Label(container, text='Curso:').pack()
entry_cursos = tk.Entry(container, width=50)
entry_cursos.pack(pady=5)

btn_enviar = tk.Button(container, text='CADASTRAR', bg = 'green', fg = 'white', command=enviar_dados, width=20)
btn_enviar.pack(pady=20)

janela.mainloop()