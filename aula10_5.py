import os 
def clear():
    os.system("cls")
clear()

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

    def eh_longo(self):
        return self.paginas > 300



meu_livro = Livro("Dom Casmurro", "Machado de Assis", 320)
meu_livro.detalhes()

if meu_livro.eh_longo():
    print("O livro é longo")
else:
    print("O livro não é longo")