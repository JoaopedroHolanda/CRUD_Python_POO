class Membro:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.livros_alugados = []
        self.historico_livros = []

    def alugar_livro(self, livro):
        self.historico_livros.append(livro)
        self.livros_alugados.append(livro)
    
    def devolver_livro(self, livro):
        self.livros_alugados.remove(livro)
