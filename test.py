import unittest

from PyFakeDados.bairro import gerar_bairro
from PyFakeDados.cep import gerar_cep
from PyFakeDados.cnpj import gerar_cnpj, validar_cnpj
from PyFakeDados.cpf import gerar_cpf, validar_cpf
from PyFakeDados.ctps import gerar_ctps

class TestBairro(unittest.TestCase):
    
    def test_gerar_bairro(self):
        result = gerar_bairro()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

class TestCEP(unittest.TestCase):
    
    def test_gerar_cep(self):
        result = gerar_cep()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()