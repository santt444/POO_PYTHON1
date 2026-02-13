class Aparelho:
    def __init__(self, nome, preço):
        self.nome = nome 
        self.preço = preço

    def exibir(self):
        print(f"Aparelho: {self.nome} \nPreço: R${self.preço:.2f}")

apa = Aparelho("Smartphone", 2500.00)
apa.exibir()