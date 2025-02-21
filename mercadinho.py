from meumodulo import Comprimentos
from meumodulo import carrinho
from meumodulo import finalizacao
import meumodulo as mm

nome = input('Para começarmos, digite o seu nome:')

produtos = ['Vagem','Leite','Ovos','Chocolate']
valores = [4.50,7.00,10.50,6.00]
dic_valores = {'Vagem':4.50,
               'Leite':7.00,
               'Ovos':10.50,
               'Chocolate':6.00}
valor_total = []

def mercado():
    mm.Comprimentos(nome)
    mm.carrinho(produtos,valores,dic_valores,valor_total)
    mm.finalizacao(nome)

m = mercado()
print(m)