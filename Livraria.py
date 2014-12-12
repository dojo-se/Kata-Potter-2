import unittest

def livraria(livros):
    preco = 42
    valor = 0
    
    for exemplares in livros[0:7]:
        valor += exemplares * preco
    
    return valor

class LivrariaTest(unittest.TestCase):
    def test_vazio(self):
        self.assertEqual(0, livraria([]))
    
    def test_zero(self):
        self.assertEqual(0, livraria([0,0,0,0,0,0,0]))
        
    def test_um(self):
        self.assertEqual(42, livraria([1,0,0,0,0,0,0]))
        self.assertEqual(42, livraria([0,1,0,0,0,0,0]))
        self.assertEqual(42, livraria([0,0,1,0,0,0,0]))
        self.assertEqual(42, livraria([0,0,0,1,0,0,0]))
        self.assertEqual(42, livraria([0,0,0,0,1,0,0]))
        self.assertEqual(42, livraria([0,0,0,0,0,1,0]))
        self.assertEqual(42, livraria([0,0,0,0,0,0,1]))
        
    def testar_oitavo_livro(self):
        self.assertEqual(0, livraria([0,0,0,0,0,0,0,1]))



if __name__ == '__main__':
    unittest.main()