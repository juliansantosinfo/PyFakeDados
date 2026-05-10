import itertools
import random


class GeradorDeCPF:
    """
    Classe para gerar e validar CPFs fictícios.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        """
        Formata um CPF para o formato XXX.XXX.XXX-XX.

        Args:
            cpf (str): O CPF a ser formatado.

        Returns:
            str: O CPF formatado.
        """
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Verifica se um CPF é válido.

        Args:
            cpf (str): O CPF a ser verificado.

        Returns:
            bool: True se o CPF for válido, False caso contrário.
        """

        # Remove caracteres não numéricos do CPF
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verifica se o CPF possui 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Calcula o primeiro dígito verificador e compara com o CPF fornecido
        soma = sum(int(x) * y for x,
                   y in zip(cpf[:9], itertools.count(10, -1)))
        if (11 - (soma % 11)) % 11 != int(cpf[9]):
            return False

        # Calcula o segundo dígito verificador e compara com o CPF fornecido
        soma = sum(int(x) * y for x,
                   y in zip(cpf[:10], itertools.count(11, -1)))
        if (11 - (soma % 11)) % 11 != int(cpf[10]):
            return False

        return True

    @staticmethod
    def gerar_cpfs(mask=False, quantidade=1) -> list:
        """
        Gera CPFs fictícios.

        Args:
            mask (bool): Indica se o CPF deve ser formatado como XXX.XXX.XXX-XX. Se False, retorna apenas os dígitos do CPF.
            quantidade (int): Indica o numero de CPFs a serem gerados.

        Returns:
            list: Lista com os CPFs gerados, formato XXX.XXX.XXX-XX ou apenas os dígitos.
        """

        cpfs = []

        for i in range(quantidade):
            # Gera os nove primeiros dígitos do CPF de forma aleatória
            cpf = [random.randint(0, 9) for _ in range(9)]

            # Calcula o primeiro dígito verificador
            soma = sum(x * y for x, y in zip(cpf, itertools.count(10, -1)))
            cpf.append((11 - (soma % 11)) % 11)

            # Calcula o segundo dígito verificador
            soma = sum(x * y for x, y in zip(cpf, itertools.count(11, -1)))
            cpf.append((11 - (soma % 11)) % 11)

            # Convert lista de digitos do cpf em string.
            cpf = ''.join([str(num) for num in cpf])

            if mask:
                # Adiciona mascara ao CPF no formatado (XXX.XXX.XXX-XX)
                cpf = GeradorDeCPF.formatar_cpf(cpf)

            cpfs.append(cpf)

        return cpfs

    @staticmethod
    def gerar_cpf(mask=False) -> str:
        """
        Gera um CPF fictício.

        Args:
            mask (bool): Indica se o CPF deve ser formatado como XXX.XXX.XXX-XX. Se False, retorna apenas os dígitos do CPF.

        Returns:
            str: O CPF gerado, formato XXX.XXX.XXX-XX ou apenas os dígitos.
        """
        cpf = GeradorDeCPF().gerar_cpfs(mask=mask)
        cpf = cpf.pop()
        return cpf
