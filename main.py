import json
from PyFakeDados.empresa import gerar_empresa
from PyFakeDados.pessoa import gerar_pessoa
from PyFakeDados.nome import gerar_nome_com_filiacao

gerar_nome_com_filiacao()

uf = 'SP'

empresa = gerar_empresa(uf)
empresa = json.dumps(empresa, indent=4, ensure_ascii=False)
print(empresa)

pessoa = gerar_pessoa(mask=True)
pessoa = json.dumps(pessoa, indent=4, ensure_ascii=False)
print(pessoa)