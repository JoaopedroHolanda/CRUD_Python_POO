from tkinter import *
from Interface import *

janela = Tk()
janela.title("Sistema Bibliotecário")
janela.geometry("600x250")
janela.resizable(False, False)
label = Label(janela,text=f"Sistema Bibliotecário da {biblioteca.nome}", font=("Arial", 12, "bold"), padx=10, pady=5)
label.pack()

botao_adicionar_livros = Button(janela, text="Adicionar livro", command=abrir_janela_livros)
botao_adicionar_livros.pack(pady=5)

botao_adicionar_membros = Button(janela, text="Adicionar membro", command=abrir_janela_membros)
botao_adicionar_membros.pack(pady=5)

botao_emprestar_livro = Button(janela, text="Emprestar livro", command=abrir_janela_emprestimos)
botao_emprestar_livro.pack(pady=5)

botao_devolver_livro = Button(janela, text="Devolver livro", command=abrir_janela_devolucao)
botao_devolver_livro.pack(pady=5)

botao_pesquisar_livros = Button(janela, text='Pesquisar livro', command=abrir_janela_pesquisa)
botao_pesquisar_livros.pack(pady=5)

janela.mainloop()
