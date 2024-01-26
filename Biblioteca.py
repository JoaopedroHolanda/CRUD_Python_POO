class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

class Usuario:
    def __init__(self,nome,numero_identificacao):
        self.nome =nome
        self.numero_identificacao = numero_identificacao
        self.livrosEmprestados = []

    def alugarLivro(self,livro):
        self.livrosEmprestados.append(livro)

    def devolverLivro(self,livro):
        self.livrosEmprestados.remove(livro)
    
    def verificarEmprestimos(self):
        print(f" \n LIVROS DE {self.nome}:")
        for livro in self.livrosEmprestados:
            print(livro.titulo)


class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.listaLivros = []

    def adicionarLivro(self,Livro):
        self.listaLivros.append(Livro)
        print(f"Livro {Livro.titulo} adicionado!")

    def removerLivro(self,livro):
        self.listaLivros.remove(livro)
        print(f"Livro {Livro.titulo} removido!")

    def alugarLivro(self, usuario, livro):
        if livro in self.listaLivros:
            usuario.alugarLivro(livro)
            self.listaLivros.remove(livro)
            print(f"Livro {livro.titulo} emprestado para {usuario.nome}")
        else:
            print(f"O livro {livro.titulo} não está disponível para empréstimo.")

    def devolverLivro(self, usuario, livro):
        usuario.devolverLivro(livro)
        self.listaLivros.append(livro)
        print(f"Livro {livro.titulo} devolvido por {usuario.nome}")

    def verificarLivrosDisponiveis(self):
        print(f"\n LISTA DE LIVROS DISPONÍVEIS: ")
        for livro in self.listaLivros:
            print(livro.titulo)



biblioteca = Biblioteca("Biblioteca Municipal")

    
livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro2 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
livro3 = Livro("Orgulho e Preconceito", "Jane Austen", 1813)

biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro3)

    
usuario1 = Usuario("João", 123)
usuario2 = Usuario("Maria", 456)

    
biblioteca.alugarLivro(usuario1, livro1)
biblioteca.alugarLivro(usuario2, livro2)
biblioteca.alugarLivro(usuario1, livro3)

   
usuario1.verificarEmprestimos()
usuario2.verificarEmprestimos()

    
biblioteca.devolverLivro(usuario1, livro1)
biblioteca.devolverLivro(usuario2, livro2)

    
usuario1.verificarEmprestimos()
usuario2.verificarEmprestimos()

biblioteca.verificarLivrosDisponiveis()



