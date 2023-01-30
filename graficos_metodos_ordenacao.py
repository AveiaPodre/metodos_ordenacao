import pandas as pd
import matplotlib.pyplot as plt
import sort_methods
# Carregar dados
df = pd.DataFrame({'tempo': [1, 2, 3, 4, 5],
                   'quantidade': [20, 10, 30, 47, 100]})

# Traçar gráfico
df.plot(x='tempo', y='quantidade', kind='line')

# Adicionar labels e título
plt.xlabel('Tempo (em dias)')
plt.ylabel('Quantidade vendida')
plt.title('Quantidade vendida por dia')

# Mostrar gráfico
plt.show()


#esse arquivo aqui era só um teste que eu tava fazendo