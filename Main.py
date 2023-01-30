from unidecode import unidecode
from sort_methods import *
from time import time
nomes = ''
try:
    with open(f'nomes500K.txt', 'r+', encoding='utf-8') as arquivo:
        for nome in arquivo:
            nomes = nomes + nome
except:
    print('Erro na leitura do arquivo!')
nomes = unidecode(nomes)
nomes = nomes.split('\n')
nomes = [x.lower() for x in nomes if x[0].isupper()]
tempo_inicial = time()
nomes = merge_sort(nomes)
tempo_final = time()
print(tempo_final-tempo_inicial)
