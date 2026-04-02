import tkinter as tk

def mostrar():
    dado = input_1.get()
    texto2.config(text = dado)

janela = tk.Tk()
janela.geometry('800x600')
janela.configure(bg = 'white')
janela.iconbitmap('pesgo.ico')

# tk.Label(janela,text = 'ISSO É UM TESTE...').pack()
texto = tk.Label(janela, text = 'Digite Algo', font = ('arial', 25),  bg = 'white')
texto.pack(pady = 80)

input_1 = tk.Entry(janela, font = ('arial', 20), bg = 'white')
input_1.pack()

btn = tk.Button(janela, text = 'Buscar', font =('arial', 15), bg = 'white', command = mostrar)
btn.pack(pady = 65)

texto2 = tk.Label(janela, text = 'Mostrar', font = ('arial',25), bg = 'white')
texto2.pack(pady = 20)

janela.mainloop()
