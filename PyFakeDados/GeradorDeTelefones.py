import random

from PyFakeDados.GeradorDeEndereco import GeradorDeEndereco

LISTA_DDD = {
    'AC': ['68'],
    'AL': ['82'],
    'AM': ['92', '97'],
    'AP': ['96'],
    'BA': ['71', '73', '74', '75', '77'],
    'CE': ['85', '88'],
    'DF': ['61'],
    'ES': ['27', '28'],
    'GO': ['62', '64'],
    'MA': ['98', '99'],
    'MG': ['31', '32', '33', '34', '35', '37', '38'],
    'MS': ['67'],
    'MT': ['65', '66'],
    'PA': ['91', '93', '94'],
    'PB': ['83'],
    'PE': ['81', '87'],
    'PI': ['86', '89'],
    'PR': ['41', '42', '43', '44', '45', '46'],
    'RJ': ['21', '22', '24'],
    'RN': ['84'],
    'RO': ['69'],
    'RR': ['95'],
    'RS': ['51', '53', '54', '55'],
    'SC': ['47', '48', '49'],
    'SE': ['79'],
    'SP': ['11', '12', '13', '14', '15', '16', '17', '18', '19'],
    'TO': ['63']
}


class GeradorDeTelefones:
    """Gerador de números de telefone."""

    @staticmethod
    def gerar_ddd(uf=None):
        return random.choice(LISTA_DDD[uf.upper()])

    @staticmethod
    def gerar_telefone_fixo(uf=None, ddd=None, mask=False):

        if uf is None:
            uf = GeradorDeEndereco().gerar_uf().pop()

        if uf.upper() not in LISTA_DDD:
            raise ValueError("UF inválida.")

        if not ddd:
            ddd = random.choice(LISTA_DDD[uf.upper()])

        numero = ''.join(str(random.randint(0, 9)) for _ in range(7))

        if mask:
            telefone = f"({ddd}) {numero[:4]}-{numero[4:]}"
        else:
            telefone = f"{ddd}3{numero[:3]}{numero[4:]}"
        return telefone

    @staticmethod
    def gerar_telefone_celular(uf=None, ddd=None, mask=False):

        if uf is None:
            uf = GeradorDeEndereco().gerar_uf().pop()

        if uf.upper() not in LISTA_DDD:
            raise ValueError("UF inválida.")

        if not ddd:
            ddd = random.choice(LISTA_DDD[uf.upper()])

        numero = f'{str(random.randint(7, 9))}' + \
            (''.join(str(random.randint(0, 9)) for _ in range(7)))

        if mask:
            telefone = f"({ddd}) 9{numero[:4]}-{numero[4:]}"
        else:
            telefone = f"{ddd}9{numero[:4]}{numero[4:]}"
        return telefone
