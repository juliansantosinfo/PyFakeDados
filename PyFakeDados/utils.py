from unidecode import unidecode

def remover_acentos(texto):
    texto_sem_acentos = unidecode(texto)
    return texto_sem_acentos
