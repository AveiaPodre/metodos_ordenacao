from sort_methods import *
from time import time
nomes = ''
try:
    with open(f'nomes10K.txt', 'r+', encoding='utf-8') as arquivo:
        for nome in arquivo:
            nomes = nomes + nome
except:
    print('Erro na leitura do arquivo!')

nomes = nomes.split('\n')
print(bubble_sort(nomes))

