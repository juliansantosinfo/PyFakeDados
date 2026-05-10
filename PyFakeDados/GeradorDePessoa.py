import random
from datetime import datetime, timedelta

from PyFakeDados.GeradorDeCPF import GeradorDeCPF
from PyFakeDados.GeradorDeCTPS import GeradorDeCTPS
from PyFakeDados.GeradorDeDominio import GeradorDeDominio
from PyFakeDados.GeradorDeEmail import GeradorDeEmail
from PyFakeDados.GeradorDeEndereco import GeradorDeEndereco
from PyFakeDados.GeradorDeNome import GeradorDeNome
from PyFakeDados.GeradorDePISs import GeradorDePISs
from PyFakeDados.GeradorDeRGs import GeradorDeRGs
from PyFakeDados.GeradorDeSenhas import GeradorDeSenhas
from PyFakeDados.GeradorDeSites import GeradorDeSites
from PyFakeDados.GeradorDeTelefones import GeradorDeTelefones
from PyFakeDados.utils import gerar_data_nascimento, remover_acentos


class GeradorDePessoa:
    """
    Classe para gerar pessoas fictícias.
    """

    def gerar_pessoa(
            self,
            uf=None,
            municipio=None,
            mask=False,
            idade=None,
            recem_nascido=False,
            force_ASCII=False,
            force_upper=False):

        if uf is None:
            uf = GeradorDeEndereco().gerar_estado().pop()
            uf = GeradorDeEndereco().get_sigla_estado(uf)

        if idade is None:

            idade_min = 1
            idade_max = 99

            if recem_nascido:
                idade_min = 0

            idade = random.randint(idade_min, idade_max)

        pessoa = {}
        data_nascimento = gerar_data_nascimento(idade)

        sexo = GeradorDeNome().gerar_sexo()
        nome, mae, pai = GeradorDeNome().gerar_nome_com_filiacao(sexo=sexo)
        cpf = GeradorDeCPF().gerar_cpf(mask=mask)
        rg = GeradorDeRGs().gerar_rg()
        ctps = GeradorDeCTPS().gerar_ctps()
        pis = GeradorDePISs().gerar_pis()
        dominio = GeradorDeDominio().gerar_dominio()
        site = GeradorDeSites().gerar_site(nome, dominio)
        email = GeradorDeEmail().gerar_email(nome)

        senha = GeradorDeSenhas().gerar_senha_numerica()
        senha_forte = GeradorDeSenhas().gerar_senha(16)

        endereco = GeradorDeEndereco().gerar_endereco(uf=uf, municipio=municipio)
        municipio = endereco["municipio"]
        cep = endereco["cep"]
        bairro = endereco["bairro"]
        logradouro = endereco["logradouro"]
        numero = endereco["numero"]

        ddd = GeradorDeTelefones().gerar_ddd(uf)
        telefone = GeradorDeTelefones().gerar_telefone_fixo(uf, ddd)
        celular = GeradorDeTelefones().gerar_telefone_celular(uf, ddd)

        pessoa = {
            "sexo": sexo,
            "nome": nome,
            "mae": mae,
            "pai": pai,
            "documentos": {
                "cpf": cpf,
                "rg": rg,
                "ctps": ctps,
                "pis": pis,
            },
            "data_nascimento": data_nascimento.strftime("%d/%m/%Y"),
            "site": site,
            "email": email,
            "senha": senha,
            "senha_forte": senha_forte,
            "endereco": {
                "estado": uf,
                "municipio": municipio,
                "cep": cep,
                "bairro": bairro,
                "logradouro": logradouro,
                "numero": numero,
            },
            "telefone": {
                "ddd": ddd,
                "fixo": telefone,
                "celular": celular,
            },
        }

        if force_ASCII:
            for i in pessoa:
                if isinstance(pessoa[i], str):
                    pessoa[i] = remover_acentos(pessoa[i])

        if force_upper:
            for i in pessoa:
                if isinstance(pessoa[i], str):
                    pessoa[i] = pessoa[i].upper()

        return pessoa
