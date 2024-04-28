import unittest

from PyFakeDados.bairro import gerar_bairro
from PyFakeDados.cep import gerar_cep
from PyFakeDados.cnpj import gerar_cnpj, validar_cnpj
from PyFakeDados.cpf import gerar_cpf, validar_cpf
from PyFakeDados.ctps import gerar_ctps
from PyFakeDados.email import gerar_email, gerar_email_empresa, gerar_email_pessoa
from PyFakeDados.empresa import gerar_segmento, gerar_nome_empresa, gerar_empresa
from PyFakeDados.nome import gerar_nome
from PyFakeDados.endereco import gerar_endereco
from PyFakeDados.estado import gerar_uf, validar_uf, gerar_estado, busca_nome_uf

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


class TestEmail(unittest.TestCase):
    
    def test_gerar_email(self):
        result = gerar_email(gerar_nome())
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_gerar_email_empresa(self):
        result = gerar_email_empresa(gerar_nome_empresa())
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_gerar_email_pessoa(self):
        result = gerar_email_pessoa(gerar_nome())
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)


class TestEmpresa(unittest.TestCase):
    

    def test_gerar_segmento(self):
        result = gerar_segmento()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
    

    def test_gerar_nome_empresa(self):
        result = gerar_nome_empresa()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
    

    def test_gerar_empresa(self):
        result = gerar_empresa()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)


class TestEndereco(unittest.TestCase):


    def test_gerar_endereco(self):
        result = gerar_endereco()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)


class TestEstado(unittest.TestCase):


    def test_gerar_uf(self):
        result = gerar_uf()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
    

    def test_validar_uf(self):
        result = validar_uf(gerar_uf())
        self.assertIsNotNone(result)
        self.assertIsInstance(result, bool)
    

    def test_gerar_estado(self):
        result = gerar_estado()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
    

    def test_busca_nome_uf(self):
        result = busca_nome_uf(gerar_uf())
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()