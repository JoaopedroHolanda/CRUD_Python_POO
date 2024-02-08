from tkinter import *
from Livro import *
from Membro import *
from Biblioteca import *

biblioteca = Biblioteca("Biblioteca Municipal")

def abrir_janela_membros():
    def enviar():
        membro = Membro(entrada_nome.get(), entrada_numero.get())
        biblioteca.adicionar_membro(membro)
        janela2.destroy()
        
    janela2 = Toplevel()
    janela2.title('Adicionar Membros')
    janela2.geometry("500x200")
    
    label_nome = Label(janela2, text="Nome do usuário:")
    entrada_nome = Entry(janela2, width=30)
    label_nome.grid(row=0, column=0, padx=10, pady=5)
    entrada_nome.grid(row=0, column=1, padx=10, pady=5)

    label_numero = Label(janela2, text="Número de identificação do usuário:")
    entrada_numero = Entry(janela2, width=30)
    label_numero.grid(row=1, column=0, padx=10, pady=5)
    entrada_numero.grid(row=1, column=1, padx=10, pady=5)
 
    botao_enviar = Button(janela2, text="Enviar", command=enviar, width=30, height=1)
    botao_enviar.grid(row=2, column=0, columnspan=2, pady=10)


def abrir_janela_livros():
    def enviar():
        livro = Livro(entrada_titulo.get(), entrada_autor.get(), entrada_id.get())
        biblioteca.adicionar_livro(livro)
        janela3.destroy()
     
    janela3 = Toplevel() 
    janela3.title("Adicionar Livros")
    janela3.geometry("300x200")
    
    label_titulo = Label(janela3, text="Título:")
    entrada_titulo = Entry(janela3, width=30)
    label_titulo.grid(row=0, column=0, padx=10, pady=5)
    entrada_titulo.grid(row=0, column=1, padx=10, pady=5) 

    label_autor = Label(janela3, text="Autor:")
    entrada_autor = Entry(janela3, width=30)
    label_autor.grid(row=1, column=0, padx=10, pady=5)
    entrada_autor.grid(row=1, column=1, padx=10, pady=5)

    label_id = Label(janela3, text="ID:")
    entrada_id = Entry(janela3, width=30)
    label_id.grid(row=2, column=0, padx=10, pady=5)
    entrada_id.grid(row=2, column=1, padx=10, pady=5)
 
    botao_enviar = Button(janela3, text="Enviar", command=enviar)
    botao_enviar.grid(row=3, column=0, columnspan=2, pady=10)


def abrir_janela_emprestimos():
    def enviar():
        for livro in biblioteca.catalogo:
            for membro in biblioteca.membros:
                if livro.titulo == entrada_livro.get() and membro.nome == entrada_membro.get():
                    biblioteca.emprestar_livro(livro, membro)
        janela4.destroy()
        
    janela4 = Toplevel()
    janela4.title("Emprestar livro")
    janela4.geometry("400x200")
    
    label_livro = Label(janela4, text="Título do livro:")
    entrada_livro = Entry(janela4, width=30)
    label_livro.grid(row=0, column=0, padx=10, pady=5)
    entrada_livro.grid(row=0, column=1, padx=10, pady=5)

    label_membro = Label(janela4, text="Nome do membro:")
    entrada_membro = Entry(janela4, width=30)
    label_membro.grid(row=1, column=0, padx=10, pady=5)
    entrada_membro.grid(row=1, column=1, padx=10, pady=5)

    botao = Button(janela4, text="Enviar", command=enviar)
    botao.grid(row=2, column=0, columnspan=2, pady=10)


def abrir_janela_devolucao():
    def enviar():
        for livro in biblioteca.catalogo:
            for membro in biblioteca.membros:
                if livro.titulo == entrada_livro.get() and membro.nome == entrada_membro.get():
                    biblioteca.devolver_livro(livro, membro)
        janela5.destroy()
        
    janela5 = Toplevel()
    janela5.title("Devolução de Livros")
    janela5.geometry("400x200")
    
    label_livro = Label(janela5, text="Título do livro:")
    entrada_livro = Entry(janela5, width=30)
    label_livro.grid(row=0, column=0, padx=10, pady=5)
    entrada_livro.grid(row=0, column=1, padx=10, pady=5)

    label_membro = Label(janela5, text="Nome do membro:")
    entrada_membro = Entry(janela5, width=30)
    label_membro.grid(row=1, column=0, padx=10, pady=5)
    entrada_membro.grid(row=1, column=1, padx=10, pady=5)

    botao = Button(janela5, text="Enviar", command=enviar)
    botao.grid(row=2, column=0, columnspan=2, pady=10)


def abrir_janela_pesquisa():
    def enviar():
        biblioteca.pesquisar_livro(entrada_pesquisa.get())
    janela6 = Toplevel()
    janela6.title("Pesquisa de livros")
    janela6.geometry("400x100")
    
    label_pesquisa = Label(janela6, text="Digite o Título, Autor ou ID:")
    entrada_pesquisa = Entry(janela6, width=30)
    label_pesquisa.grid(row=0, column=0, padx=10, pady=5)
    entrada_pesquisa.grid(row=0, column=1, padx=10, pady=5)

    botao = Button(janela6, text="Enviar", command=enviar)
    botao.grid(row=1, column=0, columnspan=2, pady=10)