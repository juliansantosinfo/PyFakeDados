import random
from PyFakeDados.CONSTANTS_NOMES import *
from PyFakeDados.sexo import gerar_sexo

LISTA_NOMES_MASCULINOS = NOMES_MASCULINOS
LISTA_NOMES_FEMININOS = NOMES_FEMININOS
SOBRENOMES = SOBRENOMES

def gerar_nome(sexo=None, composto=False):
    
    nome = ''
    segundo_nome = ''

    if sexo is None:
        sexo = gerar_sexo()

    if composto is None:
        composto = random.choice([True, False])

    if sexo == 'M':
        nome = random.choice(LISTA_NOMES_MASCULINOS)
        if composto:
            segundo_nome = random.choice(LISTA_NOMES_MASCULINOS)
    elif sexo == 'F':
        nome = random.choice(LISTA_NOMES_FEMININOS)
        if composto:
            segundo_nome = random.choice(LISTA_NOMES_FEMININOS)
    else:
        raise ValueError("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
    
    if composto:
        nome = f"{nome} {segundo_nome}"
    else:
        nome = f"{nome}"
    
    return nome

def gerar_sobrenome():
    return random.choice(SOBRENOMES)

def gerar_nome_completo(sexo=None, composto=False):

    if sexo is None:
        sexo = gerar_sexo()
    
    if composto is None:
        composto = random.choice([True, False])

    nome = gerar_nome(sexo=sexo, composto=composto)
    sobrenome = gerar_sobrenome()
    nome_completo = f"{nome} {sobrenome}"

    return nome_completo

def gerar_nome_com_filiacao():

    nome_mae = gerar_nome_completo(sexo='F')
    nome_pai = gerar_nome_completo(sexo='M')

    sobrenome_mae = nome_mae.split().pop()
    sobrenome_pai = nome_pai.split().pop()

    nome = gerar_nome()
    nome = f"{nome} {sobrenome_mae} {sobrenome_pai}"

    return nome, nome_mae, nome_pai