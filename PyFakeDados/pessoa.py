import random
from datetime import datetime, timedelta
from .nome import gerar_sexo, gerar_nome, gerar_sobrenome, gerar_nome_completo, gerar_nome_com_filiacao
from .cep import gerar_cep
from .estado import gerar_estado, gerar_uf, busca_nome_uf
from .municipio import gerar_municipio
from .bairro import gerar_bairro
from .logradouro import gerar_logradouro, gerar_numero
from .telefone import gerar_telefone_fixo, gerar_telefone_celular
from .email import gerar_email, gerar_email_pessoa
from .senha import gerar_senha, gerar_senha_numerica
from .site import gerar_site
from .cpf import gerar_cpf
from .ctps import gerar_ctps
from .pis import gerar_pis
from .utils import gerar_data, gerar_data_nascimento

def gerar_pessoa(uf=None, mask=False, idade=None, recem_nascido=False):

    if uf is None:
        uf = gerar_uf()

    if idade is None:
        
        idade_min = 1
        idade_max = 99

        if recem_nascido:
            idade_min = 0

        idade = random.randint(idade_min, idade_max)

    pessoa = {}
    data_nascimento = gerar_data_nascimento(idade)
    
    sexo = gerar_sexo()
    nome, mae, pai = gerar_nome_com_filiacao()
    cpf = gerar_cpf(mask=mask)
    ctps = gerar_ctps()
    pis = gerar_pis()
    data_nascimento = data_nascimento
    site = gerar_site(nome)
    email = gerar_email_pessoa(nome)
    senha = gerar_senha_numerica()
    senha_forte = gerar_senha(16)
    cep = gerar_cep(uf, mask=mask)
    endereco = gerar_logradouro()
    numero = gerar_numero()
    bairro = gerar_bairro()
    municipio = gerar_municipio(uf)
    estado = busca_nome_uf(uf)
    telefone = gerar_telefone_fixo(uf, mask=mask)
    celular = gerar_telefone_celular(uf)

    pessoa = {
        "sexo": sexo,
        "nome": nome,
        "mae": mae,
        "pai": pai,
        "cpf": cpf,
        "ctps": ctps,
        "pis": pis,
        "data_nascimento": data_nascimento.strftime("%d/%m/%Y"),
        "site": site,
        "email": email,
        "senha": senha,
        "senha_forte": senha_forte,
        "cep": cep,
        "endereco": endereco,
        "numero": numero,
        "bairro": bairro,
        "municipio": municipio,
        "estado": estado,
        "uf": uf,
        "telefone": telefone,
        "celular": celular,
    }

    return pessoa
