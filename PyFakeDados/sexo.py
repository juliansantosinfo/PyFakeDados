import random
from PyFakeDados.CONSTANTS_SEXOS import *

LISTA_SEXO = [SEXO_MASCULINO, SEXO_FEMININO]

def gerar_sexo():
    return random.choice(LISTA_SEXO)