import random

from PyFakeDados.GeradorDeDominio import GeradorDeDominio
from PyFakeDados.utils import remover_acentos


class GeradorDeSites:
    """Gerador de sites para pessoas."""

    @staticmethod
    def gerar_site(nome: str, dominio: str):

        nome = remover_acentos(nome)
        nome = nome.lower().replace(
            " de ",
            "").replace(
            " da ",
            "").replace(
            " do ",
            "").replace(
                " das ",
                "").replace(
                    " dos ",
                    "").replace(
                        " ",
            "")
        if not dominio:
            dominio = GeradorDeDominio().gerar_dominio()
        site = f'{nome}{dominio}'
        return site
