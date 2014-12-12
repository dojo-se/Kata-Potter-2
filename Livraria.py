import unittest

def livraria(livros):
    preco = 42
    valor = 0
    total_livros=0
    desconto = [1,0.95,0.90,0.85,0.80]
    
    for exemplares in livros[0:7]:
        valor += exemplares * preco
        if exemplares != 0: 
            total_livros += 1
    
    #print(total_livros)
    if total_livros > 0:
        valor_descontado = desconto[total_livros-1] * valor 
        valor = valor_descontado

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
    
    def test_dois(self):
        self.assertEqual(84, livraria([2,0,0,0,0,0,0]))
        self.assertEqual(84, livraria([0,2,0,0,0,0,0]))
        self.assertEqual(84, livraria([0,0,2,0,0,0,0]))
        self.assertEqual(84, livraria([0,0,0,2,0,0,0]))
        self.assertEqual(84, livraria([0,0,0,0,2,0,0]))
        self.assertEqual(84, livraria([0,0,0,0,0,2,0]))
        self.assertEqual(84, livraria([0,0,0,0,0,0,2]))



if __name__ == '__main__':
    unittest.main()