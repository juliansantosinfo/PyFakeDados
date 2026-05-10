import random

from PyFakeDados.GeradorDeCNPJ import GeradorDeCNPJ
from PyFakeDados.GeradorDeDominio import GeradorDeDominio
from PyFakeDados.GeradorDeEmail import GeradorDeEmail
from PyFakeDados.GeradorDeEndereco import GeradorDeEndereco
from PyFakeDados.GeradorDeInscricaoEstadual import GeradorDeInscricaoEstadual
from PyFakeDados.GeradorDeNome import GeradorDeNome
from PyFakeDados.GeradorDePessoa import GeradorDePessoa
from PyFakeDados.GeradorDeSenhas import GeradorDeSenhas
from PyFakeDados.GeradorDeSites import GeradorDeSites
from PyFakeDados.GeradorDeTelefones import GeradorDeTelefones
from PyFakeDados.utils import gerar_data, remover_acentos

LISTA_SEGMENTOS = [
    'Consultoria',
    'Indústria',
    'Comércio',
    'Energia',
    'Engenharia',
    'Logística',
    'Transportadora',
    'Agro',
    'Farmacêutica',
    'Cerâmica',
    'Madeireira',
    'Marcenaria',
    'Construtora',
    'Metalurgica']


class GeradorDeEmpresa():

    @staticmethod
    def gerar_segmento():
        return random.choice(LISTA_SEGMENTOS)

    @staticmethod
    def gerar_nome_empresa(segmento=None):

        layouts = [1, 2, 3, 4, 5]
        nomes = [GeradorDeNome().gerar_nome_completo() for _ in range(1, 50)]
        palavras1 = [
            'Nova',
            'Primeira',
            'Global',
            'Mega',
            'Excel',
            'Pro',
            'Super',
            'Ultra',
            'Master',
            'Max',
            'Top',
            'Red',
            'Blue',
            'Green',
            'Gray',
            'Sec',
            'Global',
            "Tech",
            "Soluções",
            "Inovação",
            "Global",
            "Digital",
            "Sistemas",
            "Estratégia",
            "Criativa",
            "Negócios",
            "Marketing",
            "Web",
            "Inteligência",
            "Projetos",
            "Tecnologia",
            "Serviços",
            "Desenvolvimento",
            "Software",
            "Gestão",
            "Empreendimentos",
            "Analytics",
            "Design",
            "Comunicação",
            "Segurança",
            "Mobile",
            "App",
            "Investimentos",
            "Financeira",
            "Consulting",
            "Vendas",
            "E-commerce",
            "Social",
            "Educação",
            "Recursos",
            "Saúde",
            "Arquitetura",
            "Arte",
            "Eventos",
            "Imobiliária",
            "Alimentos",
            "Moda",
            "Transporte",
            "Automotiva",
            "Ambiental",
            "Telecomunicações"]
        palavras2 = [
            'Nova',
            'Primeira',
            'Global',
            'Mega',
            'Excel',
            'Pro',
            'Super',
            'Ultra',
            'Master',
            'Max',
            'Top',
            'Red',
            'Blue',
            'Green',
            'Gray',
            'Sec',
            'Global',
            "Tech",
            "Soluções",
            "Inovação",
            "Global",
            "Digital",
            "Sistemas",
            "Estratégia",
            "Criativa",
            "Negócios",
            "Marketing",
            "Web",
            "Inteligência",
            "Projetos",
            "Tecnologia",
            "Serviços",
            "Desenvolvimento",
            "Software",
            "Gestão",
            "Empreendimentos",
            "Analytics",
            "Design",
            "Comunicação",
            "Segurança",
            "Mobile",
            "App",
            "Investimentos",
            "Financeira",
            "Consulting",
            "Vendas",
            "E-commerce",
            "Social",
            "Educação",
            "Recursos",
            "Saúde",
            "Arquitetura",
            "Arte",
            "Eventos",
            "Imobiliária",
            "Alimentos",
            "Moda",
            "Transporte",
            "Automotiva",
            "Ambiental",
            "Telecomunicações"]
        palavras3 = ['S/A', 'S.A.', 'LTDA', 'Ltda.', 'EIRELI', 'ME', 'Group']

        layout = random.choice(layouts)

        if segmento is None:
            segmento = GeradorDeEmpresa().gerar_segmento()

        nome = random.choice(nomes)
        palavra1 = random.choice(palavras1)
        palavras2.remove(palavra1)
        palavra2 = random.choice(palavras2)
        palavra3 = random.choice(palavras3)

        if layout == 1:
            return f'{segmento} {palavra1} {palavra2} {palavra3}'
        elif layout == 2:
            return f'{palavra1} {palavra2} {segmento} {palavra3}'
        elif layout == 3:
            return f'{palavra1} {segmento} {palavra2} {palavra3}'
        elif layout == 4:
            return f'{nome} {segmento}'
        elif layout == 5:
            return f'{segmento} {nome}'

        return f'{segmento} {palavra1} {palavra2} {palavra3}'

    @staticmethod
    def gerar_empresa(
            uf=None,
            municipio=None,
            segmento=None,
            force_ASCII=False,
            force_upper=False):

        if uf is None:
            uf = GeradorDeEndereco().gerar_estado().pop()
            uf = GeradorDeEndereco().get_sigla_estado(uf)

        empresa = {}
        socios = []

        nome = GeradorDeEmpresa().gerar_nome_empresa(segmento)
        cnpj = GeradorDeCNPJ().gerar_cnpj()
        inscricao_estadual = GeradorDeInscricaoEstadual().gerar_inscricao_estadual()
        data_abertura = gerar_data()
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

        if not nome.endswith("S.A.") and not nome.endswith("S/A"):
            socios = [GeradorDePessoa().gerar_pessoa()
                      for socio in range(1, random.randint(1, 5))]

        empresa = {
            "nome": nome,
            "documentos": {
                "cnpj": cnpj,
                "inscricao_estadual": inscricao_estadual,
            },
            "data_abertura": data_abertura.strftime("%d/%m/%Y"),
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
            "socios": socios,
        }

        if force_ASCII:
            for i in empresa:
                if isinstance(empresa[i], str):
                    empresa[i] = remover_acentos(empresa[i])

        if force_upper:
            for i in empresa:
                if isinstance(empresa[i], str):
                    empresa[i] = empresa[i].upper()

        return empresa
