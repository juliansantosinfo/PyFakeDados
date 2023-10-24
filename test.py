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

class TestCNPJ(unittest.TestCase):
    
    def test_gerar_cnpj(self):
        result = gerar_cnpj()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
    
    def test_validar_cnpj(self):
        cnpj = gerar_cnpj()
        result = validar_cnpj(cnpj)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, bool)

class TestCPF(unittest.TestCase):

    def test_gerar_cpf(self):
        result = gerar_cpf()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_validar_cpf(self):
        cpf = gerar_cpf()
        result = validar_cpf(cpf)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, bool)

class TestCTPS(unittest.TestCase):
    
    def test_gerar_ctps(self):
        result = gerar_ctps()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()