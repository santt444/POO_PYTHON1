import os 
def clear():
    os.system("cls")
clear()

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade


produto1 = Produto("Caneta", 2.50, 100)

print(f"Produto: {produto1.nome}")
print(f"Preço: R$ {produto1.preco:.2f}")
print(f"Quantidade: {produto1.quantidade}")
print(f"Valor total em estoque: R$ {produto1.valor_total():.2f}")