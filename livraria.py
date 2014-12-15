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
        for colecao in self.carrinho.produtos:
            soma_colecao = reduce(r, map(m, colecao))
            soma = soma + soma_colecao -soma_colecao*(len(colecao) -1)*0.05
            soma = round(soma,2)
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
    
    def test_tres_livros_diferentes(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(2)
        self.assertEqual(126 - (126*0.1), self.livraria.finalizar_compra())

    def test_quatro_livros_diferentes(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(2)
        self.livraria.adicionar_livro_no_carrinho(3)
        self.assertEqual(42*4 - (42*4*0.15), self.livraria.finalizar_compra())

    def test_quatro_livros_diferentes(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(2)
        self.livraria.adicionar_livro_no_carrinho(3)
        self.livraria.adicionar_livro_no_carrinho(4)
        self.assertEqual(42*5 - (42*5*0.2), self.livraria.finalizar_compra())
    
    def test_dois_livros_diferentes2(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.assertEqual(159.6, self.livraria.finalizar_compra())

    def teste_dois_livros_diferentes3(self):
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.livraria.adicionar_livro_no_carrinho(0)
        self.livraria.adicionar_livro_no_carrinho(1)
        self.assertEqual(239.4, self.livraria.finalizar_compra())


if __name__ == '__main__':
    unittest.main()