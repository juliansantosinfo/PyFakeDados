import random

tipos_logradouros = ['Rua', 'Avenida', 'Estrada', 'Beco', 'Travessa', 'Alameda', 'Viela']
prefixos = ['Do', 'Dos', 'Das', 'De', 'Doutor', 'Dom', 'Vila', 'Chácara', 'Sítio']
sufixos = ['Novo', 'Velho', 'Grande', 'Pequeno', 'Alto', 'Baixo', 'Leste', 'Oeste', 'Norte', 'Sul']

def gerar_logradouro():
    
    tipo = random.choice(tipos_logradouros)
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    numero = str(random.randint(1,2000))
    
    return f'{tipo} {prefixo} {sufixo}, {numero}'
