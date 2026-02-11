import os 
def clear():
    os.system("cls")
clear()
# criando uma classe, molde que cria,instancia e cria objeto
# objeto recebe atributos (caracteristicas) e metodos (ação)
# self representa a instancia atual do objeto

# criando uma classe
class Pessoa:
 # criando o método construtor( É executado quando criamos o objeto)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

 # Método para mostrar os dados
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
        print(f"Eu tenho {self.idade} anos")

# criar um objeto (uma pessoa)
p1 = Pessoa("Santt",17 )

# chamar o metodo 
p1.apresentar()
#teste 123

