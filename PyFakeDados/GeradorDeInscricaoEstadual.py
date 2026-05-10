import random


class GeradorDeInscricaoEstadual():
    """Gerado de Inscrições Estaduais ficticias"""

    @staticmethod
    def gerar_inscricao_estadual():
        numeros = ''.join(str(random.randint(0, 9)) for _ in range(8))
        inscricao = f'{numeros}'
        return inscricao
