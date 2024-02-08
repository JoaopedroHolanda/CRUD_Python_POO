class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_emprestimo = True
    
    def emprestar_livro(self):
        self.status_emprestimo = False
    
    def devolver_livro(self):
        self.status_emprestimo = True
