import random
import sqlite3

from PyFakeDados.utils import remover_acentos

ESTADOS_SIGLAS = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]
ESTADOS_SIGLAS_NOME = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

LOGRADOUROS_TIPOS = ['Rua', 'Avenida', 'Estrada',
                     'Beco', 'Travessa', 'Alameda', 'Viela']
LOGRADOUROS_PREFIXOS = ['Do', 'Dos', 'Das', 'De',
                        'Doutor', 'Dom', 'Vila', 'Chácara', 'Sítio']
LOGRADOUROS_SUFIXOS = ['Novo', 'Velho', 'Grande', 'Pequeno',
                       'Alto', 'Baixo', 'Leste', 'Oeste', 'Norte', 'Sul']

db_enderecos = sqlite3.connect("PyFakeDados/database/endereco.sqlite3.db")


class GeradorDeEndereco:
    """
    Classe para gerar endereços e estados fictícios a partir de consultas ao banco de dados.
    """

    def __init__(self) -> None:
        """
        Inicializa um objeto GeradorEnderecos.

        Atributos:
            cursor (objeto): Objeto de cursor para realizar consultas ao banco de dados.
            force_ASCII (bool): Define se os dados devem ser convertidos para ASCII.
            force_upper (bool): Define se os dados devem ser convertidos para maiúsculas.
        """
        self.cursor = db_enderecos.cursor()
        self.force_ASCII = False
        self.force_upper = False

    def get_nome_estado(self, uf: str):
        if uf.upper() not in ESTADOS_SIGLAS:
            raise ValueError("UF inválida.")
        return ESTADOS_SIGLAS_NOME[uf.upper()]

    def get_sigla_estado(self, estado: dict):
        return estado["sigla"]

    def get_query_estado(self, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter estados aleatórios.

        Args:
            quantidade (int): Número de estados a serem retornados. Padrão é 1.

        Returns:
            str: Consulta SQL para obter estados aleatórios.
        """
        return f"""
        SELECT
            id,
            sigla,
            nome
        FROM
            estados
        ORDER BY
            Random()
        LIMIT {quantidade}
        """

    def get_query_municipio(self, uf=None, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter municipios aleatórios.

        Args:
            quantidade (int): Número de municipios a serem retornados. Padrão é 1.

        Returns:
            str: Consulta SQL para obter municipios aleatórios.
        """
        if uf is None:
            join = ""
        else:
            join = f"join estados on estados.sigla = '{
                uf}' AND municipios.estado_id = estados.id"

        return f"""
        SELECT
            municipios.id,
            municipios.nome
        FROM
            municipios {join}
        WHERE
            1=1
        ORDER BY
            Random()
        LIMIT {quantidade}
        """

    def get_query_cep(self, uf=None, municipio=None, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter CEPs aleatórios.

        Args:
            quantidade (int): Número de CEPs a serem retornados. Padrão é 1.

        Returns:
            str: Consulta SQL para obter CEPs aleatórios.
        """
        if uf is None:
            join = ""
        else:
            join = f"join estados on estados.sigla = '{
                uf}' AND logradouros.uf = estados.sigla"

        return f"""
        SELECT
            logradouros.cep
        FROM
            logradouros {join}
        WHERE
            1=1
        ORDER BY
            Random()
        LIMIT {quantidade}
        """

    def get_query_bairro(self, uf=None, municipio=None, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter bairros aleatórios.

        Args:
            quantidade (int): Número de bairros a serem retornados. Padrão é 1.

        Returns:
            str: Consulta SQL para obter bairros aleatórios.
        """
        if uf is None:
            join = ""
        else:
            join = f"join estados on estados.sigla = '{
                uf}' AND logradouros.uf = estados.sigla"

        return f"""
        SELECT
            DISTINCT logradouros.nome_bairro
        FROM
            logradouros {join}
        WHERE
            1=1
        ORDER BY
            Random()
        LIMIT {quantidade}
        """

    def get_query_endereco(self, uf=None, municipio=None, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter endereços aleatórios.

        Args:
            uf (str): Sigla do estado para filtrar os endereços. Opcional.
            municipio (str): Nome do município para filtrar os endereços. Opcional.
            quantidade (int): Número de endereços a serem retornados. Padrão é 1.

        Returns:
            str: Consulta SQL para obter endereços aleatórios.
        """
        where_uf = f"AND uf = '{uf}'" if uf else ''
        where_municipio = f"AND lower(l.nome_municipio) = '{
            municipio.lower()}'" if municipio else ''

        return f"""
        SELECT
            uf,
            nome_municipio,
            cep,
            nome_bairro,
            nome_logradouro,
            ABS(RANDOM()) % 1050 + 1 as numero
        FROM
            logradouros l
        WHERE
            1=1
            {where_uf}
            {where_municipio}
        ORDER BY
            random()
        LIMIT
            {quantidade}
        """

    def gerar_estado(self, quantidade=1) -> list[dict]:
        """
        Gera estados fictícios.

        Args:
            quantidade (int): Número de estados a serem gerados. Padrão é 1.

        Returns:
            list: Lista de estados gerados.
        """
        estados = []

        def build(estado: tuple) -> dict:
            """
            Constrói um dicionário com informações do estado.

            Args:
                estado (tuple): Tupla contendo informações do estado.

            Returns:
                dict: Dicionário com informações do estado.
            """
            if self.force_ASCII:
                estado = (remover_acentos(v) if isinstance(
                    v, str) else v for v in estado)  # type: ignore
            if self.force_upper:
                estado = (v.upper() if isinstance(
                    v, str) else v for v in estado)  # type: ignore

            return {
                "id": estado[0],
                "sigla": estado[1],
                "nome": estado[2],
            }

        self.cursor.execute(self.get_query_estado(quantidade))
        resultado_consulta = self.cursor.fetchall()

        for registro in resultado_consulta:
            estados.append(build(registro))

        return estados

    def gerar_uf(self, quantidade=1) -> list:
        """
        Gera UF fictícios.

        Args:
            quantidade (int): Número de estados a serem gerados. Padrão é 1.

        Returns:
            str: Lista com sigla dos estados gerados.
        """

        estados = self.gerar_estado(quantidade=quantidade)
        siglas = []

        for estado in estados:
            sigla = estado["sigla"]
            siglas.append(sigla)

        return siglas

    def gerar_municipios(self, uf=None, quantidade=1) -> list:
        """
        Gera municipios fictícios.

        Args:
            quantidade (int): Número de municipios a serem gerados. Padrão é 1.

        Returns:
            list: Lista de municipios gerados.
        """
        municipios = []

        def build(municipio: tuple) -> dict:
            """
            Constrói um dicionário com informações do municipio.

            Args:
                municipio (tuple): Tupla contendo informações do municipio.

            Returns:
                dict: Dicionário com informações do municipio.
            """
            if self.force_ASCII:
                municipio = (remover_acentos(v) if isinstance(
                    v, str) else v for v in municipio)  # type: ignore
            if self.force_upper:
                municipio = (v.upper() if isinstance(
                    v, str) else v for v in municipio)  # type: ignore

            return {
                "id": municipio[0],
                "nome": municipio[1],
            }

        self.cursor.execute(self.get_query_municipio(uf, quantidade))
        resultado_consulta = self.cursor.fetchall()

        for registro in resultado_consulta:
            municipios.append(build(registro))

        return municipios

    def gerar_ceps(self, uf=None, municipio=None, quantidade=1) -> list:
        """
        Gera CEPs fictícios.

        Args:
            quantidade (int): Número de CEPs a serem gerados. Padrão é 1.

        Returns:
            list: Lista de CEPs gerados.
        """
        CEPs = []

        def build(cep: tuple) -> dict:
            """
            Constrói um dicionário com informações do cep.

            Args:
                cep (tuple): Tupla contendo informações do cep.

            Returns:
                dict: Dicionário com informações do cep.
            """
            if self.force_ASCII:
                cep = (remover_acentos(v) if isinstance(
                    v, str) else v for v in cep)  # type: ignore
            if self.force_upper:
                cep = (v.upper() if isinstance(v, str)
                       else v for v in cep)  # type: ignore

            return {
                "cep": cep[0],
            }

        self.cursor.execute(self.get_query_cep(uf, municipio, quantidade))
        resultado_consulta = self.cursor.fetchall()

        for registro in resultado_consulta:
            CEPs.append(build(registro))

        return CEPs

    def gerar_bairros(self, uf=None, municipio=None, quantidade=1) -> list:
        """
        Gera bairros fictícios.

        Args:
            quantidade (int): Número de bairros a serem gerados. Padrão é 1.

        Returns:
            list: Lista de bairros gerados.
        """
        bairros = []

        def build(bairro: tuple) -> dict:
            """
            Constrói um dicionário com informações do bairro.

            Args:
                bairro (tuple): Tupla contendo informações do bairro.

            Returns:
                dict: Dicionário com informações do bairro.
            """
            if self.force_ASCII:
                bairro = (remover_acentos(v) if isinstance(
                    v, str) else v for v in bairro)  # type: ignore
            if self.force_upper:
                bairro = (v.upper() if isinstance(
                    v, str) else v for v in bairro)  # type: ignore

            return {
                "nome": bairro[0],
            }

        self.cursor.execute(self.get_query_bairro(uf, municipio, quantidade))
        resultado_consulta = self.cursor.fetchall()

        for registro in resultado_consulta:
            bairros.append(build(registro))

        return bairros

    def gerar_enderecos(self, uf=None, municipio=None, quantidade=1) -> list:
        """
        Gera endereços fictícios.

        Args:
            uf (str): Sigla do estado para filtrar os endereços. Opcional.
            municipio (str): Nome do município para filtrar os endereços. Opcional.
            quantidade (int): Número de endereços a serem gerados. Padrão é 1.

        Returns:
            list: Lista de endereços gerados.
        """
        enderecos = []

        def build(endereco: tuple) -> dict:
            """
            Constrói um dicionário com informações do endereço.

            Args:
                endereco (tuple): Tupla contendo informações do endereço.

            Returns:
                dict: Dicionário com informações do endereço.
            """
            if self.force_ASCII:
                endereco = (remover_acentos(v) if isinstance(
                    v, str) else v for v in endereco)  # type: ignore
            if self.force_upper:
                endereco = (v.upper() if isinstance(
                    v, str) else v for v in endereco)  # type: ignore

            return {
                "uf": endereco[0],
                "estado": self.get_nome_estado(endereco[0]),
                "municipio": endereco[1],
                "cep": endereco[2],
                "bairro": endereco[3],
                "logradouro": endereco[4],
                "numero": endereco[5],
            }

        self.cursor.execute(self.get_query_endereco(uf, municipio, quantidade))
        resultado_consulta = self.cursor.fetchall()

        for registro in resultado_consulta:
            enderecos.append(build(registro))

        return enderecos

    def gerar_numero(self):
        return str(random.randint(1, 2000))

    def gerar_logradouro(self):

        tipo = random.choice(LOGRADOUROS_TIPOS)
        prefixo = random.choice(LOGRADOUROS_PREFIXOS)
        sufixo = random.choice(LOGRADOUROS_SUFIXOS)

        return f'{tipo} {prefixo} {sufixo}'

    def gerar_logradouro_com_numero(self):

        tipo = random.choice(LOGRADOUROS_TIPOS)
        prefixo = random.choice(LOGRADOUROS_PREFIXOS)
        sufixo = random.choice(LOGRADOUROS_SUFIXOS)
        numero = str(random.randint(1, 2000))

        return f'{tipo} {prefixo} {sufixo}, {numero}'

    def gerar_municipio(self, uf=None) -> str:
        municipio = self.gerar_municipios(uf=uf)
        municipio = municipio.pop()
        municipio = municipio["nome"]
        return municipio

    def gerar_bairro(self, uf=None, municipio=None) -> str:
        bairro = self.gerar_bairros(uf=None, municipio=None)
        bairro = bairro.pop()
        bairro = bairro["nome"]
        return bairro

    def gerar_endereco(self, uf=None, municipio=None) -> str:
        endereco = self.gerar_enderecos(uf=None, municipio=None)
        endereco = endereco.pop()
        return endereco

    def gerar_cep(self, uf=None, municipio=None) -> str:
        cep = self.gerar_ceps(uf=None, municipio=None)
        cep = cep.pop()
        cep = cep["cep"]
        return cep
