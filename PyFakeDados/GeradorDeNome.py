import random
import sqlite3

from PyFakeDados.utils import remover_acentos

db_nomes = sqlite3.connect('PyFakeDados/database/nome.sqlite3.db')


class GeradorDeNome:
    """
    Classe para gerar nomes fictícios a partir de consultas ao banco de dados.
    """

    def __init__(self) -> None:
        """
        Inicializa um objeto GeradorNomes.

        Atributos:
            cursor (objeto): Objeto de cursor para realizar consultas ao banco de dados.
        """
        self.cursor = db_nomes.cursor()
        self.force_ASCII = False
        self.force_upper = False

    def get_query_nome(self, sexo=None, composto=None, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter um nome aleatório.

        Args:
            sexo (str): Sexo do nome a ser retornado. Se não especificado, um sexo será gerado aleatoriamente.
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            str: Consulta SQL para obter um nome aleatório.
        """
        if sexo is None:
            sexo = self.gerar_sexo()

        if composto is None:
            composto = random.choice([True, False])

        return f"""
        SELECT
            nome
        FROM
            nomes
        WHERE
            sexo = '{sexo}'
            AND tipo = 1
        ORDER BY
            random()
        LIMIT
            {quantidade}
        """

    def get_query_nome_masculino(self, composto=None, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter um nome masculino aleatório.

        Args:
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            str: Consulta SQL para obter um nome masculino aleatório.
        """
        return self.get_query_nome(
            sexo='M',
            composto=composto,
            quantidade=quantidade)

    def get_query_nome_feminino(self, composto=None, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter um nome feminino aleatório.

        Args:
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            str: Consulta SQL para obter um nome feminino aleatório.
        """
        return self.get_query_nome(
            sexo='F',
            composto=composto,
            quantidade=quantidade)

    def get_query_sobrenome(self, quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter um sobrenome aleatório.

        Returns:
            str: Consulta SQL para obter um sobrenome aleatório.
        """
        return f"""
        SELECT
            nome
        FROM
            nomes
        WHERE
            sexo = ' '
            AND tipo = 2
        ORDER BY
            random()
        LIMIT
            {quantidade}
        """

    def get_query_nome_completo(
            self,
            sexo=None,
            composto=None,
            quantidade=1) -> str:
        """
        Retorna a consulta SQL para obter um nome completo aleatório.

        Args:
            sexo (str): Sexo do nome a ser retornado. Se não especificado, um sexo será gerado aleatoriamente.
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            str: Consulta SQL para obter um nome completo aleatório.
        """
        if sexo is None:
            sexo = self.gerar_sexo()

        if composto is None:
            composto = random.choice([True, False])

        return f"""
        WITH first_name AS (
            SELECT Row_Number() OVER (ORDER BY Random()) row_number, nome FROM nomes WHERE sexo = '{sexo}' AND tipo = 1 ORDER BY random() LIMIT {quantidade}
        ),

        middle_name AS (
            SELECT Row_Number() OVER (ORDER BY Random()) row_number, nome FROM nomes WHERE sexo = '{sexo}' AND tipo = 1 ORDER BY random() LIMIT {quantidade}
        ),

        last_name AS (
            SELECT Row_Number() OVER (ORDER BY Random()) row_number, nome FROM nomes WHERE sexo = ' ' AND tipo = 2 ORDER BY random() LIMIT {quantidade}
        )

        SELECT
            CASE
                WHEN {composto} = True THEN
                    first_name.nome || ' ' || middle_name.nome || ' ' || last_name.nome
                ELSE
                    first_name.nome || ' ' || last_name.nome
            END AS nome,
            first_name.nome as first_name,
            (CASE WHEN {composto} = True THEN middle_name.nome ELSE ' ' END) as middle_name,
            last_name.nome as last_name
        FROM
            first_name
                inner join middle_name on first_name.row_number = middle_name.row_number
                inner join last_name on first_name.row_number = last_name.row_number
        """

    def gerar_sexo(self) -> str:
        """
        Gera sexo aleatoriamente.

        Returns:
            str: Sexo aleatório.
        """
        return random.choice(["M", "F"])

    def gerar_sobrenomes(self, quantidade=1) -> list[str]:
        """
        Gera lista de sobrenomes fictícios.

        Returns:
            list: Lista de sobrenomes gerados.
        """

        sobrenomes = []

        def build(sobrenome) -> str:
            """
            Constrói sobrenome.

            Args:
                sobrenome (str): Tupla contendo informações do sobrenome.

            Returns:
                dict: String com sobrenome.
            """
            sobrenome = sobrenome[0]
            if self.force_ASCII:
                sobrenome = remover_acentos(sobrenome[0])
            if self.force_upper:
                sobrenome = sobrenome.upper()

            return sobrenome

        self.cursor.execute(self.get_query_sobrenome(
            quantidade=quantidade))

        resultado_consulta = self.cursor.fetchall()
        for registro in resultado_consulta:
            sobrenomes.append(build(registro))

        return sobrenomes

    def gerar_nomes(self, sexo=None, composto=None, quantidade=1) -> list[str]:
        """
        Gera um nome fictício.

        Args:
            sexo (str): Sexo do nome a ser gerado. Se não especificado, um sexo será gerado aleatoriamente.
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            list: Nome gerado.
        """
        nomes = []

        def build(nome):
            """
            Constrói nome.

            Args:
                nome (str): Tupla contendo informações do nome.

            Returns:
                str: Nome.
            """
            nome = nome[0]
            if self.force_ASCII:
                nome = remover_acentos(nome)
            if self.force_upper:
                nome = nome.upper()

            return nome

        self.cursor.execute(
            self.get_query_nome(sexo=sexo, composto=composto,
                                quantidade=quantidade)
        )

        resultado_consulta = self.cursor.fetchall()
        for registro in resultado_consulta:
            nomes.append(build(registro))

        return nomes

    def gerar_nomes_masculinos(self, composto=None, quantidade=1) -> list:
        """
        Gera uma lista de nome masculinos fictícios.

        Args:
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            list: Lista de nomes masculinos gerados.
        """

        nomes = []

        def build(nome):
            """
            Constrói nome.

            Args:
                nome (str): Tupla contendo informações do nome.

            Returns:
                str: Nome.
            """
            nome = nome[0]
            if self.force_ASCII:
                nome = remover_acentos(nome)
            if self.force_upper:
                nome = nome.upper()

            return nome

        self.cursor.execute(self.get_query_nome_masculino(
            composto=composto, quantidade=quantidade))

        resultado_consulta = self.cursor.fetchall()
        for registro in resultado_consulta:
            nomes.append(build(registro))

        return nomes

    def gerar_nomes_femininos(self, composto=None, quantidade=1) -> list:
        """
        Gera uma lista de nomes femininos fictícios.

        Args:
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            str: Lista de nome femininos gerados.
        """

        nomes = []

        def build(nome):
            """
            Constrói nome.

            Args:
                nome (str): Tupla contendo informações do nome.

            Returns:
                str: Nome.
            """
            nome = nome[0]
            if self.force_ASCII:
                nome = remover_acentos(nome)
            if self.force_upper:
                nome = nome.upper()

            return nome

        self.cursor.execute(self.get_query_nome_feminino(
            composto=composto, quantidade=quantidade))

        resultado_consulta = self.cursor.fetchall()
        for registro in resultado_consulta:
            nomes.append(build(registro))

        return nomes

    def gerar_nomes_completos(
            self,
            sexo=None,
            composto=None,
            quantidade=1) -> list[str]:
        """
        Gera um nome completo fictício.

        Args:
            sexo (str): Sexo do nome a ser gerado. Se não especificado, um sexo será gerado aleatoriamente.
            composto (bool): Indica se o nome deve ser composto. Se não especificado, será aleatório.

        Returns:
            str: Nome completo gerado.
        """

        nomes = []

        def build(nome) -> str:
            """
            Constrói nome.

            Args:
                nome (str): Tupla contendo informações do nome.

            Returns:
                str: Nome.
            """
            nome = nome[0]
            if self.force_ASCII:
                nome = remover_acentos(nome)
            if self.force_upper:
                nome = nome.upper()

            return nome

        self.cursor.execute(self.get_query_nome_completo(
            sexo, composto, quantidade=quantidade))

        resultado_consulta = self.cursor.fetchall()
        for registro in resultado_consulta:
            nomes.append(build(registro))

        return nomes

    def gerar_nomes_com_filiacao(self, sexo=None, quantidade=1):
        """
        Gera um nome com filiação fictício.

        Returns:
            str: Nome com filiação gerado.
        """

        nomes = []

        for i in range(quantidade):
            nome_mae = self.gerar_nome_completo(sexo='F')
            nome_pai = self.gerar_nome_completo(sexo='M')

            sobrenome_mae = nome_mae.split().pop()
            sobrenome_pai = nome_pai.split().pop()

            nome = self.gerar_nome(sexo=sexo)
            nome = f"{nome} {sobrenome_mae} {sobrenome_pai}"

            nomes.append([nome, nome_mae, nome_pai])

        return nomes

    def gerar_sobrenome(self) -> str:
        sobrenome = self.gerar_sobrenomes()
        sobrenome = sobrenome.pop()
        sobrenome = sobrenome[0]
        return sobrenome

    def gerar_nome(self, sexo=None, composto=None) -> str:
        nome = self.gerar_nomes()
        nome = nome.pop()
        return nome

    def gerar_nome_masculino(self, composto=None) -> str:
        nome = self.gerar_nomes_masculinos()
        nome = nome.pop()
        return nome

    def gerar_nome_feminino(self, composto=None) -> str:
        nome = self.gerar_nomes_femininos()
        nome = nome.pop()
        return nome

    def gerar_nome_completo(self, sexo=None, composto=None) -> str:
        nome = self.gerar_nomes_completos(sexo=None, composto=None)
        nome = nome.pop()
        return nome

    def gerar_nome_com_filiacao(self, sexo=None) -> str:
        nome = self.gerar_nomes_com_filiacao(sexo=sexo)
        nome = nome.pop()
        return nome
