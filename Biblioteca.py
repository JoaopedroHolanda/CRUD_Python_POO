import tkinter as tk
from tkinter import messagebox
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self, livro):
        for l in self.catalogo:
            if l.titulo == livro.titulo:
                messagebox.showinfo("Aviso", f"Livro {livro.titulo} já está no catálogo!")
                return
            elif l.id == livro.id:
                messagebox.showinfo("Aviso",f"O ID {livro.id} já tem um livro correspondente!")
                return
        messagebox.showinfo("Aviso",f'Livro {livro.titulo} adicionado ao catálogo!')
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        for m in self.membros:
            if m.nome == membro.nome:
                messagebox.showinfo("Aviso",f"Membro {membro.nome} com número {membro.numero} já está cadastrado!")
                return
            elif m.numero == membro.numero:
                messagebox.showinfo("Aviso",f"O número {membro.numero} já pussuí um membro correspondente!")
                return
        messagebox.showinfo("Aviso",f"Membro {membro.nome} cadastrado!")
        self.membros.append(membro)

    def emprestar_livro(self, livro, membro):
        if livro.status_emprestimo:
            membro.alugar_livro(livro)
            livro.emprestar_livro()
            messagebox.showinfo("Aviso",f"livro {livro.titulo} emprestado para {membro.nome}")
        else:
            messagebox.showinfo("Aviso","Livro não disponível para empréstimo!")
    
    def devolver_livro(self, livro, membro):
        membro.devolver_livro(livro)
        livro.devolver_livro()
        messagebox.showinfo("Aviso",f"Livro {livro.titulo} devolvido por {membro.nome}")
    
    def pesquisar_livro(self, entrada):
        for livro in self.catalogo:
            if entrada == livro.titulo or entrada == livro.autor or entrada == livro.id:
                messagebox.showinfo("Aviso",f"Livro encontrado! \n LIVRO: {livro.titulo} \n AUTOR: {livro.autor} \n ID: {livro.id}")
                
    def listar_livros(self):
        for livro in self.catalogo:
            messagebox.showinfo(livro.titulo)
            