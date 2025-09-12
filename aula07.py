import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criação de um dataset fictício
np.random.seed(42)

dados = pd.DataFrame({
    "Orcamento_Campanha": np.random.randint(1000, 5000, size=100),
    "Visualizacoes_Anuncio": np.random.randint(2000, 20000, size=100),
    "Vendas": np.random.randint(10, 10000, size=100),
    "Cliques": np.random.randint(100, 20000, size=100)
})

# Pairplot: Visualizar todas as relaçoes
sns.pairplot(dados)
plt.show()
plt.savefig('pairplot7.png')

#Joingtplot: explorar a relação entre duas variaveis especificas especificas
sns.jointplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados, kind="reg")
plt.show()
plt.savefig('jointplot.png')

#Lmplot: Visualizar a linha de regressão
sns.lmplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados)
plt.show()
plt.savefig('lmplot7.png')