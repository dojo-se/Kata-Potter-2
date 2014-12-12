#http://www.codingdojo.org/cgi-bin/index.pl?action=browse&id=KataPotter&revision=41

import unittest
from functools import reduce
from carrinho import Carrinho
from livro import Livro

class Livraria(object):
    
    def __init__(self):
        self.estante = list()
        self.carrinho = Carrinho()

    def adicionar_livro_no_carrinho(self, idx):
        self.carrinho.adicionar_produto(self.estante[idx])

    def adicionar_livro_na_estante(self, livro):
        self.estante.append(livro)

    def finalizar_compra(self):
        soma = 0
        m = lambda livro: livro.preco
        r = lambda soma, preco: soma + preco
        for lista in self.carrinho.produtos:
            soma = reduce(r, map(m, lista)) + soma
            soma = soma -soma*(len(lista) -1)*0.05
        return soma
        

class LivrariaTest(unittest.TestCase):
    def setUp(self):
        self.livraria = Livraria()
        self.livraria.adicionar_livro_na_estante(Livro("Harry livro 1", 42))
        self.livraria.adicionar_livro_na_estante(Livro("Harry livro 2", 42))
        self.livraria.adicionar_livro_na_estante(Livro("Harry livro 3", 42))
        self.livraria.adicionar_livro_na_estante(Livro("Harry livro 4", 42))
        self.livraria.adicionar_livro_na_estante(Livro("Harry livro 5", 42))


    def test_vazio(self):
        self.assertEqual(0, self.livraria.finalizar_compra())
    
    def test_apenas_um_livro(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.assertEqual(42, self.livraria.finalizar_compra())

    def test_dois_livros_iguais(self):
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.assertEqual(42*2, self.livraria.finalizar_compra())

    def test_dois_livros_diferentes(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.assertEqual(84 - (84*0.05), self.livraria.finalizar_compra())
    
    def test_dois_livros_diferentes2(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.assertEqual((84 - (84*0.05)*2), self.livraria.finalizar_compra())


if __name__ == '__main__':
    unittest.main()