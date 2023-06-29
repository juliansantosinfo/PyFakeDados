import random

def gerar_nome_empresa():
    segmento = ['Tecnologia', 'Soluções', 'Consultoria', 'Indústria', 'Comércio', 'Energia', 'Engenharia', 'Logística', 'Agro', 'Farmacêutica', 'Cerâmica', 'Madeireira', 'Marcenaria', 'Construtora', 'Metalurgica']
    palavra1 = ['Nova', 'Primeira', 'Global', 'Mega', 'Excel', 'Pro', 'Super', 'Ultra', 'Master', 'Max', 'Top']
    palavra2 = ['Tecnologia', 'Soluções', 'Consultoria', 'Indústria', 'Comércio', 'Energia', 'Engenharia', 'Logística', 'Agro', 'Farmacêutica']
    palavra3 = ['S/A', 'LTDA', 'Ltda.', 'EIRELI', 'ME', 'S.A.', 'Group']
    
    segmento_escolhido = random.choice(segmento)
    palavra1_escolhida = random.choice(palavra1)
    palavra2_escolhida = random.choice(palavra2)
    palavra3_escolhida = random.choice(palavra3)
    
    return f'{segmento_escolhido} {palavra1_escolhida} {palavra2_escolhida} {palavra3_escolhida}'

# Exemplo de uso
nome_empresa = gerar_nome_empresa()
print(nome_empresa)
