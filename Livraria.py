#http://www.codingdojo.org/cgi-bin/index.pl?action=browse&id=KataPotter&revision=41

import unittest

def livraria(livros):
    preco = 42
    valor = 0
    total_livros = 0
    desconto = [1,0.95,0.90,0.85,0.80]
    
    
    for exemplares in livros[0:5]:
        valor += exemplares * preco
        if exemplares != 0 and total_livros < 5: 
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
        self.assertEqual(0, livraria([0,0,0,0,0]))
        
    def test_um(self):
        self.assertEqual(42, livraria([1,0,0,0,0]))
        self.assertEqual(42, livraria([0,1,0,0,0]))
        self.assertEqual(42, livraria([0,0,1,0,0]))
        self.assertEqual(42, livraria([0,0,0,1,0]))
        self.assertEqual(42, livraria([0,0,0,0,1]))
        
    def testar_oitavo_livro(self):
        self.assertEqual(0, livraria([0,0,0,0,0,1]))
    
    def test_dois_sem_desconto(self):
        self.assertEqual(84, livraria([2,0,0,0,0]))
        self.assertEqual(84, livraria([0,2,0,0,0]))
        self.assertEqual(84, livraria([0,0,2,0,0]))
        self.assertEqual(84, livraria([0,0,0,2,0]))
        self.assertEqual(84, livraria([0,0,0,0,2]))
        
    def test_dois_com_desconto(self):
        self.assertEqual(84*0.95, livraria([1,1,0,0,0]))

    def test_cinco_livros(self):
        self.assertEqual((5*42)*0.8, livraria([1,1,1,1,1]))
        
    def test_dois_de_dois(self):
        self.assertEqual(4*42*0.95, livraria([2,2,0,0,0]))
    
    def teste_dois_grupos_separados(self):
        self.assertEqual((3*42*0.9)+42, livraria([2,1,1,0,0]));
        

if __name__ == '__main__':
    unittest.main()