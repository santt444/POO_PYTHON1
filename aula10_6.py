import os 
def clear():
    os.system("cls")
clear()

class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao  

    def eh_longo(self):
        return self.duracao > 120



meu_filme = Filme("Vingadores ultimato", 181)
print(f"Título: {meu_filme.titulo}")
print(f"Duração: {meu_filme.duracao} minutos")

if meu_filme.eh_longo():
    print("O filme é longo.")
else:
    print("O filme não é longo.")