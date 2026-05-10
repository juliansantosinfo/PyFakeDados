import random

dominios = [
    ".com",
    ".ru",
    ".org",
    ".net",
    ".info",
    ".biz",
    ".gov",
    ".edu",
    ".mil",
    ".int",
    ".br",
    ".us",
    ".uk",
    ".de",
    ".ca",
    ".fr",
    ".au",
    ".jp",
    ".cn",
    ".nl"
]


class GeradorDeDominio:
    """Gerador dominios para sites e email."""

    @staticmethod
    def gerar_dominio() -> str:
        return random.choice(dominios)
