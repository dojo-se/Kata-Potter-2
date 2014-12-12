import unittest

class Carrinho:
  
  def __init__(self):
    self.produtos = list()

  def adicionar_produto(self, produto):
    adicionou = False
    for lista in self.produtos:
      if not (produto in lista):
        lista.append(produto)
        adicionou = True
        break
    if not adicionou:
      self.produtos.append([produto])

class CarrinhoTest(unittest.TestCase):
  
  def setUp(self):
    self.carrinho = Carrinho()

  def test_adicionar_produto1(self):
    self.carrinho.adicionar_produto(1)
    self.assertEqual(self.carrinho.produtos, [[1]])

  def test_adicionar_produto2(self):
    self.carrinho.adicionar_produto(1)
    self.carrinho.adicionar_produto(2)
    self.assertEqual(self.carrinho.produtos, [[1,2]])

  def test_adicionar_produto3(self):
    self.carrinho.adicionar_produto(1)
    self.carrinho.adicionar_produto(2)
    self.carrinho.adicionar_produto(1)
    self.assertEqual(self.carrinho.produtos, [[1,2],[1]])

if __name__ == '__main__':
  unittest.main()