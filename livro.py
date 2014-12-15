import unittest

class Livro:
  def __init__(self, titulo, preco):
    self.titulo = titulo
    self.preco  = preco

  def __eq__(self, x):
    return type(x) == Livro and x.titulo == self.titulo \
      and x.preco == self.preco

  def __str__(self):
    return "Titulo: %s Preco: %d" % (self.titulo, self.preco)

  def __repr__(self):
    return self.__str__()

class livtoTest(unittest.TestCase):
  
  def test_comparaLivros(self):
    livro1 = Livro("Livro 1", 10)
    livro2 = Livro("Livro 1", 10)
    livro3 = Livro("Livro 3", 10)
    self.assertTrue(livro1 == livro2)
    self.assertFalse(livro1 == livro3)

if __name__ == '__main__':
    unittest.main()