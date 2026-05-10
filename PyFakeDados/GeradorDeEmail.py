import random

from PyFakeDados.GeradorDeDominio import GeradorDeDominio
from PyFakeDados.utils import remover_acentos

provedores = [
    'gmail.com',
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "icloud.com",
    "protonmail.com",
    "mail.com",
    "zoho.com",
    "mail.ru",
    "fastmail.com",
    "gmx.com",
    "ambermail.com",
    "posteo.de",
    "mailinator.com",
    "cock.li",
    "riseup.net",
    "tutanota.com",
    "yandex.ru",
    "msn.com",
    "proton.me"
]


class GeradorDeEmail:
    """Gerador de emails para pessoas e empresas."""

    @staticmethod
    def gerar_email(nome: str, dominio=None) -> str:
        nome = remover_acentos(nome)
        nome = nome.lower().replace(" ", "")
        provedor = random.choice(provedores)
        email = f'{nome}@{provedor}'
        return email

    @staticmethod
    def gerar_email_empresa(nome, dominio=None) -> str:
        nome = ''.join(f"{i}" for i in nome.split()[:-1])
        nome = remover_acentos(nome).lower().replace(" ", "")
        provedor = nome
        if not dominio:
            dominio = GeradorDeDominio().gerar_dominio()
        email = f'contato@{nome}{dominio}'
        return email

    @staticmethod
    def gerar_email_pessoa(nome) -> str:
        nome = remover_acentos(nome)
        nome = nome.lower().replace(" ", "")
        if not dominio:
            dominio = GeradorDeDominio().gerar_dominio()
        email = f'{nome}@{nome}{dominio}'
        return email
