import unittest

from PyFakeDados.GeradorDeCPF import GeradorDeCPF
from PyFakeDados.GeradorDeEndereco import GeradorDeEndereco


class TestBairro(unittest.TestCase):

    def test_gerar_bairro(self):
        result = GeradorDeEndereco().gerar_bairro()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)


class TestCEP(unittest.TestCase):

    def test_gerar_cep(self):
        result = GeradorDeEndereco().gerar_cep()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)


class TestCPF(unittest.TestCase):

    def test_gerar_cpf(self):
        result = GeradorDeCPF().gerar_cpf()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_validar_cpf(self):
        cpf = GeradorDeCPF().gerar_cpf()
        result = GeradorDeCPF().validar_cpf(cpf)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    unittest.main()
